from django import forms
from django.contrib.auth.models import User
from .models import hostel, hostel_block, room, allocate_block, allocate_room

# student problem report form
class registerHostelForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = hostel
        fields = ('created_by', 'name', 'location')


class registerBlockForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = hostel_block
        fields = ('created_by', 'block_name', 'hostel_name')


class registerRoomForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = room
        fields = ('created_by', 'room_no', 'block_name', 'hostel_name')


class allocateRoomForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=0, is_superuser = 0))

    class Meta:
        model = allocate_room
        fields = ('student', 'room', 'block_name', 'hostel_name')


class allocateBlockForm(forms.ModelForm):
    warden = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=1, is_superuser = 0))

    class Meta:
        model = allocate_block
        fields = ('warden', 'block_name', 'hostel_name')