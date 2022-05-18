from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    content = models.TextField(blank=True, verbose_name='content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated_at')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='foto', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='is_published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category',
                                 )
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})


    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'All news'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Name category')

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'All category'
        ordering = ['title']


