from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage' : "I'm blue daba dee daba die"}
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'aboutmessage' : "This tutorial has een put together by Lord Awesome"}
	return render(request, 'rango/about.html', context=context_dict)
# Create your views here.
