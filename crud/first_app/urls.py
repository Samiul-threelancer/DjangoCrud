from django.urls import path
from .views import index, studet_form, StudentInfo, StudentUpdate

app_name = 'first_app'

urlpatterns = [
    path('', index, name='index'),
    path('student_form', studet_form, name='student_form'),
    path('student_info/<int:student_id>/', StudentInfo, name='student_info'),
    path('student_update/<int:student_id>', StudentUpdate, name='student_update'),
    ]
