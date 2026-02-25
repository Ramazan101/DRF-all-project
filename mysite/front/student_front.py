import requests
import streamlit as st

def student():
    api_url = 'http://127.0.0.1:8000/en/Student/'
    st.title('Student API')

    gender = st.selectbox('Gender: ', ['male', 'female'])
    race_ethnicity = st.selectbox('Group: ', ['A', 'B', 'C', 'D', 'E'])
    parental_level_of_education = st.selectbox('Parental level education: ',
                                               ["associate's degree", "bachelor's degree", "high school",
                                                "master's degree", "some college", "some high school"])
    lunch = st.selectbox('Lunch: ', ['free/reduced', 'standard'])
    test_preparation = st.selectbox('Test preparation course: ', ['None', 'Completed'])
    reading_score = st.number_input('Reading Score: ', min_value=0, max_value=100, step=1)
    math_score = st.number_input('Math Score: ', min_value=0, max_value=100, step=1)

    student_performance = {
        "gender": gender,
        "race_ethnicity": race_ethnicity,
        "parental_level_of_education": parental_level_of_education,
        "lunch": lunch,
        "test_preparation_course": test_preparation,
        "reading_score": reading_score,
        "math_score": math_score
    }

    if st.button('Текшеруу'):
        try:
            answer = requests.post(api_url, json=student_performance, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f"Жыйынтык: {result.get('Predict')}")
            else:
                st.error(f'Ката: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error(f'Сиз API ге кошула албадыныз')