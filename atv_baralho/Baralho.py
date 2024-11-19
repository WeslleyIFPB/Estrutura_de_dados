import random
import numpy as np

class Cartas:
    def __init__(self, valor, naipe):
        self.__valor = valor  # Atributo privado
        self.__naipe = naipe  # Atributo privado

    def __str__(self):
        return f'{self.__valor} de {self.__naipe}'

    def get_valor(self):
        return self.__valor

    def get_naipe(self):
        return self.__naipe

    def set_valor(self, valor):
        self.__valor = valor

    def set_naipe(self, naipe):
        self.__naipe = naipe


class Baralho:
    __valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] # Atributo privado
    __naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']  

    def __init__(self):
        self.__cartas = [Cartas(valor, naipe) for valor in self.__valores for naipe in self.__naipes]
 
    def embaralhar(self):
        random.shuffle(self.__cartas)

    def puxar(self):        
        return self.__cartas.pop()

    def distribuir(self, n):
        # Verificando se o número de jogadores é válido
        if n < 1 or n > 4:
            return 'Número inválido de jogadores. Só são permitidos entre 1 e 4 jogadores.'
        
        # Dividindo as cartas entre os jogadores
        lista_d = np.array_split(self.__cartas, n)
        jogadores = [lista.tolist() for lista in lista_d]

        # Retornando os jogadores
        if n == 1:
            return jogadores[0]
        elif n == 2:
            return jogadores[0], jogadores[1]
        elif n == 3:
            jogadores[0].pop()
            return jogadores[0], jogadores[1], jogadores[2]
        elif n == 4:
            return jogadores[0], jogadores[1], jogadores[2], jogadores[3]

    def mostrar_cartas(self, jogadores):
        if isinstance(jogadores, str):  # Testa se deu erro, caso o número de jogadores seja inválido
            print(jogadores)
        else:
            for i, jogador in enumerate(jogadores, start=1):
                print(f'Jogador {i}:')
                for carta in jogador:
                    print(f'  -> {carta}')


# Execução do código

# Criando o baralho e embaralhando
baralho = Baralho()
baralho.embaralhar()

# Distribuindo as cartas para 3 jogadores (Cada jogador receberá 17 cartas)
jogadores = baralho.distribuir(3)

baralho.mostrar_cartas(jogadores)
