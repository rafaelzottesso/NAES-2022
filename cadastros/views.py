from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tipo_Despesa, Fornecedor, Despesa, Parcela

from django.shortcuts import get_object_or_404


# Create your views here.

class FornecedorCreate(LoginRequiredMixin, CreateView):
    model = Fornecedor
    fields = ['nome', 'documento', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')
    # login_url = reverse_lazy('login')

    def form_valid(self, form):

        # Antes do super, não existe objeto. Estamos trabalhando
        # com os dados do formuláio
        form.instance.usuario = self.request.user
        
        # Valida os dados e da um INSERT no banco
        url = super().form_valid(form)

        # neste ponto, existe o objeto que foi criado no banco relacional
        # self.object.codigo = hash(self.object.pk)
        # self.object.save()

        return url


class TipoDespesaCreate(LoginRequiredMixin, CreateView):
    model = Tipo_Despesa
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo-despesa')

    def form_valid(self, form):

        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url


class DespesaCreate(LoginRequiredMixin, CreateView):
    model = Despesa
    fields = ['fornecedor', 'categoria', 'descricao', 'data', 'valor', 'desconto', 'parcelas', 'quitou']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')

    def form_valid(self, form):

        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url


###################################


class FornecedorUpdate(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    fields = ['nome', 'documento', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedor')

    def get_object(self):
        self.object = get_object_or_404(
                            Fornecedor,
                            usuario=self.request.user,
                            pk=self.kwargs['pk']
                        )
        return self.object


class TipoDespesaUpdate(LoginRequiredMixin, UpdateView):
    model = Tipo_Despesa
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo-despesa')

    def get_object(self):
        self.object = get_object_or_404(
            Tipo_Despesa,
            usuario=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object


class DespesaUpdate(LoginRequiredMixin, UpdateView):
    model = Despesa
    fields = ['fornecedor', 'categoria', 'descricao',
              'data', 'valor', 'desconto', 'parcelas', 'quitou']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')

    def get_object(self):
        self.object = get_object_or_404(
            Despesa,
            usuario=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object

####################################

class FornecedorDelete(LoginRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-fornecedor')

    def get_object(self):
        self.object = get_object_or_404(
            Fornecedor,
            usuario=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object


class TipoDespesaDelete(LoginRequiredMixin, DeleteView):
    model = Tipo_Despesa
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-tipo-despesa')

    def get_object(self):
        self.object = get_object_or_404(
            Tipo_Despesa,
            usuario=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object


class DespesaDelete(LoginRequiredMixin, DeleteView):
    model = Despesa
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('listar-despesa')

    def get_object(self):
        self.object = get_object_or_404(
            Despesa,
            usuario=self.request.user,
            pk=self.kwargs['pk']
        )
        return self.object


#################################

class FornecedorList(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedores.html'

    # Modifica a query padrão de select que vai no banco
    def get_queryset(self):
        # armazena a lista e retorna ela
        self.object_list = Fornecedor.objects.filter(usuario=self.request.user)
        return self.object_list


class DespesaList(LoginRequiredMixin, ListView):
    model = Despesa
    template_name = 'cadastros/listas/despesas.html'

    # Modifica a query padrão de select que vai no banco
    def get_queryset(self):
        # armazena a lista e retorna ela
        self.object_list = Despesa.objects.filter(usuario=self.request.user)
        return self.object_list


class TipoDespesaList(LoginRequiredMixin, ListView):
    model = Tipo_Despesa
    template_name = 'cadastros/listas/tipos-despesa.html'

    # Modifica a query padrão de select que vai no banco
    def get_queryset(self):
        # armazena a lista e retorna ela
        self.object_list = Tipo_Despesa.objects.filter(usuario=self.request.user)
        return self.object_list


class ParcelaList(LoginRequiredMixin, ListView):
    model = Parcela
    template_name = 'cadastros/listas/parcela.html'

    def get_queryset(self):
        self.object_list = Parcela.objects.filter(despesa__usuario=self.request.user)
        return self.object_list
