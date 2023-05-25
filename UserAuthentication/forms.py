from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateNewUser(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CreateNewUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'placeholder': 'Enter your username', 'autofocus': False}
        self.fields['first_name'].widget.attrs = {
            'placeholder': 'Enter your name', 'required': True}
        self.fields['email'].widget.attrs = {
            'placeholder': 'Enter your email', 'required': True}
        self.fields['password1'].widget.attrs = {
            'placeholder': 'Enter your password' ,'id':'password1'}
        self.fields['password2'].widget.attrs = {
            'placeholder': 'Enter your again password','id':'password2'}

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
