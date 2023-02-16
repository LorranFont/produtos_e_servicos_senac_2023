from django.urls import path
from .views import listagem_produtos, detalhamento_produto, cadastro_produto, excluir_produto, alterar_produto, listagem_servicos

urlpatterns = [
    path('', listagem_produtos),
    path('<int:id>', detalhamento_produto),
    path('cadastrar', cadastro_produto),
    path('<int:id>/alterar', alterar_produto),
    path('<int:id>/excluir', excluir_produto)
]