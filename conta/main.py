from conta import Conta

if __name__ == '__main__':
    c1 = Conta('1234-5', 'Erick Matias', 200, 1000)
    print('Numero: ', c1.numero)
    print('Nome: ', c1.titular)
    print('Saldo: ', c1.saldo)
    print('Limite: ', c1.limite)

    c1.deposita(200)

    print("Saldo: ", c1.saldo)

    c1.saca(100)

    print("Saldo: ", c1.saldo)

    print(c1.extrato())

    consegue = c1.saca(4000)

    if consegue:
        print("Consegue sacar")
    else:
        print("Não pode sacar")

    c2 = Conta('4321-5', 'Alessandro Vilas Boas', 150, 1000)
    print('Numero: ', c2.numero)
    print('Nome: ', c2.titular)
    print('Saldo: ', c2.saldo)
    print('Limite: ', c2.limite)

    c1.transfere(c2, 100)

    print('C2 Saldo: ', c2.saldo)
