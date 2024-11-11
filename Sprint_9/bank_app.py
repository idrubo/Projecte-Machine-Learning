# Importar bibliotecas.
import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo y el escalador desde archivos
with open('Sprint_9/bank_model.pkl', 'rb') as model_file:
    model = pickle.load (model_file)

with open('Sprint_9/bank_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load (scaler_file)

# Título de la aplicación
st.title ('Predicción Sobre la Contratación de un Depósito a Plazo Fijo. (Regresión Logística)')
st.title ('(Regresión Logística)')

