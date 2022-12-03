from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Curator(models.Model):
    first_name = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, null= True, on_delete=models.DO_NOTHING, related_name='curator')


class Direction(models.Model):
    name = models.CharField(max_length=20)
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE, related_name='direction')


class Group(models.Model):
    nomer = models.CharField(max_length=20)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='group')


class Discipline(models.Model):
    name = models.CharField(max_length=20)
    leson = models.CharField(max_length=20)
    dz = models.CharField(max_length=20)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='discipline')


class Student(models.Model):
    name = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='student')