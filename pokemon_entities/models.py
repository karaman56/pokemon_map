from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(
        verbose_name="Название (рус.)",
        max_length=200
    )
    title_en = models.CharField(
        verbose_name="Название (англ.)",
        max_length=200,
        blank=True
    )
    title_jp = models.CharField(
        verbose_name="Название (яп.)",
        max_length=200,
        blank=True
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to='pokemons',
        blank=True,
        null=True
    )
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name="Предыдущая эволюция",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolutions'
    )

    def __str__(self):
        return self.title_ru

    @property
    def next_evolution(self):
        return self.next_evolutions.first()


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Покемон',
        related_name='entities'
    )
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )
    appeared_at = models.DateTimeField(
        verbose_name='Время появления',
        blank=True,
        null=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name='Время исчезновения',
        blank=True,
        null=True
    )
    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень',
        blank=True,
        null=True
    )
    health = models.PositiveSmallIntegerField(
        verbose_name='Здоровье',
        blank=True,
        null=True
    )
    attack = models.PositiveSmallIntegerField(
        verbose_name='Атака',
        blank=True,
        null=True
    )
    protection = models.PositiveSmallIntegerField(
        verbose_name='Защита',
        blank=True,
        null=True
    )
    endurance = models.PositiveSmallIntegerField(
        verbose_name='Выносливость',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.pokemon.title_ru} ({self.latitude}, {self.longitude})'