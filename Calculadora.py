class Usuario:
    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self):
        return f'''Olá {self.nome}!
-------------------------
    Caculadora Python
Escolha uma opção abaixo:
Soma: digite +
Subtração: digite -
Multiplicação: digite *
Divisão: digite /
Sair: digite S

Operador: '''

class Calc:
    def __init__(self, op, n1, n2):
        self.op = op
        self.n1 = n1
        self.n2 = n2
        
    def calculo(self):
        if self.op == '+':
            r = self.n1 + self.n2
        if self.op == '-':
            r = self.n1 - self.n2
        if self.op == '*':
            r = self.n1 * self.n2
        if self.op == '/':
            r = self.n1 / self.n2
        return r
    
class Item:
    def __init__(self, op, n1, n2, r):
        self.op = op
        self.n1 = n1
        self.n2 = n2
        self.r = r
        
    def get_operador(self):
        if self.op == '+':
            operador = 'Soma'
        if self.op == '-':
            operador = 'Subtração'
        if self.op == '*':
            operador = 'Multiplicação'
        if self.op == '/':
            operador = 'Divisão'
        return operador
        
    def item(self):
        operador = self.get_operador()
        item = (f'Operador: {operador}; Termos: {self.n1} {self.n2}; Resultado: {self.r}')
        return item

usuario = Usuario(input('Digite seu nome: '))
print(usuario)

vetor = []
while True:
    operador = input()
    if operador == 'S':
        print('Você saiu!')
        break
    else:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        calculo = Calc(operador, n1, n2)
        r = calculo.calculo()
        item = Item(operador, n1, n2, r)
        item_str = item.item()
        vetor.append(item_str)
        print(f'O resultado é: {r}')
        print('''
-------------------------
Escolha uma opção abaixo:
Soma: digite +
Subtração: digite -
Multiplicação: digite *
Divisão: digite /
Sair: digite S

Operador:  ''')

print('''Lista de Operações
-------------------------''')
for linha in vetor:
    print(linha)
        
