from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, EmailInput , PasswordInput,FileInput
from django.contrib.auth.forms import UserCreationForm
from django import forms


class ManagerProfile(ModelForm):
    class Meta:
        model = Patient
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'enter your name',
                'required': True,
                'id': "name",
                "pattern": "[a-zA-Z0-9]+",
            }),
            'email': TextInput(attrs={
                'placeholder': 'enter your email',
                'required': True,
                'id': "tel",
            }),
            'phone_number': TextInput(attrs={
                'placeholder': 'enter your number',
                'required': True,
                'id': "tel",
                type: "tel",
            }),
            'address': TextInput(attrs={
                'placeholder': 'enter your address',
                'id': "tel",
                "type": "text",
            }),
            'profile_img': FileInput(attrs={
                'id': "tel",
                "type": "file",
            }),
        }

        fields = ['name', 'email', 'gender', 'phone_number', 'address', 'profile_img']
class CreationUser(UserCreationForm):
    class Meta:
        model = User
        widgets = {
            'username': TextInput(attrs={
            'placeholder': 'enter user name',
            'required' : True,
              }),
            }
        fields = ['username','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(CreationUser, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password from numbers and letters of the Latin alphabet'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Password confirmation'})

        

class Creationspecification(ModelForm):
    class Meta:
        model = Specialization
        widgets = {
            'name': TextInput(attrs={
            'placeholder': 'enter a specification',
            'required' : True,
              })
            }
        fields = ['name']
        
class CreationDoctor(ModelForm):
    class Meta:
        model = Doctor
        widgets = {
              
            'name': TextInput(attrs={
                'placeholder': 'enter Doctor Name',
                'required' : True,
                'id' : 'name',
                
              }),
            
            'email': EmailInput(attrs={
                'placeholder': 'enter Doctor Email',
                'required' : True,
              }),
            
            'phone_number': TextInput(attrs={
                'placeholder': 'enter a number ',
                'required' : True,
              }),
            
            'address': TextInput(attrs={
                'placeholder': 'enter address ',
              }),
        }
        
        fields = ['user','Specialization','name','email','phone_number','gender','salary','address','profile_img']
        
        

