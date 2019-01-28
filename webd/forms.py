from django import forms
from . models import FormM

class Form(forms.ModelForm):


    class Meta:
        model = FormM
        fields = ['fname','lname','email','branch','year','mobileno']

class Check(forms.Form):
    check=forms.CharField()
    subject=forms.CharField()
    message=forms.CharField()