# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('universes', '0003_auto_20151109_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceAttribute',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('value', models.DecimalField(max_digits=3, default=1, decimal_places=0)),
                ('attribute', models.ForeignKey(to='universes.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='UniverseManager',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('role', models.CharField(default='Manager', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='startattribute',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='startattribute',
            name='race',
        ),
        migrations.RemoveField(
            model_name='startattribute',
            name='universe',
        ),
        migrations.RemoveField(
            model_name='universecreator',
            name='universe',
        ),
        migrations.RemoveField(
            model_name='universecreator',
            name='user',
        ),
        migrations.RenameField(
            model_name='universe',
            old_name='EP_tag',
            new_name='ep_tag',
        ),
        migrations.RenameField(
            model_name='universe',
            old_name='HP_tag',
            new_name='hp_tag',
        ),
        migrations.AlterField(
            model_name='race',
            name='attributes',
            field=models.ManyToManyField(through='universes.RaceAttribute', to='universes.Attribute'),
        ),
        migrations.AlterField(
            model_name='universe',
            name='creators',
            field=models.ManyToManyField(through='universes.UniverseManager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='StartAttribute',
        ),
        migrations.DeleteModel(
            name='UniverseCreator',
        ),
        migrations.AddField(
            model_name='universemanager',
            name='universe',
            field=models.ForeignKey(to='universes.Universe'),
        ),
        migrations.AddField(
            model_name='universemanager',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='raceattribute',
            name='race',
            field=models.ForeignKey(to='universes.Race'),
        ),
        migrations.AddField(
            model_name='raceattribute',
            name='universe',
            field=models.ForeignKey(to='universes.Universe'),
        ),
    ]
