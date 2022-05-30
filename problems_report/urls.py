"""auth_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('student_report_problem/', views.student_reports, name='student_report_problem'),
    path('student_reported_problems/', views.view_student_reports, name='student_reported_problems'),
    path('warden_report_problem/', views.warden_reports, name='warden_report_problem'),
    path('view_students_reported_problems/', views.view_reported_problem, name='view_students_reported_problems'),
    path('view_warden_report/', views.view_warden_report, name='view_warden_report'),
    path('wardens_report/', views.warden_reported_problem, name='wardens_report'),
    path('problem_feedback/', views.problem_feedback_view, name='problem_feedback'),
    path('student_feedback_Form/<str:problem_id>', views.student_problem_feedback_form, name='student_feedback_Form'),
    path('feedback_Form/<str:problem_id>', views.warden_problem_feedback_form, name='feedback_Form'),
    path('view_students_problems/', views.usab_manager_view_students_problem, name='view_students_problems'),
    path('feedback/<str:problem_id>', views.problem_approve, name='problem-solved'),
    path('feedback-goahead/<str:problem_id>', views.problem_decline, name='problem-goahead')
]
