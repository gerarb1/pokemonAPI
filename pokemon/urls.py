from rest_framework import routers
from .api import TipoViewSet,HabilidadViewSet,MovimientoViewSet,PokemonViewSet

router = routers.DefaultRouter()

router.register('api/pokemon',PokemonViewSet,'pokemon')
router.register ('api/tipo',TipoViewSet, 'tipos')
router.register('api/habilidades',HabilidadViewSet,'habilidades')
router.register('api/movimientos',MovimientoViewSet,'movimientos')


urlpatterns = router.urls


