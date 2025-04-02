from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_data = {}
    template_data['title'] = 'My Fitness'
    return render(request, 'myFitness/index.html',
                  {'template_data': template_data})
