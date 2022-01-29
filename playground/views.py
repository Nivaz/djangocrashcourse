from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#returns a http respose Hello world in playground/urls

def say_hello (request):

    return HttpResponse('Hello World')