# Generated by Django 3.1.6 on 2021-04-02 05:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20210304_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 4, 2, 5, 23, 41, 259902, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
