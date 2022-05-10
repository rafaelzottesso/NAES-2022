from django.db import models


# Create your models here.
class Tipo_Despesa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, verbose_name="CPF ou CNPJ", unique=True)
    telefone = models.CharField(max_length=15)


class Despesa(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Tipo_Despesa, on_delete=models.PROTECT)
    descricao = models.TextField(verbose_name="Descrição", help_text="Utilize o espaço para descrever a despesa em detalhes.")
    data = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    desconto = models.DecimalField(decimal_places=2, max_digits=9)
    parcelas = models.IntegerField(verbose_name="Quantidade de parcelas")
    quitou = models.BooleanField(verbose_name="A despesa está completamente paga?")


class Parcela(models.Model):
    despesa = models.ForeignKey(Despesa, on_delete=models.PROTECT)
    numero = models.IntegerField(verbose_name="Nº da parcela")
    vencimento = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    desconto = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    juros = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    pago_em = models.DateField(null=True)
    valor_pago = models.DecimalField(decimal_places=2, max_digits=9, null=True)