# Generated by Django 4.0.5 on 2022-06-20 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_feedback_message_en_feedback_message_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='first_name_en',
            field=models.CharField(max_length=155, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='first_name_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='First Name'),
        ),
    ]
