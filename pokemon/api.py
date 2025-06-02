from .models import Pokemon,Tipo,Habilidad,Movimiento
from rest_framework import viewsets, permissions
from .serializers import PokemonSerializer,TipoSerializer,HabilidadSerializer,MovimientoSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
    permissions_classes = [permissions.AllowAny]

class HabilidadViewSet(viewsets.ModelViewSet):
    queryset = Habilidad.objects.all()
    serializer_class = HabilidadSerializer
    permissions_classes = [permissions.AllowAny]

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    permissions_classes = [permissions.AllowAny]

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permissions_classes = [permissions.AllowAny]
    