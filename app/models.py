from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    service_number = models.IntegerField()
    position = models.CharField(max_length=50)
    date_of_enrollment = models.DateField()
    year_of_birth = models.DateField()
    boat_number = models.IntegerField()


class Result(models.Model):
    date = models.DateField()
    boat_number = models.IntegerField()
    district = models.CharField(max_length=50)
    number_of_detainees = models.IntegerField()
