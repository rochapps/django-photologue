# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photos',
            field=models.ManyToManyField(related_name='galleries', verbose_name='photos', to='photologue.Photo', blank=True),
        ),
    ]
