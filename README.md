# 🔐 LinkShield AI

LinkShield AI is a real-time phishing URL detection web application that uses machine learning to classify URLs as **safe or malicious**.

It combines a trained ML model with a modern web interface to provide instant threat analysis.

---

## 🚀 Features

- 🔍 Real-time URL scanning
- 🤖 Machine Learning-based detection
- ⚡ FastAPI backend for prediction API
- 🌐 Interactive frontend (HTML, CSS, JS)
- 🎯 High accuracy (~95%)
- 🧠 Feature-based URL analysis (112 features)
- 💡 Clean and modern UI

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI (Python)  
- **Machine Learning:** Scikit-learn (Random Forest)  
- **Deployment:** Render  

---

## 📁 Project Structure
LinkShield/
│
├── model.pkl # Trained ML model
├── phishing.csv # Dataset
├── train_model.py # Model training script
├── main.py # FastAPI backend
├── requirements.txt # Dependencies
│
└── static/
├── index.html # Frontend UI
├── style.css # Styling
└── script.js # Frontend logic

---

## ⚙️ How It Works

1. User enters a URL  
2. Frontend sends request to `/predict` API  
3. Backend extracts features & runs model  
4. Model returns prediction  
5. UI displays result (Safe / Phishing)

---


