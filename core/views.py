from django.shortcuts import render
from django.views import View

from core.models import Pokemon

# Create your views here.
class IndexView(View):
    def get(self, request):
        data = Pokemon.objects.all()
        return render(request, 'core/index.html', {'data': data})