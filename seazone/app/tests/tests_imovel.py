from django.test import TestCase
from django.urls import reverse
from app.models import Imovel
from datetime import date
from rest_framework.test import APIClient
from rest_framework import status


class ImovelModelTestCase(TestCase):
    def setUp(self):
        Imovel.objects.create(
            limite_hospedes=6,
            quantidade_banheiros=2,
            aceita_animal_estimacao=True,
            valor_limpeza=100.00,
            data_ativacao=date.today()
        )

    def test_criacao_imovel(self):
        imovel = Imovel.objects.get(limite_hospedes=6)
        self.assertEqual(imovel.quantidade_banheiros, 2)
        self.assertTrue(imovel.aceita_animal_estimacao)
        self.assertEqual(imovel.valor_limpeza, 100.00)

    def test_campos_obrigatorios(self):
        imovel = Imovel.objects.get(limite_hospedes=6)
        self.assertIsNotNone(imovel.data_ativacao)
        self.assertIsNotNone(imovel.data_horario_criacao)


class ImovelListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Imovel.objects.create(
            limite_hospedes=6,
            quantidade_banheiros=2,
            aceita_animal_estimacao=True,
            valor_limpeza=100.00,
            data_ativacao='2023-01-01'
        )

    def test_listar_imoveis(self):
        url = reverse('imovel_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_criar_imovel(self):
        url = reverse('imovel_list')
        data = {
            'limite_hospedes': 8,
            'quantidade_banheiros': 3,
            'aceita_animal_estimacao': False,
            'valor_limpeza': 120.00,
            'data_ativacao': '2024-01-01'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Imovel.objects.count(), 2)
