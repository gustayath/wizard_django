from django.contrib import admin
from django.urls import path
from algo.views import (view_dados_pessoais, view_escolha_plano, view_finalizar_plano)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_dados_pessoais, name='dados_pessoais'),
    path('planos/', view_escolha_plano, name='planos'),
    path('finalizar/', view_finalizar_plano, name='finalizar_plano'),
]