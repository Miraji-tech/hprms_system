from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import studentReportProblemForm, wardenReportProblemForm, sendFeedbackForm
from .models import student_report_problem, warden_report_problem
from django.urls import reverse

# Create your views here.

@login_required
def student_reports(request):
    form = studentReportProblemForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.student = request.user
        instance.save()
        messages.success(request, "Your problem has been reported successfully")

        return redirect('student_report_problem')

    return render(request, 'problems_report/student/student_problem_report_form.html', {'form': form})


def warden_reports(request):
    form = wardenReportProblemForm(request.POST)
    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.warden = request.user
        instance.save()
        messages.success(request, "Your problem has been reported successfully")

        return redirect('warden_report_problem')

    return render(request, 'problems_report/warden/warden_problem_report_form.html', {'form': form})


# A problem reported by a specific student  function
def view_student_reports(request):

    spr = student_report_problem.objects.filter(student_id=request.user.id)

    context = {

        'student_report_problem': spr,

    }

    return render(request, 'problems_report/student/problem_reported_by_student.html', context)


# All problems reported by all warden function
def warden_reported_problem(request):
    
    wardens = warden_report_problem.objects.all()

    context = {
        'warden_report_problem': wardens,
    }
    return render(request, 'problems_report/usab_manager/warden_reports.html', context)


# All problems reported by all students
def view_reported_problem(request):

    reports = student_report_problem.objects.all()

    context = {

        'student_report_problem': reports,

    }

    return render(request, 'problems_report/warden/reported_problem_by_students.html', context)


# A problems reported by a single warden function
def view_warden_report(request):

    wpr = warden_report_problem.objects.filter(warden_id = request.user.id)

    context = {
        'warden_report_problem': wpr,
    }

    return render(request, 'problems_report/warden/problem_reported_by_warden.html', context)


# Data feedback
def problem_feedback_view(request):

    form = sendFeedbackForm(request.POST)
    if form.is_valid:
        form.save

    context = {

        'form': form,
        
    }

    return render(request, 'problems_report/warden/reported_problem_by_students.html')


@login_required
def student_problem_feedback_form(request, problem_id):

    feedback_form = student_report_problem.objects.get(pk = problem_id)

    context = {

        'student_report_problem': feedback_form,
    }

    return render(request, 'problems_report/warden/feedback_form.html', context)


@login_required
def warden_problem_feedback_form(request, problem_id):

    warden_feedback_form = warden_report_problem.objects.get(pk = problem_id)

    context = {

        'warden_report_problem': warden_feedback_form,
    }

    return render(request, 'problems_report/usab_manager/feedback_form.html', context)


@login_required
def usab_manager_view_students_problem(request):

    reports = student_report_problem.objects.all()

    context = {

        'student_report_problem': reports,

    }

    return render(request, 'problems_report/usab_manager/students_reports.html', context)