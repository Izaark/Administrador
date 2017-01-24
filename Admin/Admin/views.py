from django.shortcuts import render,redirect

def home(request):
	return render(request,'home_page.html',{})
def error_404(request):
	return render(request,'error_404.html',{})

