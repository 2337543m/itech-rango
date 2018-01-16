from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("all around me are familiar faces")

# Create your views here.
