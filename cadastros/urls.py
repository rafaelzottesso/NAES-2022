from django.urls import path

from .views import FornecedorCreate, DespesaCreate, TipoDespesaCreate
from .views import FornecedorUpdate, DespesaUpdate, TipoDespesaUpdate

urlpatterns = [
    path('cadastrar/fornecedor/', FornecedorCreate.as_view(), name='cadastrar-fornecedor'),
    path('cadastrar/despesa/', DespesaCreate.as_view(), name='cadastrar-despesa'),
    path('cadastrar/tipo-despesa/', TipoDespesaCreate.as_view(), name='cadastrar-tipo-despesa'),

    path('editar/fornecedor/<int:pk>/', FornecedorUpdate.as_view(), name='editar-fornecedor'),
    path('editar/despesa/<int:pk>/', DespesaUpdate.as_view(), name='editar-despesa'),
    path('editar/tipo-despesa/<int:pk>/', TipoDespesaUpdate.as_view(),name='editar-tipo-despesa'),
]
