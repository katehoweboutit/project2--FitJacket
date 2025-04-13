from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='exercise.index'),
    path('newExercise/', views.new_exercise, name='exercise.new_exercise'),
    path('viewExercise/<int:id>', views.view_exercise, name='exercise.viewExercise'),
    path('completeExercise/<int:id>', views.complete_exercise, name='exercise.completeExercise')
]
