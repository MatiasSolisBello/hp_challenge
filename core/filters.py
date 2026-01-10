import django_filters

from core.models import Pokemon


class PokemonFilter(django_filters.FilterSet):
    weight_range = django_filters.BooleanFilter(
        method="filter_weight_range",
        label="Peso entre 30 y 80"
    )

    grass_type = django_filters.BooleanFilter(
        method="filter_grass_type",
        label="Tipo grass"
    )

    flying_tall = django_filters.BooleanFilter(
        method="filter_flying_tall",
        label="Tipo flying y altura > 10"
    )

    class Meta:
        model = Pokemon
        fields = []
        
    def filter_weight_range(self, queryset, name, value):
        data = queryset.filter(
            weight__gt=30,
            weight__lt=80
        )
        return data

    def filter_grass_type(self, queryset, name, value):
        return queryset.filter(
            types__icontains='"grass"'
        )

    def filter_flying_tall(self, queryset, name, value):
        return queryset.filter(
            types__icontains='"flying"',
            height__gt=10
        )