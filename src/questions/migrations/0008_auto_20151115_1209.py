# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20151115_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 12, 9, 34, 623750, tzinfo=utc)),
        ),
    ]
