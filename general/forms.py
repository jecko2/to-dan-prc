from os import name
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Task
from django import forms
from django.forms.widgets import NumberInput, Widget


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ['client', 'start_date', 'end_date', ]
