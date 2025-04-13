from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='exercise.index'),
    path('newExercise/', views.new_exercise, name='exercise.new_exercise')
]
