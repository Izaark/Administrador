from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from status.models import Status
from django.utils import timezone

import datetime

class Project(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length=60)
	description = models.TextField()
	dead_line = models.DateField()
	create_date = models.DateField(default = datetime.date.today)
	slug = models.CharField(max_length=50,default='')

	def __str__(self):
		return self.title

	def validate_unique(self, exclude=None):
		if Project.objects.filter(title = self.title).exists():
			raise ValidationError('Ya se creo un proyecto con el mismo titulo')

	def save(self, *args, **kwargs):
		self.validate_unique()
		self.slug = self.title.replace(' ','_').lower()
		super(Project, self).save(*args, **kwargs)



class ProjectStatus(models.Model):
	project = models.ForeignKey(Project)
	status = models.ForeignKey(Status)
	create_date = models.DateTimeField(default = timezone.now)

	class Meta:
		verbose_name_plural='ProjectStatus'


		
        
    