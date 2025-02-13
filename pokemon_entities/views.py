import folium
from django.shortcuts import render
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = 'https://example.com/default.png'


def add_pokemon(folium_map, lat, lon, image_url):
    icon = folium.features.CustomIcon(image_url, icon_size=(50, 50))
    folium.Marker([lat, lon], icon=icon).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons = Pokemon.objects.all()

    for pokemon in pokemons:
        entities = PokemonEntity.objects.filter(pokemon=pokemon)
        for entity in entities:
            img_url = pokemon.image.url if pokemon.image else DEFAULT_IMAGE_URL
            add_pokemon(folium_map, entity.latitude, entity.longitude, request.build_absolute_uri(img_url))

    return render(request, 'mainpage.html', {
        'map': folium_map._repr_html_(),
        'pokemons': pokemons,
    })


def show_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    entities = PokemonEntity.objects.filter(pokemon=pokemon)
    for entity in entities:
        img_url = pokemon.image.url if pokemon.image else DEFAULT_IMAGE_URL
        add_pokemon(folium_map, entity.latitude, entity.longitude, request.build_absolute_uri(img_url))

    return render(request, 'pokemon.html', {
        'map': folium_map._repr_html_(),
        'pokemon': pokemon,
    })
