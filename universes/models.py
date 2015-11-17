from django.db import models
from django.contrib.auth.models import User

class Attribute(models.Model):
    name = models.CharField(max_length=20)
    short_name  = models.CharField(max_length=3)
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField(max_length=20)
    attribute = models.ForeignKey(Attribute)
    description = models.CharField(max_length=120)

    def __str__(self):
        return '%s (%s)' % (self.name, self.attribute.short_name)

class Feature(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    rule = models.CharField(max_length=120)
    cost = models.DecimalField(max_digits=3, decimal_places=0)

class Universe(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    attributes = models.ManyToManyField(Attribute)
    abilities = models.ManyToManyField(Ability)
    features = models.ManyToManyField(Feature)
    hp_tag = models.CharField(max_length=20, default="Hit Points")
    ep_tag = models.CharField(max_length=20, default="Energy Points")
    creators = models.ManyToManyField(User, through="UniverseManager")

    def __str__(self):
        return self.name

class UniverseManager(models.Model):
    user = models.ForeignKey(User)
    universe = models.ForeignKey(Universe)
    role = models.CharField(max_length=20, default="Manager")

    def __str__(self):
        return 'Universe:%s, User:%s -> %s' % (self.universe, self.user, self.role)

class Race(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    attributes = models.ManyToManyField(Attribute, through='RaceAttribute')

    def __str__(self):
        return self.name

class RaceAttribute(models.Model):
    race = models.ForeignKey(Race)
    attribute = models.ForeignKey(Attribute)
    universe = models.ForeignKey(Universe)
    value = models.DecimalField(max_digits=3, decimal_places=0, default=1)

    def __str__(self):
        return 'Universe:%s, Race:%s, Attribute:%s -> %s' % (self.universe, self.race, self.attribute, self.value)
