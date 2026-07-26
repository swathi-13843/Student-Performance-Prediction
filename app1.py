#import Libraries
from flask import Flask, render_template, request, redirect, url_for, session, send_file
import pandas as pd
import numpy as np
import csv
import pickle
import matplotlib.pyplot as plt
import os

#Load trained models
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Load Accuracy
with open("accuracy.txt", "r") as f:
    accuracy = f.read()

#Create FLASK App
app = Flask(__name__)
app.secret_key = "supersecretkey"

#HomePage
@app.route("/")
def home():
    return render_template("index.html")

#Admin Page
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Simple Hardcoded Login
        if username == "admin" and password == "1234":
            session["admin"] = True
            return redirect(url_for("dashboard"))
        else:
            return render_template("admin_login.html", error="Invalid Credentials")

    return render_template("admin_login.html")

#Dashboard Page
@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect(url_for("admin"))
    try:
        data = pd.read_csv("results.csv")
        records = data.values.tolist()
    except:
        records = []
    return render_template("dashboard.html", records=records)

#Download Page
@app.route("/download")
def download():
    if not session.get("admin"):
        return redirect(url_for("admin"))
    return send_file("results.csv", as_attachment=True)

#Logout Page
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("home"))

#Prediction Page
@app.route("/predict", methods=["POST"])
def predict():
    try:
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        previous = float(request.form["previous"])
        
        #Input Validation
        if hours < 0:
            return render_template("index.html", error="Study hours cannot be negative.")
        
        if hours > 12:
            return render_template("index.html", error="Study hours cannot exceed 12 per day.")
        
        if attendance < 0:
            return render_template("index.html", error="Attendance cannot be negative.")
        
        if attendance > 100:
            return render_template("index.html", error="Attendance cannot exceed 100%.")
        
        if previous < 0:
            return render_template("index.html", error="Previous score cannot be negative.")
        
        if previous > 100:
            return render_template("index.html", error="Previous score cannot exceed 100.")
        
        #Predction
        input_data = pd.DataFrame(
            [[hours, attendance, previous]],
            columns=["hours_studied", "attendance", "previous_score"]
        )
        
        prediction = model.predict(input_data)
        final_result = round(prediction[0],2)
        
        #Restrict final score
        if final_result > 100:
            final_result=100
        
        # Create Graph
        plt.figure()
        plt.scatter(hours, final_result)
        plt.xlabel("Study Hours")
        plt.ylabel("Predicted Score")
        plt.title("Study Hours vs Final Score")

        # Create static folder if not exists
        if not os.path.exists("static"):
            os.makedirs("static")

        graph_path = "static/graph.png"
        plt.savefig(graph_path)
        plt.close()
        
        # Performance Category
        if final_result >= 80:
            category = "Excellent"
        elif final_result >= 60:
            category = "Good"
        elif final_result >= 40:
            category = "Average"
        else:
            category = "Needs Improvement"
                    
        #Save User Outputs in CSV File
        with open("results.csv", "a", newline="") as file:
            writer = csv.writer(file);
            writer.writerow([hours, attendance, previous, final_result])
            
        return render_template("index.html",
                       result=final_result,
                       category=category,
                       accuracy=accuracy,
                       hours=hours,
                       attendance=attendance,
                       previous=previous,
                       graph=True)
    
    except:
        return render_template("index.html", error="Invalid input, Please enter a valid numbers.")
    
#RUN APP
if __name__ == "__main__":
    app.run(debug=True)