# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universes', '0004_auto_20151110_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='ability',
            name='description',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attribute',
            name='description',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
