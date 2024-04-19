from django.db import models
from products.models import *
from shop.models import *


class ProductPrice(models.Model):
    product = models.ForeignKey(Products, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Товар', related_name='get_product_shop')
    shop = models.ForeignKey(Shop, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Магазин', related_name='get_shop_product')
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')
    new_price = models.FloatField(default=0, blank=True, null=True, verbose_name='Новая цена')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, blank=True, null=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Цена на товар"
        verbose_name_plural = "Цена на товар"
        ordering = ["created_at"]

    def __str__(self):
        return self.product.title + ' - ' + self.shop.title
