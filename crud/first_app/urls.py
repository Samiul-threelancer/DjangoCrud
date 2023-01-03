from django.urls import path
from .views import index, studet_form

app_name = 'first_app'

urlpatterns = [
    path('', index, name='index'),
    path('student_form', studet_form, name='student_form'),
    ]
