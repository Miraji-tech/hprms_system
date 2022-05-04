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
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', views.user_register, name='register'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_warden/', views.add_warden, name='add_warden'),
    path('users-list/', views.users_view, name='users-list'),
    path('update-student/<student_id>', views.update_student, name='update-student'),
    path('delete-student/<student_id>', views.delete_student, name='delete-student'),
    path('warden-list/', views.view_wardens, name='warden-list'),
    path('students-list/', views.view_students, name='students-list'),
    path('update-warden/<warden_id>', views.update_warden, name='update-warden'),
    path('delete-warden/<warden_id>', views.delete_warden, name='delete-warden'),
    path('dashboard/', views.homepage, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='users/password_change.html',
        success_url=reverse_lazy('password_change_done')), name='change-password'),
    path('change password/done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'), name='password_change_done'),
    path('password reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html'),
         name='password_reset'),
    path('password reset done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path(r'<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}/$',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password reset complete/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete')
]
