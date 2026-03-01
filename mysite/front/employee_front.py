import streamlit as st
import requests

def check_hr():
    st.title('HREmployee API')

    url = 'http://127.0.0.1:8000/en/HREmployee/'

    age = st.number_input('Age:', min_value=0, step=1)
    daily_rate = st.number_input('Daily Rate:', min_value=0, step=1)
    distance_from_home = st.number_input('Distance From Home:', min_value=0, step=1)
    education = st.number_input('Education:', min_value=0, step=1)
    environment_satisfaction = st.number_input('Environment Satisfaction:', min_value=0, step=1)
    hourly_rate = st.number_input('Hourly Rate:', min_value=0, step=1)
    job_involvement = st.number_input('Job Involvement:', min_value=0, step=1)
    job_level = st.number_input('Job Level:', min_value=0, step=1)
    job_satisfaction = st.number_input('Job Satisfaction:', min_value=0, step=1)
    monthly_income = st.number_input('Monthly Income:', min_value=0, step=1)
    monthly_rate = st.number_input('Monthly Rate:', min_value=0, step=1)
    num_companies_worked = st.number_input('Num Companies Worked:', min_value=0, step=1)
    percent_salary_hike = st.number_input('Percent Salary Hike:', min_value=0, step=1)
    performance_rating = st.number_input('Performance Rating:', min_value=0, step=1)
    relationship_satisfaction = st.number_input('Relationship Satisfaction:', min_value=0, step=1)
    stock_option_level = st.number_input('Stock Option Level:', min_value=0, step=1)
    total_working_years = st.number_input('Total Working Years:', min_value=0, step=1)
    training_times_last_year = st.number_input('Training Times Last Year:', min_value=0, step=1)
    work_life_balance = st.number_input('Work Life Balance:', min_value=0, step=1)
    years_at_company = st.number_input('Years At Company:', min_value=0, step=1)
    years_in_current_role = st.number_input('Years In Current Role:', min_value=0, step=1)
    years_since_last_promotion = st.number_input('Years Since Last Promotion:', min_value=0, step=1)
    years_with_curr_manager = st.number_input('Years With Curr Manager:', min_value=0, step=1)
    business_travel = st.selectbox('Business Travel:', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    department = st.selectbox('Department:', ['Sales', 'Research & Development', 'Human Resources'])
    education_field = st.selectbox('Education Field:', ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'])
    gender = st.selectbox('Gender:', ['Female', 'Male'])
    job_role = st.selectbox('Job Role:', ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director',
                                          'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
    marital_status = st.selectbox('Marital Status:', ['Single', 'Married', 'Divorced'])
    over_time = st.selectbox('Over Time:', ['Yes', 'No'])

    hr_data = {
        "Age": age,
        "DailyRate": daily_rate,
        "DistanceFromHome": distance_from_home,
        "Education": education,
        "EnvironmentSatisfaction": environment_satisfaction,
        "HourlyRate": hourly_rate,
        "JobInvolvement": job_involvement,
        "JobLevel": job_level,
        "JobSatisfaction": job_satisfaction,
        "MonthlyIncome": monthly_income,
        "MonthlyRate": monthly_rate,
        "NumCompaniesWorked": num_companies_worked,
        "PercentSalaryHike": percent_salary_hike,
        "PerformanceRating": performance_rating,
        "RelationshipSatisfaction": relationship_satisfaction,
        "StockOptionLevel": stock_option_level,
        "TotalWorkingYears": total_working_years,
        "TrainingTimesLastYear": training_times_last_year,
        "WorkLifeBalance": work_life_balance,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": years_in_current_role,
        "YearsSinceLastPromotion": years_since_last_promotion,
        "YearsWithCurrManager": years_with_curr_manager,
        "BusinessTravel": business_travel,
        "Department": department,
        "EducationField": education_field,
        "Gender": gender,
        "JobRole": job_role,
        "MaritalStatus": marital_status,
        "OverTime": over_time
    }

    if st.button('Текшеруу'):
        try:
            answer = requests.post(url, json=hr_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Ката: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('not connected bruh :(')