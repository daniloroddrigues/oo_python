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

    def deposita(self, valor):
        """
        Método para depositar dinheiro na conta

        :param valor:
        :return:
        """
        self.saldo += valor

    def saca(self, valor):
        """
        Método para sacar dinheiro da conta

        :param valor:
        :return:
        """
        self.saldo -= valor

    def extrato(self):
        """
        Extrato para contas bancárias

        :return:
        """
        return f"------------------------------------\nnumero: {self.numero}\nsaldo: {self.saldo}"
