from django.shortcuts import render
from rest_framework import viewsets
from .models import Tipo, Habilidad, Movimiento, Pokemon
from .serializers import TipoSerializer, HabilidadSerializer, MovimientoSerializer, PokemonSerializer
from rest_framework import generics

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class HabilidadViewSet(viewsets.ModelViewSet):
    queryset = Habilidad.objects.all()
    serializer_class = HabilidadSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
class PokemonListCreateView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
# Create your views here.
