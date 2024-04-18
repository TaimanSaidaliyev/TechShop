from django.db import models

from products.models import Products


class Feedback(models.Model):
    product = models.ForeignKey(
        Products, blank=True, on_delete=models.PROTECT, verbose_name="Отзыв о товаре"
    )
    title = models.CharField(max_length=100, blank=True, verbose_name="Название отзыва")
    description = models.TextField(
        max_length=1000, blank=True, verbose_name="Описание отзыва"
    )
    rating = models.IntegerField(default=0, verbose_name="Рейтинг")
    image = models.ImageField(
        upload_to="media/feedback/%Y/%m/%d", blank=True, verbose_name="Изображение"
    )
    created_at = models.DateField(
        auto_now_add=True, blank=True, null=True, verbose_name="Дата создания"
    )
    updated_at = models.DateField(
        auto_now=True, blank=True, null=True, verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["created_at"]

    def __str__(self):
        return self.title
