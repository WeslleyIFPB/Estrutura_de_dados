from Baralho import Baralho, Cartas

class Jogador:
    def __init__(self, qtd_jogadores):
        self.__baralho = Baralho()  
        self.__baralho.embaralhar()
        self.__lista_cartas = self.__baralho.distribuir(qtd_jogadores)

    def get_cartas(self):
        return self.__lista_cartas

class Batalha:
    __valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                 'J': 11, 'Q': 12, 'K': 13, 'A': 0 }

    def __init__(self, num_jogadores):
        self.__jogadores = Jogador(num_jogadores)
        self.__montante = [[], []]  # Lista para armazenar as cartas dos vencedores
        self.__cartas_empate = []  # Cartas que ficaram no empate

    def get_valores(self):
        return self.__valores

    def get_jogadores(self):
        return self.__jogadores

    def rodada(self):
        carta_jogador1 = str(self.__jogadores.get_cartas()[0].pop())  # Pega a última carta de cada
        carta_jogador2 = str(self.__jogadores.get_cartas()[1].pop())  
        valor_jogador1 = carta_jogador1.split()[0]  # Pega o valor da carta 
        valor_jogador2 = carta_jogador2.split()[0]

        if self.get_valores()[valor_jogador1] > self.get_valores()[valor_jogador2]:
            print('Jogador 1 venceu a rodada!')
            print(f'Carta do Jogador 1: {carta_jogador1}. \nCarta do Jogador 2: {carta_jogador2}.')
            self.__montante[0].append(carta_jogador1)
            self.__montante[0].append(carta_jogador2)
            self.__montante[0] += self.__cartas_empate  # Adiciona todas as cartas do empate ao jogador 1
            self.__cartas_empate.clear()

        elif self.get_valores()[valor_jogador1] < self.get_valores()[valor_jogador2]:
            print('Jogador 2 venceu a rodada!')
            print(f'Carta do Jogador 1: {carta_jogador1}. \nCarta do Jogador 2: {carta_jogador2}.')
            self.__montante[1].append(carta_jogador1)
            self.__montante[1].append(carta_jogador2)
            self.__montante[1] += self.__cartas_empate  # Adiciona as cartas do empate ao jogador 2
            self.__cartas_empate.clear()

        else:
            print('Valores das cartas são iguais, empate!')
            print(f'Carta do Jogador 1: {carta_jogador1}. \nCarta do Jogador 2: {carta_jogador2}.')
            self.__cartas_empate.append(carta_jogador1)
            self.__cartas_empate.append(carta_jogador2)

    def mostrar_resultado(self):
        print("\nResultado Final:")
        print(f"Jogador 1 - Cartas: {len(self.__montante[0])} cartas")
        print(f"Jogador 2 - Cartas: {len(self.__montante[1])} cartas")
        if len(self.__montante[0]) > len(self.__montante[1]):
            print("Jogador 1 é o vencedor!")
        elif len(self.__montante[0]) < len(self.__montante[1]):
            print("Jogador 2 é o vencedor!")
        else:
            print("Empate final!")

# Execução
batalha = Batalha(2)

num_rodadas = len(batalha.get_jogadores().get_cartas()[0])  # Número de rodadas. Será o número de cartas do primeiro jogador

for i in range(num_rodadas):
    print(f"\nRodada {i + 1}:")
    batalha.rodada()

batalha.mostrar_resultado()
