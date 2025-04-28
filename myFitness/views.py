from django.shortcuts import render
from .utils import get_user_activity_by_muscle

def index(request):
    userActivity = get_user_activity_by_muscle(request.user)

    template_data = {}
    template_data['userActivity'] = userActivity
    template_data['title'] = 'My Fitness'

    if sum(userActivity.values()) == 0: # if the user has not completed any exercises
        return render(request, 'myFitness/error.html',
                      {'template_data': template_data})
    else:
        return render(request, 'myFitness/index.html',
                  {'template_data': template_data})
