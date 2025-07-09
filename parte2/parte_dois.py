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

lista_pequena = []
with open("pequeno.txt","r",encoding ="utf8" ) as arquivo:
    for i in arquivo:
        dados = eval(i)
        print(dados)
        '''
        nome =  dados[0]
        idade = int(dados[1])
        quarto = int(dados[2])
        preco = float(dados[3])
        acompanhantes = [j.strip('[').strip(']') for j in dados[:4]]
        '''

print(lista_pequena)