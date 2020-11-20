from django.contrib import admin
from django.urls import path, include
from app.views import *


urlpatterns = [
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('person_add', person_add, name="person_add_url"),
    path('result_add', result_add, name="result_add_url"),
    path('accounts/profile/', schedule, name="schedule_url"),
    path('persons', persons, name="persons_url"),
    path('person/<int:person_id>/', person, name="person_url"),
    path('logout', logout, name="logout_url"),
    path('delete/<int:person_id>/', delete, name="delete_url"),
    path('edit/<int:person_id>/', edit, name="edit_url"),
]
