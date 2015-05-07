# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TodoLib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='progress',
            field=models.CharField(max_length=2),
        ),
    ]
