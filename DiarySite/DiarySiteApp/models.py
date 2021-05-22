from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField('фото пользователя', null=True, blank=True, upload_to='profiles/%Y/%m/%d')

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance, created, **kwargs):
        try:
            instance.account.save()
        except ObjectDoesNotExist:
            Account.objects.create(user=instance)


    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return f"{self.user}"

    @property
    def tags(self):
        return Tag.objects.filter(account = self)

    @property
    def notes(self):
        return Note.objects.filter(account = self)

class Tag(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField('название тега', max_length=30, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        abstract = False
    
class Note(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField('название заметки', max_length=30, null=True, blank=True)
    description = models.TextField('описание заметки', null=True, blank=True)
    planned_date = models.DateTimeField('запланированная дата', null=True, blank=True)
    on_repeat = models.BooleanField('повторяется')
    to_remind = models.BooleanField('напоминание')
    remind_date = models.DateTimeField('дата напоминания', null=True, blank=True)
    on_delete = models.BooleanField('удалено', default=False)
    delete_date = models.DateField('дата удаления', null=True, blank=True, editable=False)
    tag = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        abstract = False

    def __str__(self):
        return f'Заметка "{self.title}"'

    @property
    def tags(self):
        return Tag.objects.filter(note = self)