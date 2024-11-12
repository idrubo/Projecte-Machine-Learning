# Importar bibliotecas.
import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo y el escalador desde archivos
with open('S9/bank_model.pkl', 'rb') as model_file:
    model = pickle.load (model_file)

with open('S9/bank_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load (scaler_file)

# Título de la aplicación
st.title ('Predicción Sobre la Contratación de un Depósito a Plazo Fijo.')
st.header ('(Regresión Logística)')

# Selection box

# first argument takes the title of the selectionbox, second argument takes options
job = st.selectbox("Job: ", ['admin.', 'engineer', 'manager'])

# print the selected hobby
st.write("Your job is: ", job)

