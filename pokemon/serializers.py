from rest_framework import serializers
from .models import Tipo, Habilidad, Movimiento, Pokemon

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'nombre',  'created_at',)
        read_only_fields = ('created_at', )

class HabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidad
        fields = ('id' , 'nombre' , 'efecto' , 'created_at',)
        read_only_fields = ('created_at', )

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = ('id', 'nombre', 'tipo', 'poder', 'precision', 'created_at',)
        read_only_fields = ('created_at', )

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'nombre', 'tipos','descripcion', 'habilidades', 'movimientos', 'created_at',)
        read_only_fields = ('created_at', )


