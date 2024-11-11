class Data:
    def __init__(self, dia:int, mes:int, ano:int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes
    
    def get_ano(self):
        return self.__ano

    def set_dia(self, nv_dia):
        self.__dia = nv_dia

    def set_mes(self, nv_mes):
        self.__mes = nv_mes

    def set_ano(self, nv_ano):
        self.__ano = nv_ano

    def __str__(self):
        return f'{self.__dia:02d}/{self.__mes:02d}/{self.__ano:04d}'

data1 = Data(8,11,2024)
data2 = Data(25,1,1999)
datas = [data1, data2]
for data in datas:
    print(data.get_dia())
    print(data.get_mes())
    print(data.get_ano())
    print(data.__str__())
    data.set_dia(2)
    data.set_mes(12)
    data.set_ano(2000)
    print(data.__str__())





