class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite=1000):

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def imprime_referecia(self):
        print(f'Endereço do meu objeto: {self}')

    def extrato(self):
        print(f'Titular: {self.__titular} - Saldo: {self.__saldo}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor: [{valor}] passou do limite.')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'Banco do Brasil': '001', 'Caixa': '104', 'Bradesco': '237'}
