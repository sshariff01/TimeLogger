# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_remove_log_hours_worked'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='hours_worked',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0.5)]),
        ),
    ]
