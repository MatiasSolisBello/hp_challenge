# PokeApi Challenge

## Ejecución de proyecto

Crear entorno virtual.
```bash
virtualenv venv
source venv/bin/activate
```

Instalar paquetes necesarios
```bash
pip install -r requirements.txt
```

Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

Crear superusuario
```bash
python manage.py createsuperuser
```

Crear archivo .env dentro del folder "hp_challenge". Para este proyecto especifico se necesita:
```bash
POKEAPI_BASE_URL=https://pokeapi.co/api/v2/pokemon?limit=50&offset=0
SECRET_KEY=django-insecure-&bla%9bab(jn+s4m$=49s(_rl5oe3#icjt8^@=7=__u8jd0qvg
DEBUG=True
```

Ejecutar servidor
```bash
python manage.py runserver
```

## Docker
```bash
docker compose up --build
```

## Otros comandos
Verificar version de Python y Django respectivamente
```bash
python --version
python -m django --version
```

Cargar la base de datos con pokemones por comando personalizado o YAML:

```bash
python manage.py load_pokemon

python manage.py loaddata poke_data.yaml
```