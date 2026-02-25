import streamlit as st
import requests
def bank_chek():

    st.title('Bank API')

    api_url = 'http://127.0.0.1:8000/en/Bank/'

    person_age = st.number_input('Age: ', min_value=18, max_value=100, value=18, step=1)
    person_gender = st.selectbox('Gender: ', ['male', 'female'])
    education = st.selectbox('Education: ', ['Bachelor', 'Doctorate', 'High School', 'Master', 'Associate'])
    person_income = st.number_input('Income: ', min_value=0)
    person_exp = st.number_input('Person Emp Exp: ', min_value=0, step=1)
    ownership = st.selectbox('Ownership: ', ['OTHER', 'OWN', 'RENT', 'MORTGAGE'])
    loan_amnt = st.number_input('Amnt: ', min_value=0)
    loan_intent = st.selectbox('Intent: ',
                               ['EDUCATION', 'HOMEIMPROVEMENT' 'MEDICAL', 'PERSONAL', 'VENTURE', 'DEBTCONSOLIDATION'])
    lona_int_rate = st.number_input('Rating: ', min_value=0.0)
    percent_income = st.number_input('Percent Income: ', min_value=0.0)
    person_cred_hist_length = st.number_input('Cred hist length: ', min_value=0)
    credit_score = st.number_input('Credit Score: ', min_value=0)
    defaults_on_file = st.selectbox('Loan defaults on file: ', ['Yes', 'No'])

    bank_data = {
        "person_age": person_age,
        "person_gender": person_gender,
        "person_education": education,
        "person_income": person_income,
        "person_emp_exp": person_exp,
        "person_home_ownership": ownership,
        "loan_amnt": loan_amnt,
        "loan_intent": loan_intent,
        "loan_int_rate": lona_int_rate,
        "loan_percent_income": percent_income,
        "cb_person_cred_hist_length": person_cred_hist_length,
        "credit_score": credit_score,
        "previous_loan_defaults_on_file": defaults_on_file
    }

    if st.button('Текшеруу'):
        try:
            answer = requests.post(api_url, json=bank_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Ката: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error(f'Сиз API ге кошула албадыныз(')