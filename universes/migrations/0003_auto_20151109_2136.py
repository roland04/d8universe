# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universes', '0002_auto_20151109_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=3, decimal_places=0, default=1)),
            ],
        ),
        migrations.RenameModel(
            old_name='Atribute',
            new_name='Attribute',
        ),
        migrations.RemoveField(
            model_name='startatribute',
            name='atribute',
        ),
        migrations.RemoveField(
            model_name='startatribute',
            name='race',
        ),
        migrations.RemoveField(
            model_name='startatribute',
            name='universe',
        ),
        migrations.RenameField(
            model_name='ability',
            old_name='atribute',
            new_name='attribute',
        ),
        migrations.RenameField(
            model_name='universe',
            old_name='atributes',
            new_name='attributes',
        ),
        migrations.RemoveField(
            model_name='race',
            name='atributes',
        ),
        migrations.DeleteModel(
            name='StartAtribute',
        ),
        migrations.AddField(
            model_name='startattribute',
            name='attribute',
            field=models.ForeignKey(to='universes.Attribute'),
        ),
        migrations.AddField(
            model_name='startattribute',
            name='race',
            field=models.ForeignKey(to='universes.Race'),
        ),
        migrations.AddField(
            model_name='startattribute',
            name='universe',
            field=models.ForeignKey(to='universes.Universe'),
        ),
        migrations.AddField(
            model_name='race',
            name='attributes',
            field=models.ManyToManyField(through='universes.StartAttribute', to='universes.Attribute'),
        ),
    ]
