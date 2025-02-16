from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Pokemon, PokemonEntity

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'previous_evolution', 'image_display')
    list_filter = ('previous_evolution',)

    def image_display(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150" height="150" />')
        return "Изображение отсутствует"

    image_display.short_description = 'Фото'

@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = (
        'pokemon',
        'latitude',
        'longitude',
        'appeared_at',
        'disappeared_at',
        'level',
        'health',
        'attack',
        'protection',
        'endurance'
    )
