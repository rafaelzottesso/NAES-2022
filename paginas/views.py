from django.views.generic import TemplateView


# Create your views here.
class PaginaInicialView(TemplateView):
    template_name = 'paginas/index.html'