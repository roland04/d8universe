# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Atribute',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('short_name', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=120)),
                ('rule', models.CharField(max_length=120)),
                ('cost', models.DecimalField(max_digits=3, decimal_places=0)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='StartAtribute',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('value', models.DecimalField(default=1, max_digits=3, decimal_places=0)),
                ('atribute', models.ForeignKey(to='universes.Atribute')),
                ('race', models.ForeignKey(to='universes.Race')),
            ],
        ),
        migrations.CreateModel(
            name='Universe',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=120)),
                ('HP_tag', models.CharField(default='Hit Points', max_length=20)),
                ('EP_tag', models.CharField(default='Energy Points', max_length=20)),
                ('abilities', models.ManyToManyField(to='universes.Ability')),
                ('atributes', models.ManyToManyField(to='universes.Atribute')),
            ],
        ),
        migrations.CreateModel(
            name='UniverseCreator',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('rank', models.CharField(default='Manager', max_length=20)),
                ('universe', models.ForeignKey(to='universes.Universe')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='universe',
            name='creators',
            field=models.ManyToManyField(through='universes.UniverseCreator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='universe',
            name='features',
            field=models.ManyToManyField(to='universes.Feature'),
        ),
        migrations.AddField(
            model_name='startatribute',
            name='universe',
            field=models.ForeignKey(to='universes.Universe'),
        ),
        migrations.AddField(
            model_name='race',
            name='atributes',
            field=models.ManyToManyField(through='universes.StartAtribute', to='universes.Atribute'),
        ),
        migrations.AddField(
            model_name='ability',
            name='atribute',
            field=models.ForeignKey(to='universes.Atribute'),
        ),
    ]
