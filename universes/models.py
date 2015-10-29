from django.db import models

class Atribute(models.Model):
    name = models.CharField(max_length=20)
    short_name  = models.CharField(max_length=3)

    def __str__(self):
        return '%s (%s)' % (self.name, self.short_name)

class Ability(models.Model):
    name = models.CharField(max_length=20)
    atribute = models.ForeignKey(Atribute)

    def __str__(self):
        return '%s (%s)' % (self.name, self.atribute.short_name)

class Universe(models.Model):
    name = models.CharField(max_length=200)
    atributes = models.ManyToManyField(Atribute)
    abilities = models.ManyToManyField(Ability)

    def __str__(self):
        return self.name
