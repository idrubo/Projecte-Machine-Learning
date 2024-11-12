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

with open('S9/bank_encoder.pkl', 'rb') as encoder_file:
    encoder = pickle.load (encoder_file)

# Título de la aplicación
st.title ('Predicción Sobre la Contratación de un Depósito a Plazo Fijo.')
st.header ('(Regresión Logística)')

#  0   age
age = st.number_input ('age', min_value = 0)
st.write (f'age is ', age)

#  1   balance
balance = st.number_input ('balance', value = 0, step = 10)
st.write (f'balance is ', balance)

#  2   campaign
campaign = st.number_input ('campaign', min_value = 0)
st.write (f'campaign is ', campaign)

#  3   pdays
pdays = st.number_input ('pdays (días)', min_value = -1)
st.write (f'pdays is ', pdays)

#  4   contact
contact = st.selectbox ("contact: ", ['cellular', 'telephone', 'unknown'])
st.write (f'contact is ', contact)

#  5   default
default = st.selectbox ("default: ", ['no', 'yes'])
st.write (f'default is ', default)

#  6   housing
housing = st.selectbox ("housing: ", ['no', 'yes'])
st.write (f'housing is ', housing)

#  7   loan
loan = st.selectbox ("loan: ", ['no', 'yes'])
st.write (f'loan is ', loan)

#  8   poutcome
poutcome = st.selectbox ("poutcome: ", ['failure', 'other', 'success', 'unknown'])
st.write (f'poutcome is ', poutcome)

#  9   job_non-qualified
#  10  job_qualified
#  11  job_semi-qualified
#  12  job_freelance
#  13  job_other
job = st.selectbox ("job: ", ['non-qualified', 'qualified', 'semi-qualified', 'freelance', 'other'])

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

#  14  education_primary
#  15  education_secondary
#  16  education_tertiary
#  17  education_unknown
education = st.selectbox ("ecucation: ", ['primary', 'secondary', 'tertiary', 'unknown'])

match education:
    case 'primary':
        st.write ("Education is primary.")
    case 'secondary':
        st.write ("Education is secondary.")
    case 'tertiary':
        st.write ("Education is tertiary.")
    case 'unknown':
        st.write ("Education is unknown.")

