from django.shortcuts import render
from .utils import get_user_activity_by_muscle

def index(request):
    userActivity = get_user_activity_by_muscle(request.user)

    if sum(userActivity.values()) == 0: # if the user has not completed any exercises
        return render(request, 'myFitness/error.html')
    else:
        return render(request, 'myFitness/index.html',
                  {'userActivity': userActivity})
