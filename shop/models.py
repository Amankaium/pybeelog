from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование товара")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Информация о товаре")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    new_price = models.IntegerField(default=0, verbose_name="Новая цена")
    old_price = models.IntegerField(default=0, verbose_name="Старая цена")
    view_count = models.IntegerField(default=0, verbose_name="Число просмотров")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_available = models.BooleanField(default=True, verbose_name="Имеется в наличии")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'
        ordering = ['time_create']

class Review(models.Model):
        post = models.ForeignKey(
            "Product",
            on_delete=models.CASCADE,
            related_name="review",
        )
        author = models.CharField(max_length=255)
        data = models.DateTimeField(auto_now_add=True)
        email = models.EmailField()
        comment = models.TextField(max_length=3255)

