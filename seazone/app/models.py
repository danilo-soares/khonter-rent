from django.db import models


class Imovel(models.Model):
    id_imovel = models.BigAutoField(primary_key=True)
    limite_hospedes = models.PositiveIntegerField(null=False)
    quantidade_banheiros = models.IntegerField(null=False)
    aceita_animal_estimacao = models.BooleanField(default=False)
    valor_limpeza = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    data_ativacao = models.DateField(null=False)
    data_horario_criacao = models.DateTimeField(auto_now_add=True, null=False)
    data_horario_atualizacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Anuncio(models.Model):
    id_anuncio = models.BigAutoField(primary_key=True)
    id_imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    plataforma_publicada = models.CharField(max_length=30, null=False)
    taxa_plataforma = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    data_horario_criacao = models.DateTimeField(auto_now_add=True, null=False)
    data_horario_atualizacao = models.DateTimeField(null=True, blank=True)


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    data_checkin = models.DateField(null=False)
    data_checkout = models.DateField(null=False)
    preco_total = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    comentario = models.TextField(null=True, max_length=255, default='')
    numero_hospedes = models.PositiveIntegerField(null=False)
    data_horario_criacao = models.DateTimeField(auto_now_add=True, null=False)
    data_horario_atualizacao = models.DateTimeField(null=True)