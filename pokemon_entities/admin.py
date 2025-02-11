from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_display')  # Отображаем название и изображение
    readonly_fields = ('image_display',)  # Делаем поле только для чтения

    def image_display(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="150" />')
        return "Изображение отсутствует"

    image_display.short_description = 'Фото'  # Заголовок для колонки