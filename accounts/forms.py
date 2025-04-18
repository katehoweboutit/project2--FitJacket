from typing import Any

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import FitUser

class FitUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(FitUserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = FitUser
        fields = ('email', 'username', 'first_name', 'last_name', 'age', 'weight', 'LifestyleHabits', 'AdditionalNotes')



"""
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        (super(CustomUserCreationForm, self).__init__(*args, **kwargs))

        for field_name in ['username', 'password1',
                'password2']:
            self.fields[field_name].help_text = None
            self.fields[field_name].widget.attrs.update(
                    {'class': 'form-control'}
            )


class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''

        return mark_safe(''.join([
                f'<div class="alert alert-danger" role="alert"> {e}</div>' for e in self]))
"""