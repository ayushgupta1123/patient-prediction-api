# 🛡️ InsureAI — Insurance Premium Category Predictor

<p align="center">
  <strong>AI-Powered Insurance Premium Category Prediction System</strong>
</p>

<p align="center">
  An end-to-end Machine Learning application built with Python, FastAPI, Scikit-learn and Streamlit.
</p>

<p align="center">

  <a href="YOUR_STREAMLIT_APP_URL">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-red?style=for-the-badge" alt="Live Demo">
  </a>

  <a href="https://github.com/ayushgupta1123/patient-prediction-api">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" alt="GitHub">
  </a>

  <a href="http://127.0.0.1:8000/docs">
    <img src="https://img.shields.io/badge/API-Swagger-green?style=for-the-badge&logo=fastapi" alt="API Docs">
  </a>

</p>

---

## 📌 Overview

**InsureAI** is an end-to-end Machine Learning application designed to predict an insurance premium category based on customer demographic, financial, lifestyle and occupational information.

The project combines a trained Machine Learning model with a **FastAPI REST API** and a modern **Streamlit web interface**.

Users can enter customer information through the Streamlit dashboard. The frontend sends the information to the FastAPI backend, where additional features are calculated and passed to the trained Machine Learning model. The prediction is then returned to the frontend and displayed to the user.

### Core Workflow

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI REST API
  ↓
Feature Engineering
  ↓
Machine Learning Model
  ↓
Prediction
  ↓
Streamlit Dashboard
```

---

# 🚀 Live Demo

### 🌐 Live Application

**Live Demo:** `Coming Soon`

> The application will be publicly available after deploying the FastAPI backend and Streamlit frontend.

---

# ✨ Features

### 🤖 Machine Learning

- Machine Learning based insurance premium category prediction
- Pre-trained model loaded using Pickle
- Feature engineering before prediction
- BMI calculation
- Age group classification
- Lifestyle risk classification
- City tier classification

### ⚡ Backend

- FastAPI REST API
- Pydantic request validation
- `/predict` prediction endpoint
- Automatic Swagger API documentation
- Error handling
- JSON request/response architecture

### 🎨 Frontend

- Modern Streamlit dashboard
- Light Mode
- Dark Mode
- Customer profile form
- Live BMI calculation
- Profile overview cards
- Prediction result dashboard
- API request/response viewer
- Input validation
- Connection error handling
- Timeout handling
- Responsive interface

---

# 🏗️ System Architecture

```text
                         ┌─────────────────┐
                         │      USER       │
                         └────────┬────────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │                         │
                    │    STREAMLIT FRONTEND   │
                    │       frontend.py       │
                    │                         │
                    └────────────┬────────────┘
                                 │
                                 │ HTTP POST
                                 │ /predict
                                 ▼
                    ┌─────────────────────────┐
                    │                         │
                    │       FASTAPI           │
                    │        app.py           │
                    │                         │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │                         │
                    │   FEATURE ENGINEERING   │
                    │                         │
                    │  • BMI                  │
                    │  • Age Group            │
                    │  • Lifestyle Risk       │
                    │  • City Tier            │
                    │                         │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │                         │
                    │    ML MODEL             │
                    │     model.pkl           │
                    │                         │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │                         │
                    │   PREDICTION RESULT     │
                    │                         │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │                         │
                    │    STREAMLIT UI         │
                    │                         │
                    └─────────────────────────┘
```

---

# 🧠 Machine Learning Pipeline

The application receives customer information through the frontend and sends it to the FastAPI backend.

The backend performs feature engineering before sending the processed information to the trained Machine Learning model.

## Input Features

| Feature | Description |
|---|---|
| Age | Customer age in years |
| Weight | Customer weight in kilograms |
| Height | Customer height in metres |
| Income | Annual income in LPA |
| Smoker | Smoking status |
| City | Customer city |
| Occupation | Customer occupation |

## Derived Features

The backend calculates additional features including:

- **BMI**
- **Age Group**
- **Lifestyle Risk**
- **City Tier**

These features are then passed to the trained Machine Learning model.

---

# 📊 Prediction Workflow

```text
Customer Information
        │
        ▼
Streamlit Frontend
        │
        ▼
JSON Request
        │
        ▼
FastAPI /predict
        │
        ▼
Request Validation
        │
        ▼
Feature Engineering
        │
        ├── BMI
        ├── Age Group
        ├── Lifestyle Risk
        └── City Tier
        │
        ▼
Machine Learning Model
        │
        ▼
Premium Category
        │
        ▼
Streamlit Result
```

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Pickle

## Backend

- FastAPI
- Uvicorn
- Pydantic
- REST API

## Frontend

- Streamlit
- HTML
- CSS

## Development Tools

- Git
- GitHub
- VS Code

---

# 📂 Project Structure

```text
patient-prediction-api/
│
├── app.py
│       └── FastAPI backend and prediction endpoint
│
├── frontend.py
│       └── Streamlit user interface
│
├── model.pkl
│       └── Trained Machine Learning model
│
├── patients.json
│       └── Project data
│
├── requirement.txt
│       └── Python dependencies
│
├── README.md
│       └── Project documentation
│
└── .gitignore
        └── Git ignored files
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ayushgupta1123/patient-prediction-api.git
```

## 2. Navigate to the Project

```bash
cd patient-prediction-api
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv myenv
```

Activate the environment:

```bash
myenv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv myenv
```

Activate the environment:

```bash
source myenv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirement.txt
```

---

# ▶️ Run the FastAPI Backend

Open **Terminal 1**:

```bash
uvicorn app:app --reload
```

The FastAPI backend will run at:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger interface to test the prediction endpoint without using the Streamlit frontend.

---

# 🎨 Run the Streamlit Frontend

Open **Terminal 2**.

Make sure your virtual environment is activated, then run:

```bash
streamlit run frontend.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

# 🔌 API

## POST `/predict`

The Streamlit frontend sends customer information to the FastAPI `/predict` endpoint.

### Endpoint

```text
POST http://127.0.0.1:8000/predict
```

### Example Request

```json
{
    "age": 30,
    "weight": 65,
    "height": 1.70,
    "income_lpa": 10,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
}
```

### Example Python Request

```python
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "age": 30,
    "weight": 65,
    "height": 1.70,
    "income_lpa": 10,
    "smoker": False,
    "city": "Mumbai",
    "occupation": "private_job"
}

response = requests.post(
    url,
    json=data
)

print(response.json())
```

### Example Response

```json
{
    "predicted_category": "..."
}
```

---

# 🖥️ Frontend

The Streamlit frontend provides a modern dashboard for interacting with the Machine Learning model.

## 👤 Customer Profile

Users can enter:

- Age
- Weight
- Height
- Annual Income
- Smoking Status
- City
- Occupation

## 📊 Profile Overview

The dashboard automatically displays:

- Age
- BMI
- Income
- City
- BMI classification

## 🌙 Theme Support

The interface supports:

```text
☀️ Light Mode
🌙 Dark Mode
```

## 🎯 Prediction

After clicking:

```text
🔮 Predict Insurance Premium Category
```

the frontend sends the customer information to the FastAPI backend and displays the Machine Learning prediction.

---

# 🛡️ Error Handling

The application includes handling for common errors such as:

- Invalid user input
- FastAPI server unavailable
- Connection errors
- Request timeout
- HTTP errors
- Invalid API response
- Unexpected application errors

If the FastAPI server is not running, the Streamlit frontend displays an appropriate error message instead of crashing.

---

# 🧪 Testing

## Test FastAPI

Start the backend:

```bash
uvicorn app:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

Use the `/predict` endpoint to test the API.

## Test Streamlit

Start the frontend:

```bash
streamlit run frontend.py
```

Then open:

```text
http://localhost:8501
```

Enter customer information and click the prediction button.

---

# 🔄 End-to-End Application Flow

```text
                    USER
                     │
                     ▼
             ┌───────────────┐
             │   Streamlit   │
             │   Frontend    │
             └───────┬───────┘
                     │
                     │ JSON
                     ▼
             ┌───────────────┐
             │    FastAPI    │
             │    Backend    │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │ Validation &  │
             │ Feature       │
             │ Engineering   │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │  model.pkl    │
             │ ML Prediction │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   Prediction  │
             │    Result     │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   Streamlit   │
             │   Dashboard   │
             └───────────────┘
```

---

# ☁️ Deployment Architecture

For production deployment, the Streamlit frontend and FastAPI backend should be publicly accessible.

```text
                    INTERNET
                       │
                       ▼
            ┌─────────────────────┐
            │                     │
            │   Streamlit Cloud   │
            │                     │
            │    frontend.py      │
            │                     │
            └──────────┬──────────┘
                       │
                       │ HTTPS
                       ▼
            ┌─────────────────────┐
            │                     │
            │    FastAPI Server   │
            │                     │
            │       app.py        │
            │                     │
            └──────────┬──────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │                     │
            │      model.pkl      │
            │                     │
            │   ML Prediction     │
            │                     │
            └─────────────────────┘
```

> **Note:** During local development, the frontend uses `http://127.0.0.1:8000/predict`. For public deployment, this must be replaced with the public FastAPI URL.

---

# 🔐 Production Considerations

For a production-ready deployment, the following improvements can be implemented:

- HTTPS
- Environment variables for API URLs
- Authentication
- Database integration
- API rate limiting
- Logging
- Monitoring
- Docker
- CI/CD
- Cloud deployment
- Model versioning
- Automated testing

---

# 🚀 Future Improvements

- [ ] Deploy FastAPI backend
- [ ] Deploy Streamlit frontend
- [ ] Add live prediction URL
- [ ] Add prediction probability
- [ ] Add model performance dashboard
- [ ] Add confusion matrix visualization
- [ ] Add SHAP explainability
- [ ] Add prediction history
- [ ] Add user authentication
- [ ] Add PostgreSQL database
- [ ] Dockerize the application
- [ ] Add CI/CD pipeline
- [ ] Add application monitoring
- [ ] Add automated model retraining
- [ ] Add model versioning

---

# 🗺️ Roadmap

## Phase 1 — Machine Learning

- [x] Prepare dataset
- [x] Train Machine Learning model
- [x] Save trained model
- [x] Create prediction pipeline

## Phase 2 — Backend

- [x] Build FastAPI backend
- [x] Create `/predict` endpoint
- [x] Add request validation
- [x] Add feature engineering
- [x] Add API documentation

## Phase 3 — Frontend

- [x] Build Streamlit application
- [x] Create customer input form
- [x] Add BMI calculation
- [x] Add profile overview
- [x] Add prediction result
- [x] Add Light Mode
- [x] Add Dark Mode
- [x] Add API error handling

## Phase 4 — Deployment

- [ ] Deploy FastAPI
- [ ] Configure production API URL
- [ ] Deploy Streamlit
- [ ] Add public Live Demo
- [ ] Add deployment documentation

## Phase 5 — Production

- [ ] Docker
- [ ] PostgreSQL
- [ ] Authentication
- [ ] Monitoring
- [ ] CI/CD
- [ ] Model versioning
- [ ] Explainable AI

---

# 📸 Application Preview

Once the application is deployed, screenshots of the Streamlit dashboard can be added here.

Example:

```text
screenshots/
├── dashboard.png
├── prediction.png
└── dark-mode.png
```

---

# 📚 What This Project Demonstrates

This project demonstrates practical experience with:

- Python programming
- Machine Learning
- Feature engineering
- Model deployment
- REST APIs
- FastAPI
- Streamlit
- API integration
- JSON data exchange
- Input validation
- Error handling
- Git and GitHub
- Full-stack Machine Learning application development

---

# 👨‍💻 Author

## Ayush Gupta

**B.Tech — Computer Science Engineering**  
**Artificial Intelligence & Machine Learning**

### Areas of Interest

- 🤖 Machine Learning
- 📊 Data Science
- 🧠 Artificial Intelligence
- ✨ Generative AI
- ⚡ Backend Development
- 🔗 API Development
- 🚀 ML Deployment

---

# 🔗 Links

### GitHub Repository

https://github.com/ayushgupta1123/patient-prediction-api

### Live Application

Coming Soon

### API Documentation

Local:

http://127.0.0.1:8000/docs

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for educational, learning and portfolio purposes.


