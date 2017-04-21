from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from status.models import Status
from django.utils import timezone

import datetime

class Project(models.Model):

	#user = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length=60)
	description = models.TextField()
	dead_line = models.DateField()
	create_date = models.DateField(default = datetime.date.today)
	slug = models.CharField(max_length=50,default='')

	def __str__(self):
		return self.title

	def validate_unique(self, exclude=None):
		self.slug = self.create_slug_field(self.title)
		if Project.objects.filter(slug = self.slug).exclude(pk = self.id).exists():
			raise ValidationError('Un proyecto con el mismo titulo ya se encuentra registrado.')

	def create_slug_field(self, value):
		return value.lower().replace(" ", "-")

	def get_id_status(self):
		return self.projectstatus_set.last().status_id

	def get_status(self):
		return self.projectstatus_set.last().status


class ProjectStatus(models.Model):
	project = models.ForeignKey(Project)
	status = models.ForeignKey(Status)
	create_date = models.DateTimeField(default = timezone.now)

	class Meta:
		verbose_name_plural='ProjectStatus'

class ProjectPermission(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	level = models.IntegerField()
	create_deate = models.DateField(default= timezone.now)

	def __str__(self):
		return self.title

class ProjectUser(models.Model):
	project = models.ForeignKey(Project, on_delete = models.CASCADE)
	user = models.ForeignKey(User)
	permission = models.ForeignKey(ProjectPermission)
	create_date = models.DateField(default= timezone.now)


    


		
        
    