# Generated by Django 3.2 on 2021-04-18 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiarySiteApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='planned_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 17, 59, 53, 556937), verbose_name='запланированная дата'),
        ),
    ]
