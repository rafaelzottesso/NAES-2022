from django.urls import path

from .views import FornecedorCreate, DespesaCreate, TipoDespesaCreate
from .views import FornecedorUpdate, DespesaUpdate, TipoDespesaUpdate
from .views import FornecedorDelete, DespesaDelete, TipoDespesaDelete
from .views import FornecedorList, DespesaList, TipoDespesaList, ParcelaList, ParcelaVencidaList, ParcelaPagaList

urlpatterns = [
    path('cadastrar/fornecedor/', FornecedorCreate.as_view(), name='cadastrar-fornecedor'),
    path('cadastrar/despesa/', DespesaCreate.as_view(), name='cadastrar-despesa'),
    path('cadastrar/tipo-despesa/', TipoDespesaCreate.as_view(), name='cadastrar-tipo-despesa'),

    path('editar/fornecedor/<int:pk>/', FornecedorUpdate.as_view(), name='editar-fornecedor'),
    path('editar/despesa/<int:pk>/', DespesaUpdate.as_view(), name='editar-despesa'),
    path('editar/tipo-despesa/<int:pk>/', TipoDespesaUpdate.as_view(),name='editar-tipo-despesa'),
    
    path('excluir/fornecedor/<int:pk>/', FornecedorDelete.as_view(), name='excluir-fornecedor'),
    path('excluir/despesa/<int:pk>/', DespesaDelete.as_view(), name='excluir-despesa'),
    path('excluir/tipo-despesa/<int:pk>/', TipoDespesaDelete.as_view(),name='excluir-tipo-despesa'),

    path('listar/fornecedores/', FornecedorList.as_view(), name='listar-fornecedor'),
    path('listar/despesas/', DespesaList.as_view(), name='listar-despesa'),
    path('listar/tipos-despesa/', TipoDespesaList.as_view(), name='listar-tipo-despesa'),
    path('listar/parcelas/', ParcelaList.as_view(), name='listar-parcela'),
    path('listar/parcelas/vencidas/', ParcelaVencidaList.as_view(), name='listar-parcela-vencida'),
    path('listar/parcelas/quitadas/', ParcelaPagaList.as_view(), name='listar-parcela-paga'),

    
]
