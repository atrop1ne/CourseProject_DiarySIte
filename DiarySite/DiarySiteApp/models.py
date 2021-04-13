from django.db import models
from django.db.models.fields import TextField

class User(models.Model):
    id = models.AutoField('id пользователя', primary_key=True)
    email = models.EmailField('почта пользователя')
    password = models.CharField('пароль пользователя', max_length=30)

class Category(models.Model):
    id = models.AutoField('id категории', primary_key=True)
    name = models.CharField('название категории', max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Event(models.Model):
    id = models.AutoField('id события', primary_key=True)
    name = models.CharField('название события', max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = TextField('описание события', null=True)
    planned_date = models.DateTimeField('запланированная дата')
    is_done = models.BooleanField('выполнено')
    on_repeat = models.BooleanField('повторяется')
    to_remind = models.BooleanField('напоминание')
    remind_date = models.DateTimeField('дата напоминания', null=True)

class Tag(models.Model):
    id = models.AutoField('id события', primary_key=True)
    name = models.CharField('название тега', max_length=30, unique=True)
    event = models.ManyToManyField(Event)