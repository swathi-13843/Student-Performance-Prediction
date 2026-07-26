import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pickle

#Load Dataset
data = pd.read_csv("data.csv")

X = data[["hours_studied","attendance","previous_score"]]
y = data["final_score"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

#Train Model
model = LinearRegression()
model.fit(X, y)

# Calculate Accuracy
predictions=model.predict(X_test)
accuracy = r2_score(y_test, predictions)

#Save Model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
    
# Save Accuracy
with open("accuracy.txt", "w") as f:
    f.write(str(round (accuracy , 4)))

print("Model trained and saved successfully.")
print("Model Accuracy:", round(accuracy, 4))