from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm,CreateUserForm
from django.contrib.auth import authenticate,login as login_django,logout as logout_django
from django.contrib.auth.decorators import login_required

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


