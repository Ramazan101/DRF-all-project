import streamlit as st
import requests
def diabetes_chek():

    api_url = 'http://127.0.0.1:8000/en/Diabetes/'

    st.title('Diabetes API')

    Pregnancies = st.number_input('Кош бойлуулук', min_value=0, max_value=100, value=22, step=1)
    Glucose = st.number_input('Глюкоза', min_value=0, max_value=199, value=22, step=1)
    BloodPressure = st.number_input('Кан басымы', min_value=0, max_value=122, value=22, step=1)
    SkinThickness = st.number_input( 'Теринин калыңдыгы', min_value=0, max_value=99, value=0, step=1)
    Insulin = st.number_input('Инсулин', min_value=14.0, max_value=846.0, value=22.0, step=0.1)
    BMI = st.number_input('BMI', min_value=0.0, max_value=68.0, value=22.0, step=0.001)
    DiabetesPedigreeFunction = st.number_input('Диабеттин асыл тукум функциясы', min_value=0.00, max_value=2.00, value=0.0, step=0.1)
    Age = st.number_input('Жашы', min_value=21, max_value=81, value=22, step=1)


    diabetes_data = {
      "Pregnancies": Pregnancies,
      "Glucose": Glucose,
      "BloodPressure": BloodPressure,
      "SkinThickness": SkinThickness,
      "Insulin": Insulin,
      "BMI": BMI,
      "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
      "Age": Age
    }

    if st.button('Текшеруу'):
        try:
            regular = requests.post(api_url, json=diabetes_data, timeout=10)
            if regular.status_code == 200:
                result = regular.json()
                st.json(result)
            else:
                st.error(f'Жанылыштык: {regular.status_code}')
        except requests.exceptions.RequestException:
            st.error('API ге кошула албадыныз')