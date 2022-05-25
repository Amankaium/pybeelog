from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование товара")
    content = models.TextField(blank=True, verbose_name="Информация о товаре")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_available = models.BooleanField(default=True, verbose_name="Имеется в наличии")

    def __str__(self):
        return self.title