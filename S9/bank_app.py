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

# Crear un DataFrame con las entradas
user_data = pd.DataFrame({
    'age'                : [age],
    'balance'            : [balance],
    'campaign'           : [campaign],
    'pdays'              : [pdays],
    'contact'            : [contact],
    'default'            : [default],
    'housing'            : [housing],
    'loan'               : [loan],
    'poutcome'           : [poutcome],
    'job_non-qualified'  : [False],
    'job_qualified'      : [False],
    'job_semi-qualified' : [False],
    'job_freelance'      : [False],
    'job_other'          : [False],
    'education_primary'  : [False],
    'education_secondary': [False],
    'education_tertiary' : [False],
    'education_unknown'  : [False]
})

# Codificación de variables categóricas.

# Columnas binarias.
cols = ['contact', 'poutcome', 'housing', 'loan', 'default']

for c in cols:
    user_data [c] = encoder.fit_transform (user_data [c])

# Columnas categóricas.
match job:
    case 'non-qualified':
        user_data ['job_non-qualified'] = True,

    case 'qualified':
        user_data ['job_qualified'] = True,

    case 'semi-qualified':
        user_data ['job_semi-qualified'] = True,

    case 'freelance':
        user_data ['job_freelance'] = True,

    case 'other':
        user_data ['job_other'] = True,

match education:
    case 'primary':
        user_data ['education_primary'] = True,

    case 'secondary':
        user_data ['education_secondary'] = True,

    case 'tertiary':
        user_data ['education_tertiary'] = True,

    case 'unknown':
        user_data ['education_unknown'] = True,

cols = ['age', 'balance', 'campaign', 'pdays']

# Para los valores de entrenamiento.
for c in cols:
    user_data [c] = user_data [c].astype ('float64')

# Aplicamos "fit_transform" a los valores de entrada del usuario.
user_data.loc [:,cols] = scaler.fit_transform (user_data.loc [:,cols])

st.write ('user_data.info (): ', user_data.info ())
st.write ('user_data: ', user_data)

# Realizar la predicción con su probabilidad.
probabilidad = model.predict_proba (user_data)
prediction = model.predict (user_data)

# Mostrar la predicción.
st.write(f'Probabilidad: ', probabilidad [1])
st.write(f'Predicción: ', prediction)

