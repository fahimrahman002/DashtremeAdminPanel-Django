from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return render(response,"index.html")
def calendar(response):
    return render(response,"calendar.html")