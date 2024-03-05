from django.db import models


class Shop (models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название магазина')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание магазина')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, blank=True, null=True, verbose_name='Дата обновления')
    address = models.CharField(max_length=100, blank=True, verbose_name='Адрес магазина')
    telephone = models.CharField(max_length=100, blank=True, verbose_name='Номер телефона')
    coordinate_w = models.FloatField(default=0, blank=True, verbose_name='Коориданата по ширине')
    coordinate_h = models.FloatField(default=0, blank=True, verbose_name='Коориданата по долгота')
    image = models.ImageField(upload_to='media/shops/%Y/%m/%d', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Магазины'
        verbose_name_plural = 'Магазины'
        ordering = ['created_at']

    def __str__(self):
        return self.title

