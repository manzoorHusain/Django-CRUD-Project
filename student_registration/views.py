from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.


def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, "student_registration/student_list.html", context)


def student_form(request, id=0):
    if request.method == "GET":
        if id == 0: # if insertion
            form = StudentForm()
        else: # this is update
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, "student_registration/student_form.html", {'form': form})
    else:
        if id == 0: # insert
            form = StudentForm(request.POST)
        else: # update
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST,instance= student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')
        # return redirect('/student/list')
    # return render(request, "student_registration/student_form.html")



def student_delete(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')