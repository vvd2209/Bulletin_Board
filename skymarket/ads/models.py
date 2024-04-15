from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Ad(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена товара')
    description = models.TextField(max_length=1000, verbose_name='Описание товара')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                               **NULLABLE, verbose_name='Создатель объявления')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время'
                                                                      'создания объявления')

    class Meta:
        ordering = ['created_at']
        verbose_name = "объявление"
        verbose_name_plural = 'объявления'


class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name='Текст отзыва')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                               **NULLABLE, verbose_name='Создатель отзыва')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление, под которым '
                                                                      'оставлен отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время'
                                                                      'создания отзыва')

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = 'отзывы'
