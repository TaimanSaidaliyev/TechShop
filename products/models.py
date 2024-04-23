from django.db import models
from django.db.models import Min


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название категории')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание категории')
    image = models.ImageField(upload_to='media/categories/%Y/%m/%d', blank=True, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, blank=True, null=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название бренда')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание бренда')
    image = models.ImageField(upload_to='media/categories/%Y/%m/%d', blank=True, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, blank=True, null=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Бренды'
        verbose_name_plural = 'Бренды'
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Colours(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Цвет')
    html_color = models.CharField(max_length=7, blank=True, verbose_name='HTML цвет')
    image = models.ImageField(upload_to='media/categories/%Y/%m/%d', blank=True, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, blank=True, null=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Цвета'
        verbose_name_plural = 'Цвета'
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название товара')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание товара')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, blank=True, null=True, verbose_name='Дата обновления')
    category = models.ForeignKey(Category, blank=True, on_delete=models.PROTECT, verbose_name='Категория товара')
    html_color = models.ForeignKey(Colours, blank=True, on_delete=models.PROTECT, verbose_name='Цвет')
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.PROTECT, verbose_name='Бренд>')
    image = models.ImageField(upload_to='media/products/%Y/%m/%d', blank=True, verbose_name='Изображение')

    def get_min_price_info(self):
        price_data = self.get_product_shop.annotate(min_price=Min('price')).order_by('min_price').first()
        if price_data:
            return {
                'min_price': price_data.price,
                'shop_id': price_data.shop.id
            }
        return None

    def get_min_new_price_info(self):
        price_data = self.get_product_shop.annotate(min_new_price=Min('new_price')).order_by('min_new_price').first()
        if price_data:
            return {
                'min_new_price': price_data.new_price,
                'shop_id': price_data.shop.id
            }
        return None

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['created_at']

    def __str__(self):
        return self.title