class Conta:

    def __init__(self, numero, titular, limite, saldo):
        print('Iniciando objeto Conta...')
        self.__numero = numero
        self.__titular = titular
        self.__limite = limite
        self.__saldo = saldo
        print('Objeto Conta inicializado com sucesso...')

    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print(f"Saldo do titular {self.__titular} é de {self.__saldo}")

    def transfere(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)
    
    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

