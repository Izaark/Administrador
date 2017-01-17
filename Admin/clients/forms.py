from django import forms
from django.contrib.auth.models import User

#Const
ERROR_MESSAGE_USER = {'required': 'El username es nesesario',
'unique':'El username ya se encuentra registrado','invalid':'Ingrese un username valido'}
ERROR_MESSAGE_PASSWORD = {'required':'El password es necesario'}
ERROR_MESSAGE_EMAIL = {'required': 'El username es nesesario',
'invalid':'Ingrese un correo valido'}

#Functions
def password_validation(value_password):
	if len(value_password) < 5:
		raise forms.ValidationError('The password requires minimun 5 characters')


#Class
class LoginUserForm(forms.Form):
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

class EditPasswordForm(forms.Form):
	password = forms.CharField(max_length=20, widget=forms.PasswordInput())
	new_password = forms.CharField(max_length=20, widget=forms.PasswordInput(),validators=[password_validation])
	repeat_password = forms.CharField(max_length=20, widget=forms.PasswordInput(),validators=[password_validation])

	def clean(self):
		clean_data = super(EditPassword,self).clean()
		password1 = clean_data['new_password']
		password2 = clean_data['repeat_password']
		if password1 != password2:
			raise forms.ValidationError('los passwords no coinciden')






