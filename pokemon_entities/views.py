import dataclasses

import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render
from numpy import number

from pokemon_entities.models import PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


@dataclasses.dataclass(frozen=True)
class Pokemon:
    pokemon_id: int
    img_url: str
    title_ru: str


def get_pokemon_img_url(request, pokemon):
    if pokemon.photo:
        return request.build_absolute_uri(pokemon.photo.url)
    else:
        return DEFAULT_IMAGE_URL


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        add_pokemon(
            folium_map, pokemon.latitude,
            pokemon.longitude,
            get_pokemon_img_url(request, pokemon.pokemon)
        )
    pokemons_on_page = set()

    for pokemon in pokemons:
        pokemon = Pokemon(
            pokemon.pokemon.id,
            get_pokemon_img_url(request, pokemon.pokemon),
            pokemon.pokemon.title_ru
        )
        pokemons_on_page.add(pokemon)

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemons = PokemonEntity.objects.filter(pokemon__id=pokemon_id)

    if pokemons[0].pokemon.id == int(pokemon_id):
        requested_pokemons = pokemons
        print(dir(pokemons[0]))
        requested_pokemon = pokemons[0].pokemon
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in requested_pokemons:
        add_pokemon(
            folium_map, pokemon.latitude,
            pokemon.longitude,
            get_pokemon_img_url(request, pokemon.pokemon)
        )

    pokemon = {
        'img_url': get_pokemon_img_url(request, pokemon.pokemon),
        'title_ru': requested_pokemon.title_ru,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_ja,
        'description': requested_pokemon.description,
    }
    if requested_pokemon.previous_evolution:
        previous_pokemon = requested_pokemon.previous_evolution
        pokemon["previous_evolution"] = {
            "title_ru": previous_pokemon,
            "pokemon_id": previous_pokemon.id,
            "img_url": get_pokemon_img_url(request, previous_pokemon)
        }
    if requested_pokemon.next_evolution.first():
        next_pokemon = requested_pokemon.next_evolution.first()
        pokemon["next_evolution"] = {
            "title_ru": next_pokemon,
            "pokemon_id": next_pokemon.id,
            "img_url": get_pokemon_img_url(request, next_pokemon)
        }
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
