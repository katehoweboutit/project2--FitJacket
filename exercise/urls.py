from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='exercise.index'),
    path('', views.index, name='exercise.show')
]
