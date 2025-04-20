from django.db import models
from accounts.models import FitUser

class Exercise(models.Model):
    muscle_group = models.CharField(max_length=30, default="none")
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    equipment_needed = models.CharField(max_length=128)
    instructions = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class ExerciseAssignment(models.Model):
    id = models.AutoField(primary_key=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(FitUser, on_delete=models.CASCADE)
    fitpoint_reward = models.IntegerField(default=5)
    completed = models.BooleanField(default=False)
    duration_minutes = models.IntegerField(default=10)
    # can add time here

    def __str__(self):
        return f'{self.exercise.name} - {self.duration_minutes} minutes - {self.user.username}'