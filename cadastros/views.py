from dataclasses import field
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .models import Tipo_Despesa, Fornecedor, Despesa, Parcela

# Create your views here.

class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['nome', 'documento', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class TipoDespesaCreate(CreateView):
    model = Tipo_Despesa
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class DespesaCreate(CreateView):
    model = Despesa
    fields = ['fornecedor', 'categoria', 'descricao', 'data', 'valor', 'desconto', 'parcelas', 'quitou']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


###################################


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['nome', 'documento', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class TipoDespesaUpdate(UpdateView):
    model = Tipo_Despesa
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class DespesaUpdate(UpdateView):
    model = Despesa
    fields = ['fornecedor', 'categoria', 'descricao',
              'data', 'valor', 'desconto', 'parcelas', 'quitou']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
