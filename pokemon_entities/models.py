from django.db import models


class Pokemon(models.Model):
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='next_evolution',
        verbose_name="Предыдущая эволюция",
    )

    title_ru = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
    )
    title_en = models.CharField(
        max_length=200,
        verbose_name="Заголовок на английском",
        blank=True
    )
    title_ja = models.CharField(
        max_length=200,
        verbose_name="Заголовок на японском",
        blank=True
    )
    photo = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Картинка"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание",
        default=""
    )

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name="entities",
        verbose_name="Покемон",
    )

    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    appeared_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата и время появления",
    )
    disappeared_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата и время исчезновения"
    )

    lelvl = models.IntegerField(
        null=True,
        verbose_name="Уровень",
        blank=True,
    )
    health = models.IntegerField(
        null=True,
        verbose_name="Здоровье",
        blank=True,
    )
    attack = models.IntegerField(
        null=True,
        verbose_name="Сила атаки",
        blank=True,
    )
    orotection = models.IntegerField(
        null=True,
        verbose_name="Защита",
        blank=True,
    )
    endurance = models.IntegerField(
        null=True,
        verbose_name="Выносливость",
        blank=True,
    )

    def __str__(self):
        return f"{self.pokemon.title_ru} {self.pokemon.id}"
