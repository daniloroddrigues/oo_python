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
        if self.saldo >= valor:
            self.saldo -= valor
            return True

        return False

    def extrato(self):
        """
        Extrato para contas bancárias

        :return:
        """
        return f"------------------------------------\nnumero: {self.numero}\nsaldo: {self.saldo}"

    def transfere(self, destino, valor):
        """
        Método para transferência para outra conta

        :param destino:
        :param valor:
        :return:
        """
        retirou = self.saca(valor)

        if retirou:
            destino.saldo += valor

        return retirou
