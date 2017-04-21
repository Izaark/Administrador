from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView,ListView,DetailView
from .forms import CreateProjectForm
from .models import Project, ProjectUser
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from status.models import Status
from status.forms import StatusChoiceForm
from django.contrib import messages

class CreateProjectClass(CreateView, LoginRequiredMixin):
	login_url = 'client:login'
	model = Project
	template_name = 'project/create.html'
	form_class = CreateProjectForm
	

	def form_valid(self, form):
		self.object = form.save(commit = False)
		
		self.object.save()
		self.object.projectstatus_set.create(status = Status.getDefaultStatus())	#crea un status por defaul despues de guardar
		self.object.projectuser_set.create(user= self.request.user, permission_id = 1 )
		return HttpResponseRedirect(self.getUrlProject())

	def getUrlProject(self):
		return reverse_lazy('project:show', kwargs = {'slug': self.object.slug})

class ListClass(ListView, LoginRequiredMixin):
	login_url = 'client:login'
	template_name = 'project/own.html'
	paginate_by = 5

	def get_queryset(self):
		return ProjectUser.objects.filter(user = self.request.user)

class ShowClass(DetailView):
	model = Project
	template_name = 'project/show.html'

@login_required(login_url = 'client:login')
def edit(request, slug=''):
	project = get_object_or_404(Project, slug=slug)
	form_project = CreateProjectForm(request.POST or None, instance = project)
	forms_status = StatusChoiceForm(request.POST or None, initial={'status': project.get_id_status()})	#Ultimo status de proyecto

	if request.method == 'POST':
		if form_project.is_valid() and forms_status.is_valid():
			selection_id = forms_status.cleaned_data['status'].id	
			form_project.save()

			if selection_id != project.get_id_status():
				project.projectstatus_set.create(status_id = selection_id)
			messages.success(request, 'Datos actualizados')

	context = {
	'form_project': form_project,
	'forms_status': forms_status
	}
	return render(request, 'project/edit.html', context)

		

