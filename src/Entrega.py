from datetime import *

from datetime import datetime, timedelta

class Entrega():
    """
    Represents a delivery.

    Attributes:
        id (int): The ID of the delivery.
        peso (float): The weight of the delivery in kilograms.
        volume (float): The volume of the delivery.
        pontoDeEntrega (str): The delivery point (freguesia and rua).
        prazo (datetime): The deadline for the delivery.
        estafeta (int): The ID of the delivery person.
        rankingEstafeta (int): The ranking of the delivery person.
        dateTimeCriada (datetime): The date and time when the delivery was created.
        dateTimeEntregue (datetime): The date and time when the delivery was completed.
    """

    def __init__(self, id, peso, volume, freguesia, rua, prazo, idEstafeta, rankingEstafeta=None, dateTimeCriada=datetime.now(), dateTimeEntregue=None):
        """
        Initializes a new instance of the Entrega class.

        Args:
            id (int): The ID of the delivery.
            peso (float): The weight of the delivery in kilograms.
            volume (float): The volume of the delivery.
            freguesia (str): The freguesia of the delivery point.
            rua (str): The rua of the delivery point.
            prazo (int): The deadline for the delivery in minutes.
            idEstafeta (int): The ID of the delivery person.
            rankingEstafeta (int, optional): The ranking of the delivery person. Defaults to None.
            dateTimeCriada (datetime, optional): The date and time when the delivery was created. Defaults to the current date and time.
            dateTimeEntregue (datetime, optional): The date and time when the delivery was completed. Defaults to None.
        """
        self.id = id
        self.peso = peso
        self.volume = volume
        self.pontoDeEntrega = freguesia + ", " + rua
        self.prazo = dateTimeCriada + timedelta(minutes=prazo)
        self.estafeta = idEstafeta
        self.rankingEstafeta = rankingEstafeta
        self.dateTimeCriada = dateTimeCriada
        self.dateTimeEntregue = dateTimeEntregue

    def getID(self):
        """
        Gets the ID of the delivery.

        Returns:
            int: The ID of the delivery.
        """
        return self.id
    
    def getPeso(self):
        """
        Gets the weight of the delivery.

        Returns:
            float: The weight of the delivery in kilograms.
        """
        return self.peso
    
    def getVolume(self):
        """
        Gets the volume of the delivery.

        Returns:
            float: The volume of the delivery.
        """
        return self.volume
    
    def getPontoDeEntrega(self):
        """
        Gets the delivery point.

        Returns:
            str: The delivery point (freguesia and rua).
        """
        return self.pontoDeEntrega
    
    def getPrazo(self):
        """
        Gets the deadline for the delivery.

        Returns:
            datetime: The deadline for the delivery.
        """
        return self.prazo

    def getEstafeta(self):
        """
        Gets the ID of the delivery person.

        Returns:
            int: The ID of the delivery person.
        """
        return self.estafeta
    
    def getRankingEstafeta(self):
        """
        Gets the ranking of the delivery person.

        Returns:
            int: The ranking of the delivery person.
        """
        return self.rankingEstafeta

    def getDateTimeCriada(self):
        """
        Gets the date and time when the delivery was created.

        Returns:
            datetime: The date and time when the delivery was created.
        """
        return self.dateTimeCriada
    
    def getDateTimeEntregue(self):
        """
        Gets the date and time when the delivery was completed.

        Returns:
            datetime: The date and time when the delivery was completed.
        """
        return self.dateTimeEntregue
    
    def setID(self, id):
        """
        Sets the ID of the delivery.

        Args:
            id (int): The ID of the delivery.
        """
        self.id = id

    def setPeso(self, peso):
        """
        Sets the weight of the delivery.

        Args:
            peso (float): The weight of the delivery in kilograms.
        """
        self.peso = peso
    
    def setVolume(self, volume):
        """
        Sets the volume of the delivery.

        Args:
            volume (float): The volume of the delivery.
        """
        self.volume = volume

    def setPontoDeEntrega(self, freguesia, rua):
        """
        Sets the delivery point.

        Args:
            freguesia (str): The freguesia of the delivery point.
            rua (str): The rua of the delivery point.
        """
        self.pontoDeEntrega = freguesia + ", " + rua

    def setPrazo(self, prazo):
        """
        Sets the deadline for the delivery.

        Args:
            prazo (int): The deadline for the delivery in minutes.
        """
        self.prazo = prazo

    def setEstafeta(self, estafeta):
        """
        Sets the ID of the delivery person.

        Args:
            estafeta (int): The ID of the delivery person.
        """
        self.estafeta = estafeta

    def setRankingEstafeta(self, rankingEstafeta):
        """
        Sets the ranking of the delivery person.

        Args:
            rankingEstafeta (int): The ranking of the delivery person.
        """
        self.rankingEstafeta = rankingEstafeta

    def setDateTimeCriada(self, dateTimeCriada):
        """
        Sets the date and time when the delivery was created.

        Args:
            dateTimeCriada (datetime): The date and time when the delivery was created.
        """
        self.dateTimeCriada = dateTimeCriada

    def setDateTimeEntregue(self, dateTimeEntregue):
        """
        Sets the date and time when the delivery was completed.

        Args:
            dateTimeEntregue (datetime): The date and time when the delivery was completed.
        """
        self.dateTimeEntregue = dateTimeEntregue

    def __str__(self):
        """
        Returns a string representation of the delivery.

        Returns:
            str: A string representation of the delivery.
        """
        if self.dateTimeEntregue != None:
            return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.pontoDeEntrega} com o estafeta {self.id}. Foi criada em {self.dateTimeCriada} com um prazo até {self.prazo} e entregue em {self.dateTimeEntregue}, dando ao estafeta uma classificação de {self.rankingEstafeta}."
        else:
            return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.pontoDeEntrega} com o estafeta {self.id}, Foi criada em {self.dateTimeCriada} com um prazo até {self.prazo} e está por entregar."
    
    def __eq__(self, other):
        """
        Compares two deliveries for equality.

        Args:
            other (Entrega): The other delivery to compare.

        Returns:
            bool: True if the deliveries are equal, False otherwise.
        """
        return self.id == other.id

    def __hash__(self):
        """
        Returns the hash value of the delivery.

        Returns:
            int: The hash value of the delivery.
        """
        return hash(self.id)