from rest_framework import serializers
from .models import Tipo, Habilidad, Movimiento, Pokemon

from rest_framework import serializers
from .models import Tipo, Habilidad, Movimiento, Pokemon

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class HabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidad
        fields = '__all__'

class MovimientoSerializer(serializers.ModelSerializer):
    tipo = TipoSerializer(read_only=True)

    class Meta:
        model = Movimiento
        fields = '__all__'

class PokemonSerializer(serializers.ModelSerializer):
    tipos = TipoSerializer(many=True, read_only=True)
    habilidades = HabilidadSerializer(many=True, read_only=True)
    movimientos = MovimientoSerializer(many=True, read_only=True)
    evolucion = serializers.StringRelatedField(read_only=True)

    tipo_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tipo.objects.all(), many=True, write_only=True
    )
    habilidad_ids = serializers.PrimaryKeyRelatedField(
        queryset=Habilidad.objects.all(), many=True, write_only=True
    )
    movimiento_ids = serializers.PrimaryKeyRelatedField(
        queryset=Movimiento.objects.all(), many=True, write_only=True
    )
    evolucion_id = serializers.PrimaryKeyRelatedField(
        queryset=Pokemon.objects.all(), required=False, allow_null=True, write_only=True
    )

    class Meta:
        model = Pokemon
        fields = [
            'id', 'nombre', 'tipos', 'habilidades', 'movimientos', 'evolucion',
            'tipo_ids', 'habilidad_ids', 'movimiento_ids', 'evolucion_id'
        ]

    def create(self, validated_data):
        tipo_ids = validated_data.pop('tipo_ids')
        habilidad_ids = validated_data.pop('habilidad_ids')
        movimiento_ids = validated_data.pop('movimiento_ids')
        evolucion = validated_data.pop('evolucion_id', None)

        pokemon = Pokemon.objects.create(evolucion=evolucion, **validated_data)
        pokemon.tipos.set(tipo_ids)
        pokemon.habilidades.set(habilidad_ids)
        pokemon.movimientos.set(movimiento_ids)
        return pokemon


