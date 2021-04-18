from django.db import models
from django.conf import settings

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField('фото пользователя', null=True, blank=True, upload_to='profiles/%Y/%m/%d')
    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return f"{self.user}"

    @property
    def categories(self):
        return Category.objects.filter(account = self)

class Category(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField('название категории', max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    @property
    def events(self):
        return Event.objects.filter(category = self)

    @property
    def tags(self):
        return Tag.objects.filter(category = self)

class Tag(models.Model):
    name = models.CharField('название тега', max_length=30, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self):
        return self.name

class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('название события', max_length=30, null=True, blank=True)
    description = models.TextField('описание события', null=True, blank=True)
    planned_date = models.DateTimeField('запланированная дата', null=True, blank=True)
    on_repeat = models.BooleanField('повторяется')
    to_remind = models.BooleanField('напоминание')
    remind_date = models.DateTimeField('дата напоминания', null=True, blank=True)
    on_delete = models.BooleanField('удалено', default=False)
    delete_date = models.DateField('дата удаления', null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __init__(self):
        if self.planned_date == None:
            self.on_repeat = None

    def __str__(self):
        return f"Событие {self.name} категории {self.category}"