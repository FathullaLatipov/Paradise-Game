# Generated by Django 5.0.6 on 2024-06-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_remove_ordermodel_unique_key_ordermodel_unique_keys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamemodel',
            name='game_mode',
        ),
        migrations.RemoveField(
            model_name='gamemodel',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='gamemodel',
            name='platform',
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='game_mode',
            field=models.ManyToManyField(to='games.gamemodemodels'),
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='genre',
            field=models.ManyToManyField(to='games.genremodel'),
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='platform',
            field=models.ManyToManyField(to='games.platformmodels'),
        ),
    ]