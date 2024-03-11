"""
URL configuration for seazone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views.views_anuncio import AnuncioListView, AnuncioView
from app.views.views_imovel import ImovelListView, ImovelView
from app.views.views_reserva import ReservaListView, ReservaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anuncio/', AnuncioListView.as_view(), name='anuncio_list'),
    path('anuncio/<id_anuncio>', AnuncioView.as_view(), name='anuncio'),
    path('imovel/', ImovelListView.as_view(), name='imovel_list'),
    path('imovel/<int:id_imovel>', ImovelView.as_view(), name='imovel'),
    path('reserva/', ReservaListView.as_view(), name='reserva_list'),
    path('<int:id_reserva>', ReservaView.as_view(), name='reserva'),
]
