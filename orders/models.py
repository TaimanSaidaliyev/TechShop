from django.db import models
from products.models import *
from shop.models import *


class OrderStatus(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Статус заказа')
    html_color = models.CharField(max_length=7, blank=True, verbose_name='Цвет заказа')

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статус заказа'
        ordering = ['title']

    def __str__(self):
        return self.title


class OrderCart(models.Model):
    product = models.ForeignKey(Products, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Товар')
    shop = models.ForeignKey(Shop, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Магазин')
    status = models.ForeignKey('OrderStatus', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Статус заказа')
    count = models.IntegerField(default=1, verbose_name="Количество товаров")
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, blank=True, null=True, verbose_name="Дата обновления")
    delivery_date = models.DateField(blank=True, null=True, verbose_name="Дата доставки")

    class Meta:
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"
        ordering = ["created_at"]

    def __str__(self):
        return self.product.title + ' - ' + self.shop.title
