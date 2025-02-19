from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Pokemon, PokemonEntity


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        'title_ru',
        'previous_evolution_display',
        'next_evolution_display',
        'image_preview'
    )
    list_filter = ('previous_evolution',)
    search_fields = ('title_ru', 'title_en')

    def previous_evolution_display(self, obj):
        if obj.previous_evolution:
            return mark_safe(
                f'<a href="/admin/pokemon_entities/pokemon/{obj.previous_evolution.id}/change/">'
                f'{obj.previous_evolution.title_ru}</a>'
            )
        return "-"

    def next_evolution_display(self, obj):
        if obj.next_evolution:
            return mark_safe(
                f'<a href="/admin/pokemon_entities/pokemon/{obj.next_evolution.id}/change/">'
                f'{obj.next_evolution.title_ru}</a>'
            )
        return "-"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px; object-fit: contain"/>'
            )
        return "🖼️ Изображение отсутствует"

    previous_evolution_display.short_description = "Предыдущая эволюция"
    next_evolution_display.short_description = "Следующая эволюция"
    image_preview.short_description = "Превью"


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = (
        'pokemon_link',
        'coordinates',
        'time_period',
        'level',
        'health',
        'attack',
        'protection',
        'endurance'
    )
    list_filter = ('pokemon__title_ru', 'level')
    search_fields = ('pokemon__title_ru',)

    def pokemon_link(self, obj):
        return mark_safe(
            f'<a href="/admin/pokemon_entities/pokemon/{obj.pokemon.id}/change/">'
            f'{obj.pokemon.title_ru}</a>'
        )

    def coordinates(self, obj):
        return f"{obj.latitude:.5f}, {obj.longitude:.5f}"

    def time_period(self, obj):
        return f"{obj.appeared_at:%H:%M} – {obj.disappeared_at:%H:%M}"

    pokemon_link.short_description = "Покемон"
    coordinates.short_description = "Координаты"
    time_period.short_description = "Время активности"