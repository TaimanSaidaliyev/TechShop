from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название роли')
    slug = models.CharField(max_length=100, blank=True, verbose_name='Техническое имя')

    class Meta:
        verbose_name = 'Роли'
        verbose_name_plural = 'Роли'
        ordering = ['title']

    def __str__(self):
        return self.title


class Person(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Пользователь')
    telephone = models.CharField(max_length=100, blank=True, verbose_name='Телефон')
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Роль')

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персона'
        ordering = ['user']

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
