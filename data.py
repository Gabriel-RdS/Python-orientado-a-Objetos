
class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def referencia(self):
        print(f'Meu objeto foi construído e está alocado em: {self}')

    def formata_data(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')
