from django.test import TestCase
from app.models import Anuncio, Imovel
from decimal import Decimal
from datetime import datetime
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class AnuncioMovelTestCase(TestCase):
    def setUp(self):
        imovel = Imovel.objects.create(
            limite_hospedes=6,
            quantidade_banheiros=2,
            aceita_animal_estimacao=True,
            valor_limpeza=100.00,
            data_ativacao=datetime.today()
        )
        Anuncio.objects.create(
            id_imovel=imovel,
            plataforma_publicada='Airbnb',
            taxa_plataforma=Decimal('5.00')
        )

    def test_criacao_anuncio(self):
        anuncio = Anuncio.objects.get(plataforma_publicada='Airbnb')
        self.assertEqual(anuncio.taxa_plataforma, Decimal('5.00'))

    def test_relacionamento_imovel(self):
        anuncio = Anuncio.objects.get(plataforma_publicada='Airbnb')
        self.assertEqual(anuncio.id_imovel.id_imovel, 1)


class AnuncioListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_listar_anuncios(self):
        imovel = Imovel.objects.create(
            limite_hospedes=6,
            quantidade_banheiros=2,
            aceita_animal_estimacao=True,
            valor_limpeza=100.00,
            data_ativacao=datetime.today()
        )

        Anuncio.objects.create(
            id_imovel=imovel,
            plataforma_publicada='Airbnb',
            taxa_plataforma=Decimal('5.00')
        )

        Anuncio.objects.create(
            id_imovel=imovel,
            plataforma_publicada='Booking',
            taxa_plataforma=Decimal('8.00')
        )

        url = reverse('anuncio_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_criar_anuncio(self):
        url = reverse('anuncio_list')

        imovel = Imovel.objects.create(
            limite_hospedes=2,
            quantidade_banheiros=1,
            aceita_animal_estimacao=True,
            valor_limpeza=100.00,
            data_ativacao=datetime.today()
        )

        data = {
            'id_imovel': imovel.id_imovel,
            'plataforma_publicada': 'Booking',
            'taxa_plataforma': '8.00',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Anuncio.objects.filter(plataforma_publicada='Booking').exists())
