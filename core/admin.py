from django.contrib import admin

from core.models import Pokemon

# Register your models here.
admin.site.register(Pokemon)  # Add your models inside the parentheses to register them with the admin site.
