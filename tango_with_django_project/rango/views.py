from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage' : "I'm blue daba dee daba die"}
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	return HttpResponse("there's a moose loose aboot this hoose <a href='/rango/'>Index</a>.")
# Create your views here.
