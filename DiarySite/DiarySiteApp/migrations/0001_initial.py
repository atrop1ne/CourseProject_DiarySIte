# Generated by Django 3.2 on 2021-04-12 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id категории')),
                ('name', models.CharField(max_length=200, verbose_name='название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id события')),
                ('name', models.CharField(max_length=30, verbose_name='название события')),
                ('description', models.TextField(verbose_name='описание события')),
                ('planned_date', models.DateTimeField(verbose_name='запланированная дата')),
                ('is_done', models.BooleanField(verbose_name='выполнено')),
                ('on_repeat', models.BooleanField(verbose_name='повторяется')),
                ('to_remind', models.BooleanField(verbose_name='напоминание')),
                ('remind_date', models.DateTimeField(verbose_name='дата напоминания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiarySiteApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='почта пользователя')),
                ('password', models.CharField(max_length=30, verbose_name='пароль пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id события')),
                ('name', models.CharField(max_length=30, verbose_name='название тега')),
                ('event', models.ManyToManyField(to='DiarySiteApp.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiarySiteApp.user'),
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DiarySiteApp.user'),
        ),
    ]
