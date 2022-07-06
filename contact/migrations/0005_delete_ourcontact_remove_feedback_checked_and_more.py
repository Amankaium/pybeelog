# Generated by Django 4.0.4 on 2022-06-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contact', '0004_alter_subscribe_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OurContact',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='checked',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default=None, max_length=155, verbose_name='Your Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.IntegerField(max_length=10, verbose_name='Your Phone'),
        ),
    ]
