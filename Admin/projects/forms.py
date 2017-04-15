from django import forms
from django.contrib.auth.models import User
from .models import Project
import datetime
class CreateProjectForm(forms.ModelForm):

	title = forms.CharField(label='Título', max_length=60,required=True)
	description = forms.CharField(label='Descripción',required=False, widget=forms.Textarea )
	dead_line = forms.DateField(initial=datetime.date.today)

	class Meta:
		model = Project
		fields = ('title','description','dead_line')

