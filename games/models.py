from django.db import models
import random
import string
from django.contrib.auth.models import User


class GenreModel(models.Model):
    title = models.CharField(max_length=130, verbose_name='Жанр', help_text='Тут надо указать жанр')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class GameModeModels(models.Model):
    title = models.CharField(max_length=130, verbose_name='Режим игры', help_text='Тут надо указать режим игры')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Режим игры'
        verbose_name_plural = 'Режим игры'


class PlatformModels(models.Model):
    title = models.CharField(max_length=130, verbose_name='Платформа', help_text='Тут надо указать тип платформ')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'


class GameModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', help_text='Тут надо указать название игры')
    price = models.FloatField(verbose_name='Цена')
    sale_price = models.FloatField(verbose_name='Скидочная цена', null=True, blank=True)
    description = models.TextField(verbose_name='Описания')
    count = models.IntegerField(verbose_name='Кол-во')
    image = models.FileField(upload_to='game_images', verbose_name='Изображения')
    genre = models.ForeignKey(GenreModel, on_delete=models.CASCADE)
    game_mode = models.ForeignKey(GameModeModels, on_delete=models.CASCADE)
    platform = models.ForeignKey(PlatformModels, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.game.title} (x{self.quantity})"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unique_keys = models.JSONField(default=list)  # Use JSONField to store list of unique keys
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.unique_keys:
            self.unique_keys = [self.generate_unique_key() for _ in range(self.quantity)]
        super().save(*args, **kwargs)

    def generate_unique_key(self):
        return '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(3))

    def __str__(self):
        return f"Order {self.unique_keys} by {self.user.username}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
