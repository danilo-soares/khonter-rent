from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from app.models import Imovel
from app.serializers import ImovelSerializer


class ImovelListView(APIView):
    serializer_class = ImovelSerializer

    @staticmethod
    def get(request):
        imoveis = Imovel.objects.all()

        serializer = ImovelSerializer(
            imoveis,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = ImovelSerializer(data=self.request.data)

        Response({"message": "Imóvel Cadastrado"}, status=status.HTTP_200_OK)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "Imóvel Cadastrado"}, status=status.HTTP_200_OK)

        return Response(serializer, status=status.HTTP_404_NOT_FOUND)


class ImovelView(APIView):
    serializer_class = ImovelSerializer

    @staticmethod
    def get(request, id_imovel=None):
        try:
            serializer = ImovelSerializer(
                Imovel.objects.get(pk=id_imovel),
                many=False
            )

            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound("Imóvel não Encontrado")

    @staticmethod
    def put(request, id_imovel=None):
        imovel = Imovel.objects.get(pk=id_imovel)
        imovel.data_horario_atualizacao = timezone.now()

        serializer = ImovelSerializer(
            imovel,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Imóvel Atualizado"}, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, id_imovel=None):
        imovel = Imovel.objects.get(pk=id_imovel)
        imovel.delete()
        return Response({"message": "Imóvel Apagado"}, status=status.HTTP_200_OK)
