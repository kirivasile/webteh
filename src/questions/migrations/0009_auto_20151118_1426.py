# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
        ('questions', '0008_auto_20151115_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
                ('answer', models.ForeignKey(to='authen.MyUser')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 14, 26, 25, 38127, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='like',
            name='question',
            field=models.ForeignKey(to='questions.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(to='authen.MyUser', through='questions.Like'),
        ),
    ]
