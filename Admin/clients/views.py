from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm,CreateUserForm,EditUserForm,EditPasswordForm
from django.contrib.auth import authenticate,update_session_auth_hash,login as login_django,logout as logout_django
from django.contrib.auth.decorators import login_required
from django.views.generic import View,DetailView,CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User


class ShowView(DetailView):
	model = User
	template_name = 'clients/show.html'
	slug_field ='username'
	slug_url_kwarg = 'username_url'

class LoginView(View):
	form = LoginUserForm()
	message = None
	template = 'clients/login.html'

	def get(self,request,*args,**kwargs):
		if request.user.is_authenticated():
			return redirect('client:dashboard')
		return render(request,self.template, self.get_context())

	def post(self,request,*args,**kwargs):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)	
		if user is not None:
			login_django(request,user)
			return redirect('client:dashboard')
		else:
			self.message = "User or password incorrect"
		return render(request,'clients/login.html', self.get_context())

	def get_context(self):
		return {'form':self.form,'message':self.message}


class DashboardView(LoginRequiredMixin,View):
	login_url = 'client:login'
	def get(self,request,*args,**kwargs):
		return render(request,'clients/dashboard.html', {})

class Create(CreateView):
	success_url = reverse_lazy('client:login')
	template_name = 'clients/create.html'
	model = User
	form_class = CreateUserForm

	def form_valid(self,form):
		self.object = form.save(commit=False)
		self.object.set_password(self.object.password)
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())
 

class Edit(UpdateView): 
	model = User
	template_name = 'clients/edit.html'
	form_class = EditUserForm
	success_url = reverse_lazy('client:dashboard')

	def get_object(self,queryset = None):
		return self.request.user

def edit_password(request):
	message = ""
	form = EditPasswordForm(request.POST or None)
	if request.method =='POST':
		if form.is_valid():
			current_password = form.cleaned_data['password']
			new_password = form.cleaned_data['new_password']
			if authenticate(username=request.user.username, password=current_password):
				request.user.set_password(new_password)
				request.user.save()
				update_session_auth_hash(request,request.user)
				message = "password actualizado"

	context = {'form':form,'message':message}
	return render(request,'clients/edit_password.html',context)



def login(request):
	if request.user.is_authenticated():
		return redirect('client:dashboard')

	message = None
	# name = 'isaac'
	# age = 15
	# context = {
	# 'name': name, 'age':age
	# }
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username,password=password)
		if user is not None:
			login_django(request,user)
			return redirect('client:dashboard')
		else:
			message = "User or password incorrect"

	form = LoginForm()
	context = {
	'form': form,
	'message': message
	}
	return render(request,'clients/login.html', context)

@login_required(login_url = 'client:login')
def dashboard(request):
	return render(request,'clients/dashboard.html', {})

@login_required(login_url = 'client:login')	
def logout(request):
	logout_django(request)
	return redirect('client:login')

def create(request): 
	form = CreateUserForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			return redirect('client:login')
	context={
	'form': form
	}
	return render(request,'clients/create.html',context)




