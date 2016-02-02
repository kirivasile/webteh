# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
        ('questions', '0006_auto_20151115_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(related_name='answers', to='authen.MyUser', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(related_name='questions', to='authen.MyUser', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 11, 2, 25, 950480, tzinfo=utc)),
        ),
    ]
