import email
from django.db import models
from distutils.command.upload import upload


class Feedback(models.Model):
    '''Форма обратной связи'''
    first_name = models.CharField('First Name', max_length=155)
    last_name = models.CharField('Last Name', max_length=155)
    email = models.EmailField('Your Email',
                              max_length=155, blank=True, null=True)
    phone = models.CharField('Your Phone', max_length=10)
    title = models.CharField('Your Subject', max_length=155)
    message = models.TextField('Your Message')

    checked = models.BooleanField('Checked', default=False)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Date')

    def __str__(self):
        return self.message[:20]

    class Meta:
        verbose_name = 'Форма обратной связь'
        verbose_name_plural = 'Формы обратной связи'


class OurContact(models.Model):
    '''Наши контакты'''
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name="Описание 1")
    description2 = models.CharField(max_length=255, blank=True, null=True,
                                    verbose_name="Описание 2")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наш контакт'
        verbose_name_plural = 'Наши контакты'


class Subscribe(models.Model):
    '''Подписка по email'''
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка по email'
        verbose_name_plural = 'Подписки по email'
