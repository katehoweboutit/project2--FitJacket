from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='friends.index'),
    path('/add_friend', views.add_friend, name='friends.add_friend')
]