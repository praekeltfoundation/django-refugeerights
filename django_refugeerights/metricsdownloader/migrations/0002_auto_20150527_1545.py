# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metricsdownloader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricrecord',
            name='value',
            field=models.FloatField(),
        ),
    ]
