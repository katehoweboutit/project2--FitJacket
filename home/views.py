from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template_data = {}
    template_data['title'] = 'Home'
    return render(request, 'home/index.html',
                  {'template_data': template_data})


def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html',
                  {'template_data': template_data})

