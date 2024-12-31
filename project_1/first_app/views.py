from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("This is firstapp/ courses page .")
def about(request):
    return HttpResponse("This is firstapp/ about page .")
def home(request):
    return HttpResponse("This is firstapp/ home page .")