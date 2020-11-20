from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .models import *
from .forms import *


class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"

    template_name = "login.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def person_add(request):
    context = {}
    form = PersonForm(request.POST or None)
    context['data'] = Person.objects.all()
    print(form.is_valid())
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_patrol.html", context)


def result_add(request):
    context = {}
    form = ResultForm(request.POST or None)
    context['data'] = Result.objects.all()
    print(form.is_valid())
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_result.html", context)


def schedule(request):
    context = {'data_p': Person.objects.all(), 'data_r': Result.objects.all()}
    return render(request, 'navbar.html', context)


def person(request, person_id):
    try:
        context = {'data_p': Person.objects.get(pk=person_id)}
    except User.DoesNotExist:
        raise Http404("Пользователя не сущетсвует")
    return render(request, 'person.html', context)


def persons(request):
    context = {'data_p': Person.objects.all()}
    return render(request, 'persons.html', context)


def logout(request):
    return render(request, "registration/logout.html")


def delete(request, person_id):
    try:
        person = Person.objects.get(id=person_id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return Http404("Пользователя не сущетсвует")


def edit(request, person_id):
    try:
        data_p = Person.objects.get(id=person_id)

        if request.method == "POST":
            data_p.name = request.POST.get("name")
            data_p.boat_number = request.POST.get("boat_number")
            data_p.date_of_enrollment = request.POST.get("date_of_enrollment")
            data_p.position = request.POST.get("position")
            data_p.service_number = request.POST.get("service_number")
            data_p.year_of_birth = request.POST.get("year_of_birth")
            data_p.save()
            return HttpResponseRedirect("/persons")
        else:
            return render(request, "edit.html", {"data_p": data_p})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

