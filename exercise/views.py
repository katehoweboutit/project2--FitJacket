from django.shortcuts import render
from django.http import HttpResponse
from .utils import muscle_groups

def index(request):
    template_data = {}
    template_data['title'] = 'Exercises'
    return render(request, 'exercise/index.html',
                  {'template_data': template_data})


def new_exercise(request):
    if request.method == 'POST':
        print(request.POST.getlist('muscle_group'))

    template_data = {}
    template_data['title'] = 'New Exercise'
    template_data['muscle_groups'] = muscle_groups

    return render(request, 'exercise/new_exercise.html',
                  {'template_data': template_data})