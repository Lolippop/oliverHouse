# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 1, 31, 3, 1, 56, 997606, tzinfo=utc), unique=True, max_length=100),
            preserve_default=False,
        ),
    ]
