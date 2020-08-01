from django.db import models


STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]


class Guestbook(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='Email автора')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active', verbose_name='Активно')

    def __str__(self):
        return f'{self.author} ({self.email})'

    class Meta:
        verbose_name = 'Гостевая книга'
        verbose_name_plural = 'Гостевые книги'
