from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('string1 from app1')

def second(request):
    return HttpResponse('string2 from app1')

