import streamlit as st
import requests


def telecom():
    st.title('Telecom API')

    api_url = 'http://127.0.0.1:8000/en/Telecom/'


    gender = st.selectbox('Gender:', ['Female', 'Male'])
    senior_citizen = st.number_input('Senior Citizen: ', min_value=0, step=1)
    partner = st.selectbox('Partner:', ['Yes', 'No'])
    dependents = st.selectbox('Dependents:', ['No', 'Yes'])
    tenure = st.number_input('Tenure:', min_value=0, step=1)
    phone_service = st.selectbox('Phone Service:', ['No', 'Yes'])
    multiple_lines = st.selectbox('Multiple Lines:', ['No phone service', 'No', 'Yes'])
    internet_service = st.selectbox('Internet Service:', ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox('Online Security:', ['No', 'Yes', 'No internet service'])
    online_backup = st.selectbox('Online Backup:', ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox('Device Protection:', ['No', 'Yes', 'No internet service'])
    tech_support = st.selectbox('Tech Support:', ['No', 'Yes', 'No internet service'])
    streaming_tv = st.selectbox('Streaming TV:', ['No', 'Yes', 'No internet service'])
    streaming_movies = st.selectbox('Streaming Movies:', ['No', 'Yes', 'No internet service'])
    contract = st.selectbox('Contract:', ['Month-to-month', 'One year', 'Two year'])
    paperless_billing = st.selectbox('Paperless Billing:', ['Yes', 'No'])
    payment_method = st.selectbox('Payment Method:', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    monthly_charges = st.number_input('Monthly Charges:', min_value=0.0, step=1.0)
    total_charges = st.number_input('Total Charges:', min_value=0.0, step=1.0)

    telecom_data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    if st.button('Текшеруу'):
        try:
            answer = requests.post(api_url, json=telecom_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Ката: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Сиз API ге кошула албадыныз (')