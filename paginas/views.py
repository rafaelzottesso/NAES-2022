from django.views.generic import TemplateView
from cadastros.models import Parcela

# Create your views here.
class PaginaInicialView(TemplateView):
    template_name = 'paginas/index.html'

    # de uma maneira geral, envia dados para o template html
    def get_context_data(self, *args, **kwargs):
        # Executa da classe pai para ter dados padrão
        dados = super().get_context_data(*args, **kwargs)

        # Cria um dado na posição teste
        dados["teste"] = "Bem vindo ao sistema"
    
        # Verifica se o usuário está logado
        if(self.request.user.is_authenticated):
            # Cria a posição parcelas_vencidas com uma contagem de parcela que não foram pagas
            dados["parcelas_vencidas"] = Parcela.objects.filter(
                    despesa__usuario=self.request.user, 
                    pago_em__isnull=True
                ).count()
       
        return dados
