import streamlit as st
import pandas as pd
import numpy as np
import joblib
import xgboost as xgb  


st.set_page_config(page_title="Exoplanet Analysis", page_icon="🪐", layout="centered")

# 1. تحميل النماذج والـ Scaler
@st.cache_resource 
def load_models():
    # تحميل الـ Classifier والـ Scaler عادي بـ joblib
    clf = joblib.load('habitability_classifier.pkl')
    scaler = joblib.load('feature_scaler.pkl')
    
    # تحميل الـ Regressor (XGBoost) بالطريقة المخصصة ليه
    reg = xgb.XGBRegressor()
    reg.load_model('earth_similarity_regressor.json')
    
    return clf, reg, scaler

clf_model, reg_model, scaler = load_models()


st.title("🪐 Exoplanet Habitability & Similarity Model")
st.markdown("Enter the physical properties of the Exoplanet: ")
st.divider()

col1, col2 = st.columns(2)

with col1:
    radius = st.number_input("Planet Radius (Earth Radii)", min_value=0.1, value=1.0, step=0.1)
    mass = st.number_input("Planet Mass (Earth Masses)", min_value=0.1, value=1.0, step=0.1)
    flux = st.number_input("Stellar Flux", min_value=0.01, value=1.0, step=0.1)

with col2:
    temp = st.number_input("Equilibrium Temperature (K)", min_value=50.0, value=255.0, step=10.0)
    semi_major = st.number_input("Semi-major Axis (AU)", min_value=0.01, value=1.0, step=0.1)
    eccentricity = st.number_input("Eccentricity", min_value=0.0, max_value=0.99, value=0.01, step=0.01)


if st.button("🚀 Analyze Planet", use_container_width=True):
    input_data = pd.DataFrame({
        'radius': [radius],
        'mass': [mass],
        'flux': [flux],
        'temp': [temp],
        'semi_major': [semi_major],
        'eccentricity': [eccentricity]
    })

    
    input_scaled = scaler.transform(input_data)


    is_habitable = clf_model.predict(input_scaled)[0]
    confidence = clf_model.predict_proba(input_scaled)[0].max() * 100
    

    esi_score = reg_model.predict(input_scaled)[0]
    esi_score = max(0, min(100, esi_score)) 


    st.divider()
    st.subheader("📊 Analysis Results:")
    
    # First Model:
    if is_habitable == 1:
        st.success(f"✅ **Habitability Classification:** Habitable (Confidence: {confidence:.2f}%)")
    else:
        st.error(f"❌ **Habitability Classification:** Not Habitable (Confidence: {confidence:.2f}%)")
        
    # Second Model: 
    st.info(f"🌍 **Earth Similarity Index (ESI):** {esi_score:.2f} / 100")
    
    # ESI Score:
    st.progress(int(esi_score) / 100)

