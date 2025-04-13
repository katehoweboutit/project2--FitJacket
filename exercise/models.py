from django.db import models
from accounts.models import FitUser

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    equipment_needed = models.CharField(max_length=128)
    instructions = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class ExerciseAssignment(models.Model):
    id = models.AutoField(primary_key=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(FitUser, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    duration_minutes = models.IntegerField()

    def __str__(self):
        return f'{self.exercise.name} - {self.duration_minutes} minutes - {self.user.username}'