# Generated by Django 2.1.5 on 2019-02-07 20:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190207_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 20, 3, 51, 288733, tzinfo=utc)),
        ),
    ]
