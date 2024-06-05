from django.db import models


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


