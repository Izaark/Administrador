from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CreateProjectForm
from .models import Project
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

class CreateProjectClass(CreateView, LoginRequiredMixin):

	success_url = reverse_lazy('client:dashboard')
	login_url = 'client_login'
	model = Project
	template_name = 'project/create.html'
	form_class = CreateProjectForm
	

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

