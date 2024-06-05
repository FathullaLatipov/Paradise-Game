# Generated by Django 5.0.6 on 2024-06-05 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Тут надо указать название игры', max_length=200, verbose_name='Название')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('sale_price', models.FloatField(blank=True, null=True, verbose_name='Скидочная цена')),
                ('description', models.TextField(verbose_name='Описания')),
                ('count', models.IntegerField(verbose_name='Кол-во')),
                ('image', models.FileField(upload_to='game_images', verbose_name='Изображения')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('game_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.gamemodemodels')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.genremodel')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.platformmodels')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
    ]
