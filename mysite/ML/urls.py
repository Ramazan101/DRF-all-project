from django.urls import path
from .views import StudentPredict, Titanic, House, Bank, Diabetes, Avocado, Mushroom, Telecom

urlpatterns = [
    path('Student/',StudentPredict.as_view(), name='student'),
    path('Titanic/',Titanic.as_view(), name='titanic'),
    path('House/',House.as_view(), name='house'),
    path('Bank/',Bank.as_view(), name='bank'),
    path('Diabetes/',Diabetes.as_view(), name='diabetes'),
    path('Avocado/',Avocado.as_view(), name='avocado'),
    path('Mushroom/',Mushroom.as_view(), name='mushroom'),
    path('Telecom/',Telecom.as_view(), name='telecom'),
]