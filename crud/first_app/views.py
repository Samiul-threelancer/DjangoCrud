from django.shortcuts import render
from .form import StudentForm
from .models import Student

def index(request):
    student_list = Student.objects.order_by('first_name')
    diction = {'title': "index", 'student_list': student_list}
    return render(request, 'first_app/index.html', context=diction)


def studet_form(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title': 'student_form', 'student_form':form}
    return render(request, 'first_app/student_form.html', context=diction)



def StudentInfo(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    diction = {'student_info':student_info}
    return render(request, 'first_app/student_info.html', context=diction)


def StudentUpdate(request):
    diction = {}
    return render(request, 'first_app/student_update.html', context=diction)