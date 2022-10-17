from django import template

register = template.Library()


@register.filter(name="remover")
def remover(texto, r):
    return texto.replace(r, "")


@register.simple_tag(name="substituir")
def substituir(string, txt, subs, txt2="", subs2=""):
    novo = string.replace(txt, subs)
    
    if(txt2 != "" and subs2 != ""):
        novo = novo.replace(txt2, subs2)

    return novo


@register.filter(name="verificardddpr")
def verificardddpr(telefone):
    ddd = telefone[0:4]
    if(ddd == "(44)"):
        return True
    else:
        return False


@register.filter(name="esta_no_grupo")
def esta_no_grupo(usuario, nome_do_grupo):
    if(usuario.groups.filter(name=nome_do_grupo)):
        return True
    else:
        return False