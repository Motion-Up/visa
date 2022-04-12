from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Article(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField('Загаловок', max_length=200),
        text = models.TextField('Текс статьи'),
        created_date = models.DateTimeField('Дата публикации', auto_now_add=True),
        image = models.ImageField(
            'Картинка',
            upload_to='visa/',
            blank=True,
        )
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Service(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField('Загаловок', max_length=200),
        text = models.TextField('Услуга'),
        price = models.IntegerField('Цена'),
        amount_of_days = models.IntegerField('Количество дней')
    )

    def __str__(self): 
        return self.title
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Client(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField('Имя', max_length=200),
        phone = models.CharField('Телефон', max_length=200),
        email = models.EmailField('Почта'),
        created_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'