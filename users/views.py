from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegisterForm, WardenRegisterForm
from django.contrib.auth.models import User
from django.conf import settings
from django.template.loader import render_to_string
from hostel.models import hostel
from problems_report.models import warden_report_problem, student_report_problem

# Create your views here.
@login_required
def homepage(request):
    students_count = User.objects.filter(is_staff=0, is_superuser=0).count()
    staff_count = User.objects.filter(is_staff=1).count()
    hostels_count = hostel.objects.count()
    warden_report_count = warden_report_problem.objects.count()
    block_students_report_count = student_report_problem.objects.count()
    students_report_count = student_report_problem.objects.filter(id=request.user.id).count()
    only_warden_report_count = warden_report_problem.objects.filter(id=request.user.id).count()

    context = {
        'students_count' : students_count,
        'hostels_count' : hostels_count,
        'staff_count' : staff_count,
        'warden_report_count' : warden_report_count,
        'students_report_count' : students_report_count,
        'only_warden_report_count' :  only_warden_report_count,
        'block_students_report_count' : block_students_report_count,
    }

    return render(request, 'users/dashboard.html', context)


@login_required
def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulation! You have registered successfully Now click link below to login")
            return redirect('register')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def add_student(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New Student has been added successfully")
            return redirect('add_student')
    else:
        form = UserRegisterForm()

    return render(request, 'users/add_student.html', {'form': form})


@login_required
def add_warden(request):
    if request.user.is_superuser:
        form = WardenRegisterForm
        if request.method == "POST":
            form = WardenRegisterForm(request.POST)
            
            if form.is_valid():
                form.save()
                
                messages.success(request, "New Warden has been added successfully")
                return redirect('add_warden')
        else:
            form = WardenRegisterForm()

    return render(request, 'users/add_warden.html', {'form': form})


@login_required
def users_view(request):

    view_lists = User.objects.all()


    context = {
        'User': view_lists,
    }

    return render(request, 'users/students_list.html', context)


@login_required
def view_wardens(request):

    view_warden_list = User.objects.filter(is_staff=1, is_superuser=0)

    context = {

        'User': view_warden_list,
    }
    return render(request, 'users/wardens_list.html', context)


@login_required
def view_students(request):

    view_student_list = User.objects.filter(is_staff=0, is_superuser=0)

    context = {

        'User': view_student_list,
    }
    return render(request, 'users/students_list.html', context)


@login_required
def update_student(request, student_id):
    user_view = User.objects.get(pk = student_id)
    form = UserRegisterForm(request.POST or None, instance=user_view)
    if form.is_valid():
        form.save()
        return redirect('students-list')

    return render(request, 'users/update_student.html', {'form': form})


@login_required
def delete_student(request, student_id):
    user_del = User.objects.get(pk=student_id)
    user_del.delete()
    return redirect('students-list')


@login_required
def update_warden(request, warden_id):
    user_view = User.objects.get(pk = warden_id)
    form = UserRegisterForm(request.POST or None, instance=user_view)
    if form.is_valid():
        form.save()
        return redirect('warden-list')

    return render(request, 'users/update_warden.html', {'form': form})


@login_required
def delete_warden(request, warden_id):
    user_del = User.objects.get(pk=warden_id)
    user_del.delete()
    return redirect('warden-list')