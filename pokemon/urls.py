from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoViewSet, HabilidadViewSet, MovimientoViewSet, PokemonViewSet
from .views import PokemonListCreateView

router = DefaultRouter()
router.register(r'tipos', TipoViewSet)
router.register(r'habilidades', HabilidadViewSet)
router.register(r'movimientos', MovimientoViewSet)
router.register(r'pokemons', PokemonViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Quitamos el 'api/' porque ya viene del archivo principal
    path('pokemons/', PokemonListCreateView.as_view(), name='pokemon-list-create'),
]

