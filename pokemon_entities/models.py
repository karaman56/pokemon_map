from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemons/', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    """ уже создал ForeignKey1 """
    appeared_at = models.DateTimeField(verbose_name='Время появления', blank=True, null=True)
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения', blank=True, null=True)

    def __str__(self):
        return f'{self.pokemon.title} ({self.latitude}, {self.longitude})'