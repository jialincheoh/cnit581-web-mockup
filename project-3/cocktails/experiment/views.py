from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Task</h1')

def dashboard(request):
    return HttpResponse('<h1>Dashboard</h1>')

