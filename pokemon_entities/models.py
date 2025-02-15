from django.db import models

# pokemon_entities/models.py
from django.db import models

class Pokemon(models.Model):
    title_ru = models.CharField("Название (рус.)", max_length=200)
    title_en = models.CharField("Название (англ.)", max_length=200, blank=True)
    title_jp = models.CharField("Название (яп.)", max_length=200, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to='pokemons', blank=True, null=True)
    """Ранее добавил возможность описани яна трех языках"""


    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    """ уже создал ForeignKey1 """
    appeared_at = models.DateTimeField(verbose_name='Время появления', blank=True, null=True)
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения', blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    protection = models.IntegerField(blank=True, null=True)
    endurance = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon.title_ru} ({self.latitude}, {self.longitude})'
