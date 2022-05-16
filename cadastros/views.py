from dataclasses import field
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Tipo_Despesa, Fornecedor, Despesa, Parcela

# Create your views here.

class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['nome', 'documento', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')


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
    success_url = reverse_lazy('listar-fornecedor')


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

####################################

class FornecedorDelete(DeleteView):
    model = Fornecedor
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-fornecedor')


class TipoDespesaDelete(DeleteView):
    model = Tipo_Despesa
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')


class DespesaDelete(DeleteView):
    model = Despesa
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')


#################################

class FornecedorList(ListView):
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedores.html'