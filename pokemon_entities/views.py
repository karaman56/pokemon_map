import folium
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = 'https://example.com/default.png'


def add_pokemon(folium_map, lat, lon, image_url):
    """Добавляет маркер покемона на карту"""
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50)
    )
    folium.Marker(
        [lat, lon],
        icon=icon
    ).add_to(folium_map)


def show_all_pokemons(request):
    """Отображает всех активных покемонов на карте"""
    current_time = timezone.localtime(timezone.now())
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    # Фильтр активных покемонов
    active_entities = PokemonEntity.objects.filter(
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    ).select_related('pokemon')

    # Добавление маркеров
    for entity in active_entities:
        img_url = (
            request.build_absolute_uri(entity.pokemon.image.url)
            if entity.pokemon.image
            else request.build_absolute_uri(DEFAULT_IMAGE_URL)
        )
        add_pokemon(folium_map, entity.latitude, entity.longitude, img_url)

    return render(request, 'mainpage.html', {
        'map': folium_map._repr_html_(),
        'pokemons': Pokemon.objects.all(),
    })


def show_pokemon(request, pokemon_id):
    current_time = timezone.localtime(timezone.now())
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    active_entities = PokemonEntity.objects.filter(
        pokemon=pokemon,
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in active_entities:
        img_url = (
            request.build_absolute_uri(pokemon.image.url)
            if pokemon.image
            else DEFAULT_IMAGE_URL
        )
        add_pokemon(folium_map, entity.latitude, entity.longitude, img_url)

    return render(request, 'pokemon.html', {
        'map': folium_map._repr_html_(),
        'pokemon': pokemon,  # Передаём объект, а не словарь
    })