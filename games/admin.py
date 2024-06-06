from django.contrib import admin

from .models import GenreModel, GameModeModels, PlatformModels, GameModel, CartModel, OrderModel


@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    pass


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
