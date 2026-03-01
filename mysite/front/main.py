import sys
import streamlit as st
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from mysite.front.student_front import student
from mysite.front.titanic_front import check_titanic
from mysite.front.house_front import house_chek
from mysite.front.bank_front import bank_chek
from mysite.front.diabetes_front import diabetes_chek
from mysite.front.avocado_front import avocado_chek
from mysite.front.mushrooms_front import mushrooms_chek
from mysite.front.telecom_front import telecom
from mysite.front.employee_front import check_hr


with st.sidebar:
    name = st.radio(label='Models: ', options=['Info', 'Student', 'Titanic', 'House', 'Bank',
                                                'Diabetes', 'Avocado', 'Mushroom', 'Telecom',
                                               'HREmployee'])

if name == 'Info':
    st.title('Welcome')
    st.write('Student — успеваемости студентов')
    st.write('Titanic — выживаемости на Титанике')
    st.write('House — стоимости недвижимостей')
    st.write('Bank — банковская аналитика')
    st.write('Diabetes — диагностика диабета')
    st.write('Avocado — предсказание цен на авокадо')
    st.write('Mushroom — классификация грибов')
    st.write('Telecom — отток клиентов телекома')

elif name == 'Student':
    student()
elif name == 'Titanic':
    check_titanic()
elif name == 'House':
    house_chek()
elif name == 'Bank':
    bank_chek()
elif name == 'Diabetes':
    diabetes_chek()
elif name == 'Avocado':
    avocado_chek()
elif name == 'Mushroom':
    mushrooms_chek()
elif name == 'Telecom':
    telecom()
elif name == 'HREmployee':
    check_hr()