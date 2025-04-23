from django.db import models
from exercise.models import Exercise
from exercise.models import ExerciseAssignment
# Create your models here.
class createMyFitness(models.Model):
    def calculate_fitnessing(self):
        arr = [['abdominals', 0], ['abductors', 0], ['adductors', 0], ['biceps',0], ['calves', 0],['chest', 0], ['forearms',0], ['glutes', 0], ['hamstrings', 0], ['lats', 0], ['lower back',0],
               ['middle back',0], ['neck',0], ['quadriceps',0], ['traps',0], ['triceps',0]]

        assignments = ExcerciseAssignment.objects.select_related('excercise')
        for assignment in assignments:
            muscles = assignment.excercise.target_muscles
        if isinstance(muscles, str):
            muscles = [m.strip() for m in muscles.split(',')]

        for muscle in arr:
            if muscle in arr:
                muscle_groups[muscle] += 1

        return [[muscle, count] for muscle, count in arr.items()]

