from django.db import models

class Universe(models.Model):
    category = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Atribute(models.Model):
    name = models.CharField(max_length=200)

class Ability(models.Model):
    name = models.CharField(max_length=200)
