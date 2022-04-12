# Generated by Django 4.0.3 on 2022-04-12 05:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_remove_article_created_date_remove_article_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default='ignfd@dsf.ry', max_length=254, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default='ignat', max_length=200, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default='43534243', max_length=200, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ClientTranslation',
        ),
    ]
