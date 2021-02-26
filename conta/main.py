from conta import Conta

if __name__ == '__main__':
    c1 = Conta('1234-5', 'Erick Matias', 200, 1000)
    print('Numero: ', c1.numero)
    print('Nome: ', c1.titular)
    print('Saldo: ', c1.saldo)
    print('Limite: ', c1.limite)
