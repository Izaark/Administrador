from django import forms
from django.contrib.auth.models import User
#Const
ERROR_MESSAGE_USER = {'required': 'El username es nesesario',
'unique':'El username ya se encuentra registrado','invalid':'Ingrese un username valido'}
ERROR_MESSAGE_PASSWORD = {'required':'El password es necesario'}
ERROR_MESSAGE_EMAIL = {'required': 'El username es nesesario',
'invalid':'Ingrese un correo valido'}

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput())

class CreateUserForm(forms.ModelForm):
	username = forms.CharField(max_length=30, error_messages=ERROR_MESSAGE_USER)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput(),error_messages=ERROR_MESSAGE_PASSWORD)
	email = forms.CharField(error_messages=ERROR_MESSAGE_EMAIL)

	class Meta:
		model= User
		fields =('username','password','email')

class EditUserForm(forms.ModelForm):
	username = forms.CharField(max_length=30, error_messages=ERROR_MESSAGE_USER)
	email = forms.CharField(error_messages=ERROR_MESSAGE_EMAIL)
	class Meta:
		model = User
		fields =('username','email','first_name','last_name')




