from django.core.management.base import BaseCommand, CommandError

from core.services.pokeapi_service import PokeAPIService


class Command(BaseCommand):
    help = "Carga los primeros Pokémon desde la PokeAPI"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE(f"Cargando Pokemones..."))
        try:
            PokeAPIService.load_pokemons()
        except Exception as exc:
            raise CommandError(f"Error cargando Pokemon: {exc}")

        self.stdout.write(
            self.style.SUCCESS(f"EXITO: Pokemones cargados correctamente")
        )
