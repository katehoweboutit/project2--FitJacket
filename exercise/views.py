from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import all_muscle_groups, update_db_exercises, update_assigned_exercises
from .models import ExerciseAssignment

def index(request):
    template_data = {}
    template_data['title'] = 'Exercises'
    template_data['exercise_assignments'] = ExerciseAssignment.objects.filter(user=request.user)
    return render(request, 'exercise/index.html',
                  {'template_data': template_data})


def new_exercise(request):
    if request.method == 'POST':
        checked_muscle_groups = request.POST.getlist('muscle_group')
        update_db_exercises(checked_muscle_groups)

        update_assigned_exercises(request.user, checked_muscle_groups)
        return redirect('exercise.index')

    template_data = {}
    template_data['title'] = 'New Exercise'
    template_data['muscle_groups'] = all_muscle_groups

    return render(request, 'exercise/new_exercise.html',
                  {'template_data': template_data})

def view_exercise(request, id):
    template_data = {}
    template_data['title'] = 'View Exercise'
    template_data['exercise_id'] = id

    return render(request, 'exercise/viewExercise.html',
                  {'template_data': template_data})