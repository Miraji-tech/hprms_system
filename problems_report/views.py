from unicodedata import name
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import F
from hostel.models import allocate_block, allocate_room, hostel, hostel_block, room
from .forms import studentReportProblemForm, wardenReportProblemForm, sendFeedbackForm
from .models import student_report_problem, warden_report_problem
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

@login_required
def student_reports(request):
 
    form = studentReportProblemForm(request.POST, request.FILES)

    # hostel__ = allocate_room.objects.filter(hostel_name_id = F('id'))
    # block__ = allocate_room.objects.filter(block_name_id = F('id'))
    # room__ = allocate_room.objects.filter(room_id = F('id'),block_name_id = F('id'), hostel_name_id = F('id'))
    allocateroom__ = allocate_room.objects.filter(student_id = request.user.id)

    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.student = request.user
        instance.allocateroom = instance.allocateroom
        # instance.hostel = instance.hostel
        # instance.block_name = instance.block_name
        # instance.room_name = instance.room_name
        instance.save()
        messages.success(request, "Your problem has been reported successfully")

        return redirect('student_report_problem')

    context = {
        'form': form,
        'allocate_room' : allocateroom__,
        }

    return render(request, 'problems_report/student/student_problem_report_form.html', context)


@login_required
def warden_reports(request):

    # block__ = allocate_block.objects.filter(block_name_id = F('id'), hostel_name_id = F('id'))
    form = wardenReportProblemForm(request.POST)
    
    allocateblock__ = allocate_block.objects.filter(warden_id = request.user.id)

    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.warden = request.user
        instance.allocateblock = instance.allocateblock
        # instance.hostel = instance.hostel
        # instance.block_name = instance.block_name
        instance.save()
        messages.success(request, "Your problem has been reported successfully")

        return redirect('warden_report_problem')

    context = {
        'form': form,
        'allocate_block':allocateblock__,
    }

    return render(request, 'problems_report/warden/warden_problem_report_form.html', context)


# A problem reported by a specific student function
def view_student_reports(request):

    spr = student_report_problem.objects.filter(student_id=request.user.id).select_related('allocateroom')

    context = {

        'student_report_problem': spr,

    }

    return render(request, 'problems_report/student/problem_reported_by_student.html', context)


# All problems reported by all warden function
def warden_reported_problem(request):
    
    wardens = warden_report_problem.objects.all().select_related('allocateblock')

    context = {
        'warden_report_problem': wardens,
    }
    return render(request, 'problems_report/usab_manager/warden_reports.html', context)


# All problems reported by all studentsb
def view_reported_problem(request):

    # student_in_block = allocate_room.objects.get(student_id=student_report_problem.student_id, block_name = allocate_block.block_name)
    reports = student_report_problem.objects.all().select_related('allocateroom')

    # student_id=student_in_block

    context = {

        'student_report_problem': reports,

    }

    return render(request, 'problems_report/warden/reported_problem_by_students.html', context)


# A problems reported by a single warden function
def view_warden_report(request):

    wpr = warden_report_problem.objects.filter(warden_id = request.user.id).select_related('allocateblock')

    context = {
        'warden_report_problem': wpr,
    }

    return render(request, 'problems_report/warden/problem_reported_by_warden.html', context)


# Data feedback
def problem_feedback_view(request, problem_id):

    feedback_form_ = student_report_problem.objects.get(pk = problem_id)
    
    if request.method == 'POST':
        form = sendFeedbackForm(request.POST, instance = feedback_form_)
        if form.is_valid:
            form.save
    else:
        return render(request, 'problems_report/warden/reported_problem_by_students.html', context)
    context = {

        'form': form,
        
    }

    return render(request, 'problems_report/warden/reported_problem_by_students.html', context)


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

    reports = student_report_problem.objects.all().select_related('allocateroom')

    context = {

        'student_report_problem': reports,

    }

    return render(request, 'problems_report/usab_manager/students_reports.html', context)


@login_required
def problem_approve(request, problem_id):
    srp = student_report_problem.objects.get(id=problem_id)
    srp.feedback = 1
    srp.save()
    return HttpResponseRedirect(reverse("view_students_reported_problems"))


@login_required
def problem_decline(request, problem_id):
    srp_decline = student_report_problem.objects.get(id=problem_id)
    srp_decline.feedback = 2
    srp_decline.save()
    return HttpResponseRedirect(reverse("view_students_reported_problems"))


@login_required
def wd_problem_approve(request, problem_id):
    wrp = warden_report_problem.objects.get(id=problem_id)
    wrp.feedback = 1
    wrp.save()
    return HttpResponseRedirect(reverse("wardens_report"))


@login_required
def wd_problem_decline(request, problem_id):
    wrp_decline = warden_report_problem.objects.get(id=problem_id)
    wrp_decline.feedback = 2
    wrp_decline.save()
    return HttpResponseRedirect(reverse("wardens_report"))