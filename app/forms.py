from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'service_number', 'position', 'date_of_enrollment', 'year_of_birth', 'boat_number',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'service_number': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_enrollment': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'boat_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('date', 'boat_number', 'district', 'number_of_detainees', )
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'boat_number': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_detainees': forms.TextInput(attrs={'class': 'form-control'}),
        }
