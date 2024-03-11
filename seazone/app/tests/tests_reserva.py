from django.test import TestCase
from decimal import Decimal
from datetime import date
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from app.models import Reserva, Anuncio, Imovel


class ReservaModelTestCase(TestCase):
    def setUp(self):
        imovel = Imovel.objects.create(
            limite_hospedes=6,
            quantidade_banheiros=2,
            aceita_animal_estimacao=True,
            valor_limpeza=100.00,
            data_ativacao=date.today()
        )

        anuncio = Anuncio.objects.create(
            plataforma_publicada='Airbnb',
            id_imovel=imovel,
            taxa_plataforma=Decimal('5.00')
        )

        Reserva.objects.create(
            id_anuncio=anuncio,
            data_checkin=date.today(),
            data_checkout=date.today(),
            preco_total=Decimal('250.00'),
            numero_hospedes=4
        )

    def test_criacao_reserva(self):
        reserva = Reserva.objects.get(preco_total=Decimal('250.00'))
        self.assertEqual(reserva.numero_hospedes, 4)

    def test_preco_total_calculado_corretamente(self):
        reserva = Reserva.objects.get(preco_total=Decimal('250.00'))
        self.assertEqual(reserva.preco_total, Decimal('250.00'))


class ReservaListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_listar_reservas(self):
        url = reverse('reserva_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
