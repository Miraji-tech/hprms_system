from django import forms
from django.contrib.auth.models import User
from .models import student_report_problem, warden_report_problem
from hostel.models import hostel, hostel_block, room, allocate_room

# student problem report form
class studentReportProblemForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=User.objects.all(),
                                    widget=forms.HiddenInput())
    hostel = forms.ModelChoiceField(queryset=hostel.objects.all(),
                                    widget=forms.HiddenInput())
    block_name = forms.ModelChoiceField(queryset=hostel_block.objects.all(),
                                    widget=forms.HiddenInput())
    room_name = forms.ModelChoiceField(queryset=room.objects.all(),
                                    widget=forms.HiddenInput())  

    class Meta:
        model = student_report_problem
        fields = ('student', 'problem_type', 'image', 'description', 'hostel', 'block_name', 'room_name')

    # def clean_image(self):
    #     image_file = self.cleaned_data.get('image')
    #     if not image_file.name.endswith(".jpg"):
    #         raise forms.ValidationError("Look at your image file type")
    #     return image_file


# warden problem report form
class wardenReportProblemForm(forms.ModelForm):
    warden = forms.ModelChoiceField(queryset=User.objects.all(),
                                    widget=forms.HiddenInput())
    hostel = forms.ModelChoiceField(queryset=hostel.objects.all(),
                                    widget=forms.HiddenInput())
    block_name = forms.ModelChoiceField(queryset=hostel_block.objects.all(),
                                    widget=forms.HiddenInput())

    class Meta:
        model = warden_report_problem
        fields = ('warden', 'problem_title', 'details', 'hostel', 'block_name')


    # student problem report form
class sendFeedbackForm(forms.ModelForm):

    class Meta:
        model = student_report_problem
        fields = ('feedback',)
        
