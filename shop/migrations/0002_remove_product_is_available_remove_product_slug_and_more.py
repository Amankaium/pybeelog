# Generated by Django 4.0.4 on 2022-05-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_available',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='photos/products/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='new_price',
            field=models.IntegerField(verbose_name='Новая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(verbose_name='Старая цена'),
        ),
    ]
