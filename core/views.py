from django_filters.views import FilterView

from core.filters import PokemonFilter
from core.models import Pokemon

# Create your views here.
class IndexView(FilterView):
    model = Pokemon
    template_name = 'core/index.html'
    filterset_class = PokemonFilter
    
    def get_queryset(self):
        queryset = Pokemon.objects.all()

        self.filterset = self.filterset_class(self.request.GET, 
                                              queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        queryset = self.get_queryset()
         
        context['data'] = queryset
        context['filter'] = self.filterset_class(self.request.GET, 
                                                 queryset=queryset)
        return context