# Generated by Django 4.0.4 on 2022-06-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_options_alter_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Информация о товаре'),
        ),
        migrations.AddField(
            model_name='product',
            name='content_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Информация о товаре'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование товара'),
        ),
    ]