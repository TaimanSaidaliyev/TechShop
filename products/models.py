from django.db import models


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
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.PROTECT, verbose_name='Категория товара')
    image = models.ImageField(upload_to='media/products/%Y/%m/%d', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['created_at']

    def __str__(self):
        return self.title