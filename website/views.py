from django.shortcuts import render
from django.http import HttpResponse

def index_views(request):
    return render(request,'index.html')

def about_views(request):
    return render(request,'About.html')

def contact_views(request):
    return render(request,'contact.html')