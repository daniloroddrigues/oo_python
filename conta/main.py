from conta import Conta
from cliente import Cliente

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
    c1.transfere(c2, 200)

    print(c1.transfere(c2, 200))
    print('C2 Saldo: ', c2.saldo)

    cli1 = Cliente('Erick', 'Matias', 00000000000)
    print('_________CLIENTE_________')
    print('Nome: ', cli1.nome)
    print('Sobrenome: ', cli1.sobrenome)
    print('CPF: ', cli1.cpf)

    c3 = Conta('12345-6', cli1, 400, 1000)

    print('_________CONTA_________')
    print('Nome: ', c3.titular.nome)
    print('Sobrenome: ', c3.titular.sobrenome)
    print('CPF: ', c3.titular.cpf)
    print('Numero: ', c3.numero)
    print('Saldo: ', c3.saldo)
    print('Limite: ', c3.limite)
