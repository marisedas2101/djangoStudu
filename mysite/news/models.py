from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', related_name='get_news')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    # сюда редиректится после добавления новости на сайте
    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    # описательный класс
    class Meta:
        # название в единственном числе
        verbose_name = 'Новость'
        # название во множественном числе
        verbose_name_plural = 'Новости'
        # правило сортировки (можно несколько полей для сортировки)
        # знак - перед названием поля - сортировка в обратном порядке
        ordering = ['-created_at']


class Category(models.Model):
    # db_index - индексирует поле title
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        # название в единственном числе
        verbose_name = 'Категория'
        # название во множественном числе
        verbose_name_plural = 'Категории'
        ordering = ['title']
