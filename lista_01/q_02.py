class Aluno:
    def __init__(self, matricula:int, nome:str, notas:list = []):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas

    def get_nome(self):
        return f'Olá, {self.__nome}!'

    def get_matricula(self):
        return f'Mat: {self.__matricula}'

    def media(self):
        return sum(self.__notas)/len(self.__notas)

    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def adiciona_nota(self, nota):
        self.__notas.append(nota)

aluno01 = Aluno(1234, 'joao')
aluno01.adiciona_nota(100)
aluno01.adiciona_nota(90)
media = aluno01.media()
print(aluno01.get_nome())
print(aluno01.get_matricula())
print(media)

aluno01.set_nome('jose')
print(aluno01.get_nome())
