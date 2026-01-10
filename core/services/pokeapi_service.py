import logging
import requests

from core.models import Pokemon
from hp_challenge.settings import POKEAPI_BASE_URL

class PokeAPIService:
    def load_pokemons():
        try:
            # Obtener los primeros 50 Pokémon desde la PokeAPI
            url = POKEAPI_BASE_URL      
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            logging.error(f"Error al obtener datos de la PokeAPI: {e}")
            return

        for i in data['results']:
            response = requests.get(i['url'])
            data = response.json()
                        
            try:
                Pokemon.objects.update_or_create(
                    id=data['id'],
                    name=data['name'],
                    types=[t['type']['name'] for t in data['types']],
                    height=data['height'],
                    weight=data['weight'],
                    reversed_name=data['name'][::-1]
                )
            except Exception as e:
                logging.error(f"Error al guardar Pokémon: {e}")