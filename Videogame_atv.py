from datetime import date

class Videogame:
    num_serie = 1
    def __init__(self, marca = 'playstation', modelo = 'play 5', data_fab = date.today()):
        self.marca = marca
        self.modelo = modelo
        self.data_fab = data_fab
        self.num_serie = Videogame.num_serie
        self.jogos = ['need for stive', 'praça of world']
        self.garantia = 5
        Videogame.num_serie += 1
        
v1 = Videogame()
v2 = Videogame(data_fab = 2022)
v3 = Videogame(data_fab = 2022, marca = 'Nintendo', modelo = '64')

games = [v1, v2, v3]

for game in games:            #imprime os atibutos de cada videogame
    print(f'Marca: {game.marca}; \nModelo: {game.modelo}; \nData de Fabricação: {game.data_fab}; \nNumero de série: {game.num_serie}; \nJogos: {game.jogos[0]}, {game.jogos[1]}; \n----------------\n')

for game in games:            #imprime os atibutos de cada videogame de maneira simplificada
    for atributo, valor in game.__dict__.items():
        print(f'{atributo}: {valor}')
    print('\n----------------\n')
