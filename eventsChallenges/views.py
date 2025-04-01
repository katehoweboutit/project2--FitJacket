from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_data = {}
    template_data['title'] = 'Events and Challenges'
    return render(request, 'eventsChallenges/index.html',
                  {'template_data': template_data})
