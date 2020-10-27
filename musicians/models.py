from django.db import models


class Musician(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    instrumento = models.CharField(max_length=255)


class Bio(models.Model):
    musician = models.OneToOneField(Musician, on_delete=models.CASCADE)
    hometown = models.CharField(max_length=255)


class Album(models.Model):
    name = models.CharField(max_length=255)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

# Create your models here.
