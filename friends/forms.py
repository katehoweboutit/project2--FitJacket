from django import forms
from django.contrib.auth.forms import UserCreationForm

class FriendForm(forms.Form):
    friend_name = forms.CharField()