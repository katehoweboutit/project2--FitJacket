from django.contrib import admin

from .models import Exercise
admin.site.register(Exercise)

from .models import ExerciseAssignment
admin.site.register(ExerciseAssignment)