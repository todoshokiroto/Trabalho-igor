import random
import time
#lista de nomes gerados pelo chatGPT
nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Karina", "Lucas", "Mariana", "Nelson", "Olivia", "Paulo", "Quesia", "Rafael", "Silvia", "Tiago",
    "Vanessa", "William", "Yasmin", "Zeca", "Alice", "Bernardo", "Camila", "Diego", "Elisa", "Felipe",
    "Giovana", "Henrique", "Isadora", "Joao", "Kelly", "Leonardo", "Mirela", "Nathan", "Priscila", "Rodrigo",
    "Sabrina", "Tomas", "Vitoria", "Wagner", "Aline", "Breno", "Clara", "Davi", "Ester", "Fabricio",
    "Graziella", "Hugo", "Iara", "Jorge", "Livia", "Marcelo", "Nicole", "Otavio", "Patricia", "Quirino",
    "Renata", "Samuel", "Talita", "Ubirajara", "Valeria", "Wallace", "Xenia", "Yago", "Zilda", "Andre",
    "Beatriz", "Cesar", "Daniela", "Fabiana", "Gustavo", "Heloisa", "Icaro", "Janaina", "Kleber", "Larissa",
    "Matheus", "Neide", "Orlando", "Paloma", "Quiteria", "Raul", "Sheila", "Tulio", "Vitor", "Amanda",
    "Caio", "Debora", "Enzo", "Flavia", "Guilherme", "Hilda", "Ian", "Joana", "Kaio", "Laura",
    "Miguel", "Nadia", "Osvaldo", "Pamela", "Sandra", "Tales", "Uelinton", "Wellington", "Xuxa", "Yuri",
    "Zuleica", "Adriano", "Bianca", "Cristiano", "Denise", "Everton", "Fabiano", "Glaucia", "Heitor", "Ines",
    "Juliano", "Karol", "Leandro", "Mirella", "Noemi", "Pedro", "Romulo", "Suelen", "Tatiane", "Ulisses",
    "Veronica", "Washington", "Xisto", "Zacarias", "Alan", "Barbara", "Cassio", "Dayane", "Edson", "Fatima",
    "Gilson", "Hortencia", "Iuri", "Jessica", "Kleiton", "Luan", "Michele", "Patricio", "Rafaela", "Sara",
    "Andrea", "Clarissa", "Danilo", "Eloa", "Gisele", "Haroldo", "Iris", "Kamila", "Leticia", "Mauricio",
    "Natan", "Otavia", "Paula", "Ronaldo", "Simone", "Thiago", "Ursula", "Viviane", "Wilian", "Xavier",
    "Zoraide", "Augusto", "Bruna", "Carlos", "Daiane", "Eliane", "Fabio", "Geovana", "Humberto", "Ivana",
    "Jonas", "Katia", "Luiz", "Melina", "Nilson", "Alana", "Caue", "Joice", "Samuel", "Renan"
]

#lista de sobrenomes gerandos pelo chatGPT
sobrenomes = [
    "Silva", "Santos", "Oliveira", "Souza", "Lima", "Pereira", "Costa", "Ferreira", "Rodrigues", "Almeida",
    "Nascimento", "Araujo", "Melo", "Barbosa", "Ribeiro", "Alves", "Carvalho", "Castro", "Martins", "Rocha",
    "Dias", "Teixeira", "Moreira", "Correia", "Pinto", "Goncalves", "Vieira", "Cardoso", "Monteiro", "Moura",
    "Campos", "Leite", "Batista", "Freitas", "Ramos", "Rezende", "Farias", "Machado", "Borges", "Mendes",
    "Nogueira", "Coelho", "Bezerra", "Cavalcanti", "Andrade", "Barros", "Tavares", "Sales", "Fonseca", "Braga",
    "Camargo", "Amaral", "Antunes", "Figueiredo", "Garcia", "Queiroz", "Pacheco", "Lopes", "Morais", "Aguiar",
    "Chaves", "Peixoto", "Neves", "Guimaraes", "Assis", "Bernardes", "Bittencourt", "Buarque", "Candido", "Carmo",
    "Cavalcante", "Coutinho", "Delgado", "Domingues", "Dorneles", "Drumond", "Duraes", "Esteves", "Fagundes", "Felix",
    "Fogaca", "Franca", "Franco", "Galvao", "Gama", "Germano", "Gomes", "Goulart", "Guedes", "Henrique",
    "Jardim", "Jesus", "Jordao", "Lacerda", "Laranjeira", "Leal", "Leme", "Lessa", "Lins", "Lourenco",
    "Maia", "Malta", "Marinho", "Marques", "Mascarenhas", "Matias", "Medeiros", "Meireles", "Menezes", "Mesquita",
    "Miranda", "Muniz", "Neiva", "Novaes", "Nunes", "Ortega", "Padilha", "Paiva", "Paz", "Pedrosa",
    "Penha", "Pimentel", "Portela", "Porto", "Quadros", "Quaresma", "Queiros", "Quintana", "Rangel", "Reis",
    "Resende", "Rios", "Romero", "Sabino", "Sampaio", "Sanches", "Sandoval", "Santana", "Santiago", "Saraiva",
    "Seabra", "Serra", "Soares", "Sousa", "Souto", "Torres", "Trindade", "Valente", "Valle", "Vargas",
    "Vasconcelos", "Vaz", "Veiga", "Veloso", "Veras", "Vilela", "Xavier", "Abreu", "Accioli", "Achcar",
    "Acioli", "Albuquerque", "Alencar", "Altamirano", "Alvarenga", "Anunciacao", "Appolinario", "Aquino", "Aragao", "Arantes",
    "Arruda", "Atayde", "Avellar", "Baia", "Baumgartner", "Belarmino", "Belchior", "Belem", "Benevides", "Bicalho",
    "Boaventura", "Bonfim", "Bontempo", "Borba", "Brandao", "Brito", "Buendia", "Cabral", "Caldas", "Caldeira",
    "Capistrano", "Carneiro", "Carrilho", "Cassiano", "Cattani", "Cerqueira", "Cintra", "Coimbra", "Colares", "Conceicao",
    "Cordeiro", "Couto", "Craveiro", "Crispim", "Cunha", "Curvelo", "Damasio", "Dantas", "Duarte", "Dutra"
]

def gerar_nome():
    return nomes[random.randint(0,189)] +" "+ sobrenomes[random.randint(0,209)]
def gerar_idade():
    return random.randint(18,80)
def gerar_quarto():
    return random.randint(1,100)
def gerar_acompanhantes(qtd):
    lista = [gerar_nome() for i in range(qtd)]
    return lista
def gerar_cliente():
    lista = []
    lista.append(gerar_nome())
    lista.append(gerar_idade())
    quarto = gerar_quarto()
    lista.append(quarto)
    if quarto >= 67:
        lista.append(1100.5)
        lista.append(gerar_acompanhantes(3))
    elif quarto >= 34:
        lista.append(737.33)
        lista.append(gerar_acompanhantes(2))
    else:
        lista.append(460.99)
        lista.append(gerar_nome)
    return lista

inicio = time.time()
for i in range(100):
    with open("parte1/pequeno.txt","a") as arquivo:
        arquivo.write("\n" + str(gerar_cliente()))
fim = time.time()
print(fim - inicio)

inicio = time.time()
for i in range(500):
    with open("parte1/medio.txt","a") as arquivo:
        arquivo.write("\n" + str(gerar_cliente()))
fim = time.time()
print(fim - inicio)

inicio = time.time()
for i in range(100):
    with open("parte1/pequeno.txt","a") as arquivo:
        arquivo.write("\n" + str(gerar_cliente()))
fim = time.time()
print(fim - inicio)

inicio = time.time()
for i in range(2000):
    with open("parte1/grande.txt","a") as arquivo:
        arquivo.write("\n" + str(gerar_cliente()))
fim = time.time()
print(fim - inicio)

inicio = time.time()
for i in range(6000):
    with open("parte1/muito_grande.txt","a") as arquivo:
        arquivo.write("\n" + str(gerar_cliente()))
fim = time.time()
print(fim - inicio)
