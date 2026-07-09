# 🪐 EXOPLANET HABITABILITY ZONE ANALYSIS

Fabric Link: https://app.fabric.microsoft.com/groups/me/reports/5b165a7d-0301-44cb-9247-83aa32546ea3?ctid=77255288-5298-4ea5-81aa-a13e604c30ac&pbi_source=linkShare

> **"Where Data Meets Discovery"**

## 🚀 Project Overview
This project was developed as a graduation project for the **Digital Egypt Pioneers Initiative (DEPI) - Data Analysis Track**[cite: 1]. It utilizes real, continuously-updated observational data from NASA's Exoplanet Archive to identify which of the thousands of confirmed exoplanets fall inside their star's habitable zone (the "Goldilocks Zone") and to rank their physical similarity to Earth[cite: 1].

**Our Mission:** To explore distant worlds through data by analyzing exoplanet and stellar properties, revealing the conditions that make planets potentially habitable[cite: 1].

---

## 🏗️ Technical Architecture & Workflow
The analysis pipeline was built entirely with Python (pandas/NumPy) across a **Medallion Architecture (Bronze → Silver → Gold)**[cite: 1]. 

* **Data Modeling:** The Gold layer implements a robust Star Schema optimized for Power BI[cite: 1]. 
* It features one central `Fact_Exoplanets` table surrounded by four Dimension tables (`Dim_Planet`, `Dim_Star`, `Dim_Discovery`, `Dim_Date`)[cite: 1].

---

## 🔬 Data Engineering & Physics-Based Imputation
Instead of dropping missing values, we used astrophysics laws to recover missing data from the NASA archive[cite: 1]:
* **Kepler's Third Law:** Applied to calculate missing semi-major axes and orbital periods[cite: 1].
* **Stellar Relationships:** Used main-sequence power-law relationships to cross-fill missing stellar radii and masses[cite: 1].
* **Mass-Radius Relations:** Filled missing planet radii and masses by splitting the data into rocky vs. gaseous regimes[cite: 1].
* **Scientific Feature Engineering:** Derived new features that are not directly observed, including Stellar Luminosity (using the Stefan-Boltzmann law), Planet Received Flux (using the inverse-square law), and Equilibrium Temperature[cite: 1].

---

## 🤖 Machine Learning Models
To predict habitability, we trained two complementary models using `scikit-learn` and `XGBoost`[cite: 1]. We created custom features including the **Earth Similarity Index (ESI)** and habitability flags (based on flux and temperature windows)[cite: 1].

1. **Habitability Classifier (Random Forest):** 
   * Predicts if a planet is Habitable or Not Habitable[cite: 1].
   * Handled severe class imbalance (0.47% habitable planets) using a stratified train/test split and **SMOTE** oversampling[cite: 1].
2. **Earth Similarity Regressor (XGBoost):**
   * Predicts the ESI score on a 0-100 scale[cite: 1].
   * Tuned using **sample weights** to heavily penalize errors on high-ESI (highly Earth-like) planets, forcing the model to accurately recognize rare, habitable worlds[cite: 1].

---

## 📊 Power BI Dashboard
The final deliverable is a 7-page interactive Power BI dashboard featuring a custom-designed cosmic/nebula visual identity prototyped in Figma[cite: 1]. 

**Dashboard Pages:**
* **Overview:** Discovery history, distance histograms, and binary system shares[cite: 1].
* **Habitability:** Physical and orbital characteristics (validating Kepler's Third Law visually)[cite: 1].
* **Star Systems:** Host star properties and Hertzsprung-Russell-style diagrams[cite: 1].
* **Planet Explorer:** The "Goldilocks Zone" scatter plots and top 10 Earth-like planet rankings[cite: 1].
* **AI Model:** A fully interactive page with live slicers where users can input parameters and a Python visual runs the classifier and regressor on the fly[cite: 1].

---

## 🛠️ Tools & Technologies Used
* **Data Source:** NASA Exoplanet Archive (Caltech / IPAC)[cite: 1]
* **Data Processing & ML:** Python (pandas, NumPy, scikit-learn, XGBoost, imbalanced-learn, joblib)[cite: 1]
* **Visualization & BI:** Power BI, Matplotlib/Seaborn, Figma[cite: 1]
* **App Deployment:** Streamlit[cite: 1]

---

## 👥 Project Team
* **DEPI Data Analysis Track (2025/2026)**[cite: 1]
* **Team Members:** Nourhan Khalifa, Hannah Hany, Reham Osama, Mohamed Essam, Youssef Abdullah, Youssef Amir[cite: 1]
* **Supervisor:** Eng. Mohamed El-Eman[cite: 1]
