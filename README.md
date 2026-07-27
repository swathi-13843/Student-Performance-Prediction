# 🎓 Student Performance Prediction System Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black) ![SQLite](https://img.shields.io/badge/SQLite-Database-green) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)

## 📖 Overview

The **Student Performance Prediction System** is a Machine Learning web application developed using **Python, Flask, Scikit-learn, and SQLite**. The application predicts a student's final score based on study hours, attendance, and previous academic performance. It provides a user-friendly interface, graphical visualization, and an admin dashboard for managing prediction records stored in an SQLite database.

---

## ✨ Features

- Predict student final performance using Machine Learning
- Interactive web application built with Flask
- SQLite database integration
- Automatic database and table creation
- Secure admin login
- Prediction history dashboard
- Performance category classification
- Graph visualization using Matplotlib
- Input validation
- Download prediction records
- Responsive user interface using Bootstrap

---

## 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Framework | Flask |
| Machine Learning | Scikit-learn |
| Database | SQLite |
| Libraries | Pandas, NumPy, Matplotlib, Pickle |
| Frontend | HTML5, CSS3, Bootstrap |
| Version Control | Git, GitHub |

---

## 📂 Project Structure

```text
Student-Performance-Prediction/
│── app.py
│── model.pkl
│── accuracy.txt
│── student.db
│── requirements.txt
│── README.md
│── LICENSE
│── .gitignore
│
├── static/
│   └── graph.png
│
└── templates/
    ├── index.html
    ├── admin_login.html
    └── dashboard.html
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/swathi-13843/Student-Performance-Prediction.git
```

### Navigate to Project

```bash
cd Student-Performance-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📊 Input Parameters

- Study Hours
- Attendance Percentage
- Previous Score

---

## 📈 Output

- Predicted Final Score
- Performance Category
- Prediction Graph
- Prediction History

---

## 🗄 Database

**Database:** `student.db`

**Table:** `predictions`

| Column |
|---------|
| id |
| study_hours |
| attendance |
| previous_score |
| predicted_score |
| category |

The database is automatically created when the application starts.

---

## 🔐 Admin Login

| Username | Password |
|----------|----------|
| admin | 1234 |

---

## 🚀 Future Enhancements

- User Authentication
- CSV & PDF Report Export
- Multiple Machine Learning Models
- Cloud Deployment
- Deep Learning Integration
- Email Notifications
- Performance Analytics Dashboard

---

## 📚 Learning Outcomes

- Machine Learning Model Development
- Flask Web Application Development
- SQLite Database Integration
- Data Visualization
- Data Preprocessing
- Backend Development
- Frontend Development
- Git & GitHub Workflow
- Machine Learning Deployment

---

## 👩‍💻 Author

**Maloth Swathi**

B.Tech – Computer Science and Data Science  
Malla Reddy University

**GitHub:** https://github.com/swathi-13843

---

## ⭐ Support

If you found this project useful, please consider **starring ⭐ the repository**.
