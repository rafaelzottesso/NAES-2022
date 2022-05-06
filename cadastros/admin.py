from django.contrib import admin
from .models import Tipo_Despesa, Despesa, Parcela, Fornecedor

# Register your models here.
admin.site.register(Tipo_Despesa)
admin.site.register(Despesa)
admin.site.register(Parcela)
admin.site.register(Fornecedor)