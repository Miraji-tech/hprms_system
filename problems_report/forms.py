from django import forms
from django.contrib.auth.models import User

from hostel.models import allocate_block
from .models import student_report_problem, warden_report_problem
from hostel.models import hostel, hostel_block, room, allocate_room,allocate_block

# student problem report form
class studentReportProblemForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=User.objects.all(),
                                    widget=forms.HiddenInput())
    allocateroom = forms.ModelChoiceField(queryset=allocate_room.objects.all(),
                                    widget=forms.HiddenInput())

    class Meta:
        model = student_report_problem
        fields = ('student', 'problem_type', 'image', 'description', 'allocateroom')

    # def clean_image(self):
    #     image_file = self.cleaned_data.get('image')
    #     if not image_file.name.endswith(".jpg"):
    #         raise forms.ValidationError("Look at your image file type")  
    #     return image_file


# warden problem report form
class wardenReportProblemForm(forms.ModelForm):
    warden = forms.ModelChoiceField(queryset=User.objects.all(),
                                    widget=forms.HiddenInput())
    allocateblock = forms.ModelChoiceField(queryset=allocate_block.objects.all(),
                                    widget=forms.HiddenInput())


    class Meta:
        model = warden_report_problem
        fields = ('warden', 'problem_title', 'details', 'allocateblock')


    # student problem report form
class sendFeedbackForm(forms.ModelForm):

    class Meta:
        model = student_report_problem
        fields = ('feedback',)
        
