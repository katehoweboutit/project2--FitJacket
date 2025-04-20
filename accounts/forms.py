from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from .models import FitUser


class FitUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = FitUser
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'age', 'weight', 'Lifestyle_Habits', 'Additional_Notes')
        widgets = {
            'Lifestyle_Habits': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'Additional_Notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if FitUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


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