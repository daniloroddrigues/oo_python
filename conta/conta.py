class Conta:
    """
    Classe para criação de contas bancárias
    """
    def __init__(self, numero, titular, saldo, limite):
        """
        Método construtor python

        :param numero:
        :param titular:
        :param saldo:
        :param limite:
        """
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
