# Generated by Django 4.0.4 on 2022-06-05 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('date_of_post', models.DateField(auto_now_add=True)),
                ('date_of_change', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='posts/%Y/%m/%d')),
                ('visits', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-id', '-date_of_post'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
    ]
