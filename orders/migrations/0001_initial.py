# Generated by Django 4.2.11 on 2024-04-19 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_shop_image'),
        ('products', '0003_alter_products_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Статус заказа')),
                ('html_color', models.CharField(blank=True, max_length=7, verbose_name='Цвет заказа')),
            ],
            options={
                'verbose_name': 'Статус заказа',
                'verbose_name_plural': 'Статус заказа',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='OrderCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, verbose_name='Количество товаров')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('delivery_date', models.DateField(blank=True, null=True, verbose_name='Дата доставки')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.products', verbose_name='Товар')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.shop', verbose_name='Магазин')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='orders.orderstatus', verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name': 'Цена на товар',
                'verbose_name_plural': 'Цена на товар',
                'ordering': ['created_at'],
            },
        ),
    ]
