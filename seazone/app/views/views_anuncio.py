from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from app.models import Anuncio
from app.serializers import AnuncioSerializer


class AnuncioListView(APIView):
    serializer_class = AnuncioSerializer

    @staticmethod
    def get(request):
        anuncios = Anuncio.objects.all()
        serializer = AnuncioSerializer(
            anuncios,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = AnuncioSerializer(data=self.request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Anúncio Cadastrado"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class AnuncioView(APIView):
    serializer_class = AnuncioSerializer

    @staticmethod
    def get(request, id_anuncio=None):
        try:
            serializer = AnuncioSerializer(
                Anuncio.objects.get(pk=id_anuncio),
                many=False
            )
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound("Imóvel não Encontrado")

    @staticmethod
    def put(request, id_anuncio=None):
        anuncio = Anuncio.objects.get(pk=id_anuncio)
        anuncio.data_horario_atualizacao = timezone.now()
        serializer = AnuncioSerializer(
            anuncio,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Anúncio Atualizado"}, status=status.HTTP_200_OK)
