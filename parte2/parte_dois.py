import ast 
import time
class Pessoa:
    def __init__(self,nome,idade,quarto,preco,acompanhantes):
        self.nome = nome
        self.idade = idade
        self.quarto = quarto
        self.preco = preco
        self.acompanhantes = acompanhantes
    def present(self):
        print(f'meu nome é {self.nome},tenho {self.idade} anos e estou no quarto {self.quarto}')
def cria_lista(arq):
    lista = []
    with open(arq,"r",encoding ="utf8" ) as arquivo:
        for i in arquivo:
            dados = ast.literal_eval(i.strip())
            #print(dados)
            nome =  dados[0]
            idade = int(dados[1])
            quarto = int(dados[2])
            preco = float(dados[3])
            acompanhantes = dados[4]
            lista.append(Pessoa(nome,idade,quarto,preco,acompanhantes))
    return lista

inicio =  time.time()
lista_grande = cria_lista("grande.txt")
fim = time.time()
print(fim-inicio)

inicio =  time.time()
lista_media = cria_lista("medio.txt")
fim = time.time()
print(fim-inicio)

inicio =  time.time()
lista_pequena = cria_lista("pequeno.txt")
fim = time.time()
print(fim-inicio)

inicio =  time.time()
lista_muito_grande = cria_lista("muito_grande.txt")
fim = time.time()
print(fim-inicio)