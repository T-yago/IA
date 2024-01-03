from datetime import *

from datetime import datetime, timedelta

"""
Classe que representa uma entrega.
"""
class Entrega():

    def __init__(self, id, peso, volume, freguesia, rua, prazo, idEstafeta, rankingEstafeta=None, dateTimeCriada=datetime.now(), dateTimeEntregue=None):
            """
            Inicializa uma instância da classe Entrega.

            Args:
                id (int): O id da entrega.
                peso (float): O peso da entrega.
                volume (float): O volume da entrega.
                freguesia (str): A freguesia da entrega.
                rua (str): A rua da entrega.
                prazo (int): O prazo em minutos para entregar a encomenda.
                idEstafeta (int): O id do estafeta responsável pela entrega.
                rankingEstafeta (int, optional): O ranking atribuído ao estafeta após a entrega estar realizada. Defaults to None.
                dateTimeCriada (datetime, optional): A data e hora em que a entrega foi criada. Defaults to datetime.now().
                dateTimeEntregue (datetime, optional): A data e hora em que a encomenda foi entregue. Defaults to None.
            """
            self.id = id                                                        # Id da Entrega
            self.peso = peso                                                    # Peso da Entrega
            self.volume = volume                                                # Volume da Entrega
            self.pontoDeEntrega = freguesia + ", " + rua                        # Local de Entrega
            self.prazo = dateTimeCriada + timedelta(minutes=prazo)              # Data limite para entregar a encomenda
            self.estafeta = idEstafeta                                          # Id do estafeta responsável pela entrega
            self.rankingEstafeta = rankingEstafeta                              # Ranking atribuído ao estafeta após a entrega estar realizada
            self.dateTimeCriada = dateTimeCriada                                # Data em que a entrega foi criada
            self.dateTimeEntregue = dateTimeEntregue                            # Data em que a encomenda foi entregue

    def getID(self):
        """
        Retorna o ID do objeto.
        
        :return: O ID do objeto.
        """
        return self.id
    
    def getPeso(self):
        """
        Retorna o peso do objeto.
        """
        return self.peso
    
    def getVolume(self):
        """
        Retorna o volume do objeto.
        """
        return self.volume
    
    def getPontoDeEntrega(self):
        """
        Retorna o ponto de entrega.

        :return: O ponto de entrega.
        """
        return self.pontoDeEntrega
    
    def getPrazo(self):
        """
        Retorna o prazo da entrega.

        :return: O prazo da entrega.
        """
        return self.prazo

    def getEstafeta(self):
        """
        Retorna o estafeta associado a esta entrega.
        """
        return self.estafeta
    
    def getRankingEstafeta(self):
        """
        Retorna o ranking do estafeta.

        :return: O ranking do estafeta.
        """
        return self.rankingEstafeta

    def getDateTimeCriada(self):
        """
        Retorna a data e hora de criação.
        
        :return: A data e hora de criação.
        :rtype: datetime.datetime
        """
        return self.dateTimeCriada
    
    def getDateTimeEntregue(self):
        """
        Retorna a data e hora em que a entrega foi realizada.

        :return: A data e hora da entrega.
        """
        return self.dateTimeEntregue
    
    def setID(self, id):
        """
        Define o ID do objeto.

        Args:
            id (int): O ID a ser atribuído ao objeto.
        """
        self.id = id

    def setPeso(self, peso):
            """
            Define o peso do objeto.

            Args:
                peso (float): O peso do objeto.
            """
            self.peso = peso
    
    def setVolume(self, volume):
            """
            Define o volume do objeto.

            Args:
                volume (float): O valor do volume a ser definido.
            """
            self.volume = volume

    def setPontoDeEntrega(self, freguesia, rua):
        """
        Define o ponto de entrega da encomenda.

        Args:
            freguesia (str): O nome da freguesia onde será feita a entrega.
            rua (str): O nome da rua onde será feita a entrega.

        Returns:
            None
        """
        self.pontoDeEntrega = freguesia + ", " + rua

    def setPrazo(self, prazo):
        """
        Define o prazo da entrega.

        Args:
            prazo (str): O prazo da entrega.

        Returns:
            None
        """
        self.prazo = prazo

    def setEstafeta(self, estafeta):
        """
        Define o estafeta associado a esta entrega.

        Args:
            estafeta (str): O nome do estafeta.

        Returns:
            None
        """
        self.estafeta = estafeta

    def setRankingEstafeta(self, rankingEstafeta):
        """
        Define o ranking do estafeta.

        :param rankingEstafeta: O ranking do estafeta.
        :type rankingEstafeta: int
        """
        self.rankingEstafeta = rankingEstafeta

    def setDateTimeCriada(self, dateTimeCriada):
        """
        Define a data e hora de criação da entrega.

        :param dateTimeCriada: A data e hora de criação da entrega.
        :type dateTimeCriada: datetime.datetime
        """
        self.dateTimeCriada = dateTimeCriada

    def setDateTimeEntregue(self, dateTimeEntregue):
        """
        Define a data e hora de entrega da encomenda.

        :param dateTimeEntregue: A data e hora de entrega da encomenda.
        :type dateTimeEntregue: datetime.datetime
        """
        self.dateTimeEntregue = dateTimeEntregue

    """
    Devolve uma string representativa da informação da entrega, que varia dependendo se esta está completa ou não
    """
    def __str__(self):
        if self.dateTimeEntregue != None:
            return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.pontoDeEntrega} com o estafeta {self.id}. Foi criada em {self.dateTimeCriada} com um prazo até {self.prazo} e entregue em {self.dateTimeEntregue}, dando ao estafeta uma classificação de {self.rankingEstafeta}."
        else:
            return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.pontoDeEntrega} com o estafeta {self.id}, Foi criada em {self.dateTimeCriada} com um prazo até {self.prazo} e está por entregar."
    
    def __eq__(self, other):
            """
            Verifica se o objeto atual é igual ao objeto 'other'.

            Args:
                other: O objeto a ser comparado com o objeto atual.

            Returns:
                True se os objetos forem iguais, False caso contrário.
            """
            return self.id == other.id

    def __hash__(self):
        """
        Retorna o valor hash do objeto com base no seu atributo 'id'.
        
        :return: O valor hash do objeto.
        """
        return hash(self.id)