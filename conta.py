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

    def saca(self, valor):
        self.__saldo -= valor

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
