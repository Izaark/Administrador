from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView
from .forms import CreateProjectForm
from .models import Project
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from status.models import Status

class CreateProjectClass(CreateView, LoginRequiredMixin):
	login_url = 'client_login'
	model = Project
	template_name = 'project/create.html'
	form_class = CreateProjectForm
	

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.user = self.request.user
		self.object.save()
		self.object.projectstatus_set.create(status = Status.getDefaultStatus())	#crea un status por defaul despues de guardar
		return HttpResponseRedirect(self.getUrlProject())

	def getUrlProject(self):
		return reverse_lazy('project:show', kwargs = {'slug': self.object.slug})

class ListClass(ListView, LoginRequiredMixin):
	login_url = 'client_login'
	template_name = 'project/own.html'
	paginate_by = 3

	def get_queryset(self):
		return Project.objects.filter(user = self.request.user).order_by('dead_line')


class ShowClass(DetailView):
	model = Project
	template_name = 'project/show.html'

		

