from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'pyladiesapp/index.html')
	
def about(request):
	return render(request, 'pyladiesapp/about.html')