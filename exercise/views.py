from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_data = {}
    template_data['title'] = 'Exercises'
    return render(request, 'exercise/index.html',
                  {'template_data': template_data})


def new_exercise(request):
    template_data = {}
    template_data['title'] = 'Exercises'
    return render(request, 'exercise/new_exercise.html',
                  {'template_data': template_data})