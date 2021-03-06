# Generated by Django 3.1.6 on 2021-04-02 05:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20210402_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 4, 2, 5, 24, 24, 705752, tzinfo=utc), verbose_name='생성일'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
    ]
