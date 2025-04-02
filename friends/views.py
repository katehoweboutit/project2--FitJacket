from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_data = {}
    template_data['title'] = 'Friends'
    return render(request, 'friends/index.html',
                  {'template_data': template_data})
