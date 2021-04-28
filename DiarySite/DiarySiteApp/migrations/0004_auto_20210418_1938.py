# Generated by Django 3.2 on 2021-04-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiarySiteApp', '0003_auto_20210418_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_done',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='delete_date',
            field=models.DateField(null=True, verbose_name='дата удаления'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='DiarySiteApp.Tag'),
        ),
    ]