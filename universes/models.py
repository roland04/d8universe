from django.db import models

class Atribute(models.Model):
    name = models.CharField(max_length=20)
    short_name  = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField(max_length=20)
    atribute = models.ForeignKey(Atribute)

    def __str__(self):
        return '%s (%s)' % (self.name, self.atribute.short_name)

class Feature(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    rule = models.CharField(max_length=120)
    cost = models.DecimalField(max_digits=3, decimal_places=0)

class Universe(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    atributes = models.ManyToManyField(Atribute)
    abilities = models.ManyToManyField(Ability)
    features = models.ManyToManyField(Feature)
    HP_tag = models.CharField(max_length=20, default="Hit Points")
    EP_tag = models.CharField(max_length=20, default="Energy Points")

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    atributes = models.ManyToManyField(Atribute, through='StartAtribute')

    def __str__(self):
        return self.name

class StartAtribute(models.Model):
    race = models.ForeignKey(Race)
    atribute = models.ForeignKey(Atribute)
    universe = models.ForeignKey(Universe)
    value = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return '%s initial %s' % (self.race, self.atribute)
