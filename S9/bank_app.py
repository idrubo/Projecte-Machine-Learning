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
st.write (f'job is ', job)

#  14  education_primary
#  15  education_secondary
#  16  education_tertiary
#  17  education_unknown
education = st.selectbox ("ecucation: ", ['primary', 'secondary', 'tertiary', 'unknown'])
st.write (f'education is ', education)

#  #   Column               Non-Null Count  Dtype
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

# Crear un DataFrame con las entradas
user_data = pd.DataFrame({
    'age'      : [age],
    'balance'  : [balance],
    'campaign' : [campaign],
    'pdays'    : [pdays],
    'contact'  : [contact],
    'default'  : [default],
    'housing'  : [housing],
    'loan'     : [loan],
    'poutcome' : [poutcome],
    'job'      : [job],
    'education': [education]
})

# Codificación de variables categóricas.

# Columnas binarias.
cols = ['contact', 'poutcome', 'housing', 'loan', 'default']

for c in cols:
    user_data [c] = encoder.fit_transform (user_data [c])

# Columnas categóricas.
user_data = pd.get_dummies (user_data, columns = ['job', 'education'])

st.write (user_data.info ())
st.write (user_data)

