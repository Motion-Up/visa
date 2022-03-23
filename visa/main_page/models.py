from django.db import models


class Article(models.Model):
    title = models.CharField('Загаловок', max_length=200)
    text = models.TextField('Текс статьи')
    created_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(
        'Картинка',
        upload_to='visa/',
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Service(models.Model):
    title = models.CharField('Загаловок', max_length=200)
    text = models.TextField('Услуга')
    price = models.IntegerField('Цена')
    amount_of_days = models.IntegerField('Количество дней')

    def __str__(self): 
        return self.title
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'