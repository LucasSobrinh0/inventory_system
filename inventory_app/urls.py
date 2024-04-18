from django.urls import path
from .views import listar_produtos, cadastrar_produto, editar_produto, remover_produto

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('editar/<int:pk>/', editar_produto, name='editar_produto'),
    path('remover/<int:pk>/', remover_produto, name='remover_produto'),
]
