from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from app.models import Reserva
from app.serializers import ReservaSerializer


class ReservaListView(APIView):
    serializer_class = ReservaSerializer

    @staticmethod
    def get(request):
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(
            reservas,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        if self.request.data['data_checkin'] > self.request.data['data_checkout']:
            return Response({"message": "Data de Checkin maior do que Checkout"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReservaSerializer(data=self.request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Reserva Cadastrada"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ReservaView(APIView):

    @staticmethod
    def get(request, id_reserva=None):
        try:
            serializer = ReservaSerializer(
                Reserva.objects.get(pk=id_reserva),
                many=False
            )
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound("Reserva não Encontrada")

    @staticmethod
    def delete(request, id_reserva=None):
        reserva = Reserva.objects.get(pk=id_reserva)
        reserva.delete()

        return Response({"message": "Reserva Apagada"}, status=status.HTTP_200_OK)
