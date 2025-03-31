from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("home index placeholder view (temporary)")

    # return render(request, 'home/index.html')


def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html',
                  {'template_data': template_data})

