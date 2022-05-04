from django import forms
from django.contrib.auth.models import User
from .models import hostel, hostel_block

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
        