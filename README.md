

https://vehicles-env-33zh.onrender.com/
# 🚗 Data on the Road: Interactive Car Sales Dashboard with Streamlit & Render

## 📌 Introduction
This project demonstrates how to go beyond traditional notebooks and build a **fully interactive web dashboard**.  
Using **Streamlit, Plotly, and Render cloud deployment**, the app allows users to explore a dataset of used car listings (`vehicles_us.csv`) through dynamic visualizations.  

The project highlights skills in:
- **Software engineering for data apps**  
- **EDA (Exploratory Data Analysis)**  
- **Web app development with Streamlit**  
- **Cloud deployment with Render**  

---

## 📂 Dataset
Default dataset: `vehicles_us.csv` (used car listings)  
Fields include:  
- Vehicle attributes (model, odometer, price, etc.)  
- Listing details (year, condition, cylinders, fuel type, etc.)  

👉 Note: The app is dataset-agnostic — any CSV file can be adapted for analysis.  

---
## 🛠️ Methodology

### 1. Environment Setup
- **Python virtual environment**
- **Dependencies:** `pandas`, `plotly`, `streamlit`

### 2. Exploratory Data Analysis (EDA)
- Conducted in `notebooks/EDA.ipynb`
- Used **Plotly** for interactive histograms & scatter plots

### 3. Web App Development
- Built with **Streamlit** (`app.py`)
- **Features:**
  - Header & description  
  - Button/checkbox interactivity  
  - Interactive histogram  
  - Interactive scatter plot  

### 4. Cloud Deployment
- Hosted via **Render.com**
- Configured `requirements.txt` and deploy commands
- Accessible via a public URL

---

## 📊 App Features
- Histogram visualization (e.g., odometer distribution)
- Scatter plot visualization (e.g., price vs mileage)
- Interactive controls (buttons / checkboxes)
- Responsive Plotly charts

---

## ✅ Conclusion
This project showcases how to:
- Transition from **EDA in Jupyter** → to **production‑ready dashboards**
- Use **Streamlit** for rapid web app prototyping
- Deploy apps to the cloud (**Render**) for global access  

It demonstrates both **data science** and **software engineering** skills, making it highly relevant for end‑to‑end data product development.

---

## 💻 Tech Stack
- Python
- Pandas
- Plotly
- Streamlit
- Render (Cloud Deployment)
- Jupyter Notebook
