# Importar bibliotecas.
import streamlit as st
import pickle
import pandas as pd

job = education = None

# Cargar el modelo y el escalador desde archivos
with open('S9/bank_model.pkl', 'rb') as model_file:
    model = pickle.load (model_file)

with open('S9/bank_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load (scaler_file)

# Título de la aplicación
st.title ('Predicción Sobre la Contratación de un Depósito a Plazo Fijo.')
st.header ('(Regresión Logística)')

# #   Column               Non-Null Count  Dtype
# ---  ------               --------------  -----
#  0   age                  7813 non-null   float64
#  1   balance              7813 non-null   float64
#  2   campaign             7813 non-null   float64
#  3   pdays                7813 non-null   float64
#  4   contact              7813 non-null   int64
#  5   default              7813 non-null   int64
#  6   housing              7813 non-null   int64
#  7   loan                 7813 non-null   int64
#  8   poutcome             7813 non-null   int64
#  9   job_non-qualified    7813 non-null   bool
#  10  job_qualified        7813 non-null   bool
#  11  job_semi-qualified   7813 non-null   bool
#  12  job_freelance        7813 non-null   bool
#  13  job_other            7813 non-null   bool
#  14  education_primary    7813 non-null   bool
#  15  education_secondary  7813 non-null   bool
#  16  education_tertiary   7813 non-null   bool
#  17  education_unknown    7813 non-null   bool

#  0   age                  7813 non-null   float64
#  1   balance              7813 non-null   float64
#  2   campaign             7813 non-null   float64
#  3   pdays                7813 non-null   float64
#  4   contact              7813 non-null   int64
#  5   default              7813 non-null   int64
#  6   housing              7813 non-null   int64
#  7   loan                 7813 non-null   int64
#  8   poutcome             7813 non-null   int64

#  9   job_non-qualified    7813 non-null   bool
#  10  job_qualified        7813 non-null   bool
#  11  job_semi-qualified   7813 non-null   bool
#  12  job_freelance        7813 non-null   bool
#  13  job_other            7813 non-null   bool
job = st.selectbox ("Job type: ", ['non-qualified', 'qualified', 'semi-qualified', 'freelance', 'other'])

match job:
    case 'non-qualified':
        st.write ("Job is non-qualified.")
    case 'qualified':
        st.write ("Job is qualified.")
    case 'semi-qualified':
        st.write ("Job is semi-qualified.")
    case 'freelance':
        st.write ("Job is freelance.")
    case 'other':
        st.write ("Job is other.")

#  14  education_primary    7813 non-null   bool
#  15  education_secondary  7813 non-null   bool
#  16  education_tertiary   7813 non-null   bool
#  17  education_unknown    7813 non-null   bool
education = st.selectbox ("Education: ", ['primary', 'secondary', 'tertiary', 'unknown'])

match education:
    case 'primary':
        st.write ("Education is primary.")
    case 'secondary':
        st.write ("Education is secondary.")
    case 'tertiary':
        st.write ("Education is tertiary.")
    case 'unknown':
        st.write ("Education is unknown.")

