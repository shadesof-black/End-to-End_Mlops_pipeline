# 💎 End-to-End Diamond Price Prediction MLOps Pipeline

An end-to-end Machine Learning Operations (MLOps) project that predicts diamond prices using a production-ready ML pipeline. The project demonstrates the complete ML lifecycle—from data versioning and model training to workflow orchestration and deployment using modern MLOps tools. :contentReference[oaicite:0]{index=0}

---

## 🌐 Live Demo

🚀 **Web Application:** https://diamond-price-app-latest.onrender.com/

📂 **GitHub Repository:** https://github.com/shadesof-black/End-to-End_Mlops_pipeline.git

---

# 📌 Project Overview

This project automates the complete machine learning workflow for predicting diamond prices.

It includes:

- ✅ Data Ingestion
- ✅ Data Validation
- ✅ Data Transformation
- ✅ Model Training
- ✅ Model Evaluation
- ✅ Model Selection
- ✅ Data Version Control (DVC)
- ✅ Experiment Tracking (MLflow)
- ✅ Workflow Orchestration (Apache Airflow)
- ✅ Flask Web Application
- ✅ Docker Containerization
- ✅ Cloud Deployment

---

# 🛠 Tech Stack

### Machine Learning
- Python
- Scikit-Learn
- XGBoost
- CatBoost
- LightGBM
- Pandas
- NumPy

### MLOps
- Apache Airflow
- DVC
- MLflow
- Docker

### Backend
- Flask

### Deployment
- Render

### Version Control
- Git
- GitHub

---

# 📂 Project Structure

```
End-to-End_Mlops_pipeline
│
├── airflow/
├── artifacts/
├── src/
├── templates/
├── static/
├── app.py
├── Dockerfile
├── docker-compose.yaml
├── dvc.yaml
├── requirements.txt
└── README.md
```

---

# 🔄 Complete MLOps Pipeline

```
Raw Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
Model Serialization
      │
      ▼
Flask Prediction API
      │
      ▼
Web Deployment
```

---

# ⚙ Workflow

### 1️⃣ Data Ingestion

- Reads raw diamond dataset
- Splits train/test data
- Stores processed files

---

### 2️⃣ Data Transformation

- Missing value handling
- Feature preprocessing
- Encoding categorical variables
- Feature scaling

---

### 3️⃣ Model Training

Multiple regression algorithms are trained.

Examples:

- Linear Regression
- Random Forest
- Decision Tree
- XGBoost
- CatBoost
- LightGBM

The best performing model is automatically selected.

---

### 4️⃣ Experiment Tracking

MLflow tracks:

- Parameters
- Metrics
- Model artifacts
- Training history

---

### 5️⃣ Data Versioning

DVC tracks:

- Dataset versions
- Pipeline stages
- Artifacts

Ensuring reproducible machine learning experiments.

---

### 6️⃣ Workflow Automation

Apache Airflow orchestrates the complete ML pipeline.

Tasks include:

- Data Ingestion
- Data Transformation
- Model Training
- Model Evaluation

---

### 7️⃣ Model Deployment

The trained model is deployed using Flask.

Users can:

- Enter diamond specifications
- Predict price instantly
- Access the application through a web interface

---

# 📷 Screenshots

## 🏠 Home Page

> Replace with your screenshot

```markdown
![Home Page](images/home.png)
```

---

## 📋 Prediction Form

```markdown
![Prediction Form](images/form.png)
```

---

## 💰 Prediction Result

```markdown
![Prediction Result](images/result.png)
```

---


## ✅ Airflow Successful Pipeline

```markdown
![Airflow Success](images/airflow_success.png)
```

---

## 🏆 Best Model Selection

```markdown
![Best Model](images/best_model_terminal.png)
```

---

# 🚀 Deployment

The application is deployed on Render.

### Live URL

https://diamond-price-app-latest.onrender.com/

---

# 📊 Features

- End-to-End ML Pipeline
- Modular Project Structure
- Production Ready Code
- Automated Model Training
- Multiple Model Comparison
- Automatic Best Model Selection
- Airflow Workflow Automation
- DVC Version Control
- MLflow Experiment Tracking
- Flask Prediction API
- Responsive User Interface
- Docker Support
- Cloud Deployment

---

# ▶️ Run Locally

Clone the repository

```bash
git clone https://github.com/shadesof-black/End-to-End_Mlops_pipeline.git
```

Move into the project

```bash
cd End-to-End_Mlops_pipeline
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
python app.py
```

Open

```
http://localhost:8000
```

---

# 🐳 Docker

Build image

```bash
docker build -t diamond-price-app .
```

Run container

```bash
docker run -p 8000:8000 diamond-price-app
```

---

# 🎯 Future Improvements

- CI/CD using GitHub Actions
- Kubernetes Deployment
- AWS Cloud Deployment
- Model Monitoring
- Data Drift Detection
- Automated Retraining
- REST API Documentation

---

# 👨‍💻 Author

**Rahul Raj**


GitHub:
https://github.com/shadesof-black

---

# ⭐ If you found this project useful, don't forget to Star the repository!