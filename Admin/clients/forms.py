from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput())

class CreateUserForm(forms.ModelForm):
	class Meta:
		model= User
		fields =('username','password','email')


