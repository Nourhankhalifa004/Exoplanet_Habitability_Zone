# 🪐 Exoplanet Habitability Zone Analysis

**Digital Egypt Pioneers Initiative (DEPI) — Data Analysis Track**
**Graduation Project — 2025/2026**

> *"Where Data Meets Discovery"*

A full data analytics pipeline that identifies which confirmed exoplanets fall inside their star's habitable zone ("Goldilocks Zone") and ranks how physically similar each one is to Earth — built on real, continuously-updated NASA data.

---

## 👥 Project Team

| Name | Name |
|---|---|
| Nourhan Khalifa | Mohamed Essam |
| Hannah Hany | Youssef Abdullah |
| Reham Osama | Youssef Amir |

**Supervisor:** Eng. Mohamed El-Eman

---

## 📖 Overview

This project takes raw, real observational data from the **NASA Exoplanet Archive** and turns it into:

1. A cleaned, dimensionally-modeled dataset (Medallion Architecture: Bronze → Silver → Gold)
2. A set of scientific habitability calculations (Earth Similarity Index, escape velocity, equilibrium temperature, stellar flux)
3. An interactive **Power BI dashboard** with 7 pages of discovery, physical, stellar, and habitability analysis
4. A **machine learning model** that predicts whether a hypothetical planet is habitable, and how Earth-like it is, live inside the dashboard and through a standalone Streamlit app

---

## 🗂️ Data Sources

| Source | Description |
|---|---|
| [NASA Exoplanet Archive — Planetary Systems (PS) Table](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS) | Primary dataset — real, daily-updating observational data on confirmed exoplanets |
| Parallax export (same archive) | Used to fill missing system distances via the distance-modulus law |
| [ExoHabX — Habitable Exoplanets Dataset (NASA/HWC)](https://www.kaggle.com/datasets/walididbennacer/exohabx-habitable-exoplanets-dataset-nasa-hwc) | Kaggle dataset with a pre-computed Habitable Worlds Catalog ESI score, used to train the ML models |

> ⚠️ Because the NASA archive updates daily as new exoplanets are confirmed, row counts and statistics reported in the notebooks/documentation reflect the snapshot downloaded at the time — a fresh download will differ slightly.

---

## 🏗️ Architecture

```
NASA Exoplanet Archive (raw CSV)
        │
        ▼
┌───────────────┐
│  Bronze Layer │  raw ingestion, no transformation
└───────────────┘
        │
        ▼
┌───────────────┐
│  Silver Layer │  cleaning, physics-based imputation, feature derivation
└───────────────┘
        │
        ▼
┌───────────────┐
│  Gold Layer   │  star-schema dimensional model (Fact + 4 Dim tables)
└───────────────┘
        │
        ▼
┌────────────────────┐
│  EDA / Enrichment  │  ESI, escape velocity, habitability flags
└────────────────────┘
        │
        ├──────────────► Power BI Dashboard (7 pages)
        └──────────────► ML Models (Habitability Classifier + ESI Regressor)
```

### Star Schema (Gold Layer)

- **Fact_Exoplanets** — central fact table linking every planet to its star, discovery record, and date
- **Dim_Planet** — orbital & physical properties + habitability flags (ESI, is_habitable, is_rocky)
- **Dim_Star** — host star temperature, mass, luminosity, distance
- **Dim_Discovery** — discovery method & year
- **Dim_Date** — discovery year, for time-series visuals

---

## 🧪 Data Cleaning Highlights

The raw NASA extract had substantial missing data, solved with real physics rather than simple dropping wherever possible:

- **Stellar radius/mass** → filled using the Radius–Mass relationship for main-sequence stars
- **Semi-major axis / orbital period** → filled iteratively using **Kepler's Third Law**
- **Eccentricity** → filled with a small random value for close-in orbits (near-circular assumption)
- **Planet radius/mass** → filled using the Mass–Radius relation, split by rocky vs. gaseous regime
- **System distance** → filled via the **Distance-Modulus Law**, using a merged parallax dataset
- Remaining unrecoverable rows were dropped

New scientific columns derived: **Stellar Luminosity** (Stefan–Boltzmann Law), **Received Flux** (inverse-square law), **Planet Equilibrium Temperature**, **Escape Velocity**, and the **Earth Similarity Index (ESI)**.

---

## 📊 Power BI Dashboard

| Page | Focus |
|---|---|
| Cover | Project identity & branding |
| Description | Mission statement |
| Overview | Discovery history, distances, single vs. multi-star systems |
| Habitability | Planet size, mass, density, orbital shape, rocky vs. gaseous |
| Star Systems | Host star temperature, mass, luminosity, correlations |
| Planet Explorer | Flux vs. temperature (Goldilocks Zone), ESI ranking, top Earth-like candidates |
| AI Model | Live habitability & similarity prediction for a user-entered planet |

Designed first in **Figma** (cosmic/nebula theme, indigo & violet palette), then built in Power BI with DAX measures connected to the Gold-layer star schema.

---

## 🤖 Machine Learning

Two models work together to answer two different questions:

| Model | Question | Algorithm |
|---|---|---|
| **Habitability Classifier** | Is this planet Habitable or Not? | RandomForestClassifier (SMOTE-balanced, regularized) |
| **Earth Similarity Regressor** | How Earth-like is it, on a 0–100 scale? | XGBRegressor (sample-weighted toward high-ESI planets) |

Trained on the **ExoHabX (NASA/HWC)** dataset — 5,326 planets, with habitability defined as ESI ≥ 80. Because only 25 planets (0.47%) meet that bar, the classifier uses a stratified split, SMOTE oversampling, and a custom decision threshold to make the most of a very rare positive class.

Both models are exposed two ways:
- **Live inside Power BI** — the "AI Model" page runs six input slicers through a Python visual
- **Streamlit app** (`app.py`) — a standalone interactive form with the same six inputs

---

## ⚙️ How to Run

### 1. Download the data
```bash
python kaggle.py
```

### 2. Run the pipeline notebooks in order
```
Copy_of_Data_Cleaning.ipynb   →  initial cleaning & physics-based imputation
Bronze_Layer.ipynb            →  raw ingestion
Silver_Layer.ipynb            →  cleaning pipeline (mirrors step 1)
Gold_Layer.ipynb               →  star-schema build
EDA_Habitability_Analysis.ipynb → ESI, habitability flags, dashboard-ready export
AiModel.ipynb                   →  trains & saves the ML models
```

### 3. Open the dashboard
Open `Exoplanet_Dashboard_final.pbix` in **Power BI Desktop**. The AI Model page's Python visual requires a local Python installation with the same packages used in `AiModel.ipynb` (scikit-learn, xgboost, joblib).

### 4. Run the Streamlit demo
```bash
pip install streamlit joblib xgboost pandas numpy
streamlit run app.py
```

---

## 📁 Key Files

| File | Purpose |
|---|---|
| `Bronze_Layer.ipynb` / `Silver_Layer.ipynb` / `Gold_Layer.ipynb` | Medallion pipeline notebooks |
| `EDA_Habitability_Analysis.ipynb` | Scientific feature engineering & dashboard-page design |
| `AiModel.ipynb` | ML model training |
| `habitability_classifier.pkl`, `feature_scaler.pkl`, `earth_similarity_regressor.json` | Trained model artifacts |
| `app.py` | Streamlit demo app |
| `Exoplanet_Dashboard_final.pbix` | Power BI dashboard |
| `Exoplanet_Habitability_Zone_Analysis_Documentation.docx` | Full graduation project documentation |

---

## 📝 Notes

- The NASA Exoplanet Archive updates daily — exact row counts differ slightly between pipeline runs captured at different times.
- The "Habitable" class is extremely rare in real exoplanet data, so classifier metrics on that class should be read alongside the (very small) support count rather than accuracy alone.

---

*Digital Egypt Pioneers Initiative — Data Analysis Track, 2025/2026*
