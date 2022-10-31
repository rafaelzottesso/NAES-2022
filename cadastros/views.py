from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tipo_Despesa, Fornecedor, Despesa, Parcela

from django.shortcuts import get_object_or_404

import datetime
# Para somar meses a uma data
from dateutil.relativedelta import relativedelta

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

        # Para cada parcela, cria um objeto Parcela
        try:
            valor_parcela = self.object.valor / self.object.parcelas
            
            for i in range( self.object.parcelas ):
                mes_parcela = relativedelta(months=i)
                
                parcela = Parcela.objects.create(
                    despesa=self.object,
                    numero=i+1,
                    vencimento=self.object.data + mes_parcela,
                    valor=valor_parcela,
                )

                if(self.object.quitou):
                    parcela.pago_em = parcela.vencimento
                    parcela.valor_pago = valor_parcela
                    parcela.save()

        except:
            self.object.delete()
            form.add_error(None, "Houve um problema. Tente novamente!")
            return self.form_invalid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)

        dados["form"].fields["fornecedor"].queryset = Fornecedor.objects.filter(usuario=self.request.user)
        dados["form"].fields["categoria"].queryset = Tipo_Despesa.objects.filter(usuario=self.request.user)

        return dados


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

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)

        dados["form"].fields["fornecedor"].queryset = Fornecedor.objects.filter(usuario=self.request.user)
        dados["form"].fields["categoria"].queryset = Tipo_Despesa.objects.filter(usuario=self.request.user)

        return dados

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
        self.object_list = Despesa.objects.filter(usuario=self.request.user).select_related('fornecedor', 'categoria')
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
    template_name = 'cadastros/listas/parcelas.html'
    paginate_by = 10

    def get_queryset(self):
        self.object_list = Parcela.objects.filter(
                despesa__usuario=self.request.user
            ).order_by('vencimento').select_related('despesa', 'despesa__fornecedor')
        return self.object_list


class ParcelaVencidaList(LoginRequiredMixin, ListView):
    model = Parcela
    template_name = 'cadastros/listas/parcelas.html'

    def get_queryset(self):
        self.object_list = Parcela.objects.filter(
            despesa__usuario=self.request.user,
            valor_pago__isnull=True,
            pago_em__isnull=True,
            vencimento__lt=datetime.datetime.today()
        ).select_related('despesa', 'despesa__fornecedor', 'despesa__fornecedor__cidade')
        return self.object_list


class ParcelaPagaList(LoginRequiredMixin, ListView):
    model = Parcela
    template_name = 'cadastros/listas/parcelas.html'

    def get_queryset(self):
        self.object_list = Parcela.objects.filter(
            despesa__usuario=self.request.user,
            valor_pago__isnull=False,
            pago_em__isnull=False
        )
        return self.object_list
