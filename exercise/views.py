from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_data = {}
    template_data['title'] = 'Exercises'
    return render(request, 'exercise/index.html',
                  {'template_data': template_data})
