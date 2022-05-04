from django import forms
from django.contrib.auth.models import User
from .models import student_report_problem, warden_report_problem


# student problem report form
class studentReportProblemForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=User.objects.all(),
                                    widget=forms.HiddenInput())

    class Meta:
        model = student_report_problem
        fields = ('student', 'problem_type', 'image', 'description')


# warden problem report form
class wardenReportProblemForm(forms.ModelForm):
    warden = forms.ModelChoiceField(queryset=User.objects.all(),
                                    widget=forms.HiddenInput())

    class Meta:
        model = warden_report_problem
        fields = ('warden', 'problem_title', 'details')


    # student problem report form
class sendFeedbackForm(forms.ModelForm):

    class Meta:
        model = student_report_problem
        fields = ('feedback',)
