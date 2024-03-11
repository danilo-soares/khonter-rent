from rest_framework import serializers

from app.models import Imovel, Anuncio, Reserva


class AbstractSerializerMixin(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if not representation.get('data_horario_atualizacao'):
            representation.pop('data_horario_atualizacao')

        return representation


class AnuncioSerializer(AbstractSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = Anuncio
        fields = '__all__'


class ImovelSerializer(AbstractSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = Imovel
        fields = '__all__'


class ReservaSerializer(AbstractSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = Reserva
        fields = '__all__'
        read_only_fields = ('data_horario_atualizacao',)
