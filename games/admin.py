from django.contrib import admin

from .models import GenreModel, GameModeModels, PlatformModels, GameModel


@admin.register(GenreModel)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'updated_at', 'created_at']


@admin.register(GameModeModels)
class GameModeModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'updated_at', 'created_at']


@admin.register(PlatformModels)
class PlatformModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'updated_at', 'created_at']


@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'updated_at', 'created_at']
