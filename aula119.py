# *args (ilimitado de arqumentos posicionais)
# **kwargs(ilimitado de argumentos nomeados)
# tudo que vem antes da barra deve ser pocisional
#_______________________________________________
#Keyword- Only- Arguments (*) -> * sozinho (sem a palavra args)
#NÃO SUGA os valores para a tupla
def soma(a, b, *, c):
    print(a + b+ c)
soma(1,2,c=3)
    