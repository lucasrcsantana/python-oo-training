def cria_conta(numero, titular, limite, saldo):
    conta = {
        'numero': numero,
        'titular': titular,
        'limite': limite,
        'saldo': saldo
    }
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f"Seu saldo é {conta['saldo']}")