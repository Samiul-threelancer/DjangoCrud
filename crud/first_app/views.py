from django.shortcuts import render
from .form import StudentForm

def index(request):
    diction = {'title':'index'}
    return render(request, 'first_app/index.html', context=diction)


def studet_form(request):
    form = StudentForm()
    diction = {'title': 'student_form', 'student_form':form}
    return render(request, 'first_app/student_form.html', context=diction)