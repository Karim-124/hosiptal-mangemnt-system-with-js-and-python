from .models import *
from django.forms import ModelForm, TextInput, EmailInput ,FileInput
from django import forms 

class ProfilePatient(ModelForm):
    class Meta:
        model = Patient
        widgets = {
        'name': TextInput(attrs={
        'placeholder': 'enter your name',
        'required' : True,
        'id' : "name",
        "pattern" : "[a-zA-Z0-9]+",
        }),
        'email': TextInput(attrs={
        'placeholder': 'enter your email',
        'required' : True,
        'id' : "tel",
        }),
        'phone_number': TextInput(attrs={
        'placeholder': 'enter your number',
        'required' : True,
        'id' : "tel",
         type : "tel",
        }),
        'address': TextInput(attrs={
        'placeholder': 'enter your address',
        'id' : "tel",
        "type" : "text",
        }),
        'profile_img': FileInput(attrs={
        'id' : "tel",
        "type" : "file",
        }),
        }

        fields = ['name','email','gender','phone_number','address','city','profile_img']
        
        
  