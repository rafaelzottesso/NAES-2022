from dataclasses import field
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tipo_Despesa, Fornecedor, Despesa, Parcela

# Create your views here.

class FornecedorCreate(LoginRequiredMixin, CreateView):
    model = Fornecedor
    fields = ['nome', 'documento', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')
    # login_url = reverse_lazy('login')


class TipoDespesaCreate(LoginRequiredMixin, CreateView):
    model = Tipo_Despesa
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class DespesaCreate(LoginRequiredMixin, CreateView):
    model = Despesa
    fields = ['fornecedor', 'categoria', 'descricao', 'data', 'valor', 'desconto', 'parcelas', 'quitou']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


###################################


class FornecedorUpdate(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    fields = ['nome', 'documento', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')


class TipoDespesaUpdate(LoginRequiredMixin, UpdateView):
    model = Tipo_Despesa
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class DespesaUpdate(LoginRequiredMixin, UpdateView):
    model = Despesa
    fields = ['fornecedor', 'categoria', 'descricao',
              'data', 'valor', 'desconto', 'parcelas', 'quitou']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

####################################

class FornecedorDelete(LoginRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-fornecedor')


class TipoDespesaDelete(LoginRequiredMixin, DeleteView):
    model = Tipo_Despesa
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')


class DespesaDelete(LoginRequiredMixin, DeleteView):
    model = Despesa
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')


#################################

class FornecedorList(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedores.html'