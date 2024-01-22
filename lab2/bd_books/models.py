from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    image = models.ImageField('Картинка книги', upload_to="photos")
    title = models.CharField('Название', max_length=50, default='')
    author = models.CharField('Автор книги', max_length=20, default='')
    description = models.TextField('Описание книги')
    price = models.IntegerField('Цена книги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'



class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Article, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Книга: {self.book.title}'