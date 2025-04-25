from django.shortcuts import render
from django.http import HttpResponse
from .models import createMyFitness
from .utils import get_user_activity_by_muscle
def index(request):
    template_data = {}
    template_data['title'] = 'My Fitness'
    return render(request, 'myFitness/index.html',
                  {'template_data': template_data})
#request.user.fit_points += exercise.fitpoint_reward
def listofDeath(request, id):
    #exercise = ExerciseAssignment.objects.get(id=id)
    template_data = createMyFitness(id).calculate_fitnessing()
    return render(request, 'myFitness/index.html', {'template_data': template_data})
    #exercise.completed = True
    #exercise.save()
    #request.user.fit_points += exercise.fitpoint_reward
    #request.user.save()

    #template_data = {}
    #template_data['title'] = 'Complete Exercise'
    #template_data['exercise'] = exercise
    #template_data['user_name'] = request.user.first_name

    #return render(request, 'exercise/complete_exercise.html', {'template_data': template_data})
def randoList(request, id):
    template_data = createMyFitness(id).rando_fitness()
    return render(request, 'myFitness/index.html', {'template_data': template_data})