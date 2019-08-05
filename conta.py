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

    def __saque_valido(self, valor_a_sacar):
        valor_disponivel = self.__limite + self.__saldo
        return (valor_a_sacar <= valor_disponivel)
    
    def saca(self, valor):
        if self.__saque_valido(valor):
            self.__saldo -= valor
        else:
            print('Saque inválido')

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

    @staticmethod
    def codigos_bancos(self):
        return {
            'BB': '001',
            'Caixa': '104',
            'Bradesco': '237'
        }
    
