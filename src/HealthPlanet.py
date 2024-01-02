import datetime
import random
from Graph import *
from Entrega import *
from Estafeta import *
from MeioTransporte import *

class HealthPlanet():
    """
    Represents a HealthPlanet object that manages deliveries, couriers, and transportation methods.

    Attributes:
        grafo (Grafo): The graph representing the intersections and distances between them.
        estafetas (dict): A dictionary of couriers, where the key is the courier ID and the value is the Estafeta object.
        entregasPendentes (dict): A dictionary of pending deliveries, where the key is the delivery ID and the value is the Entrega object.
        entregasConcluidas (dict): A dictionary of completed deliveries, where the key is the delivery ID and the value is the Entrega object.
        meiosTransporte (dict): A dictionary of transportation methods, where the key is the method name and the value is the MeioTransporte object.
    """

    def __init__(self):
        """
        Initializes a new instance of the HealthPlanet class.
        """
        self.grafo = Grafo()
        self.estafetas = {}
        self.entregasPendentes = {}
        self.entregasConcluidas = {}
        self.meiosTransporte = {}

    def addEstafeta(self, nomeEstafeta, entregas, ranking):
        """
        Adds a new courier to the HealthPlanet.

        Args:
            nomeEstafeta (str): The name of the courier.
            entregas (int): The number of deliveries the courier has completed.
            ranking (float): The ranking of the courier.

        Returns:
            None
        """
        idEstafeta = len(self.estafetas)
        newEstafeta = Estafeta(idEstafeta, nomeEstafeta, entregas, ranking)
        self.estafetas[idEstafeta] = newEstafeta
    
    def addMeioTransporte(self, nome, pesoMax, velocidade, decrescimo):
        """
        Adds a new transportation method to the HealthPlanet.

        Args:
            nome (str): The name of the transportation method.
            pesoMax (float): The maximum weight the transportation method can carry.
            velocidade (float): The speed of the transportation method.
            decrescimo (float): The decrease factor for the transportation method.

        Returns:
            None
        """
        self.meiosTransporte[nome] = MeioTransporte(nome, pesoMax, velocidade, decrescimo)
    
    def addEntrega(self, peso, volume, freguesia, rua, prazo, idEstafeta = None):
        """
        Adds a new delivery to the HealthPlanet.

        Args:
            peso (float): The weight of the delivery.
            volume (float): The volume of the delivery.
            freguesia (str): The name of the neighborhood where the delivery should be made.
            rua (str): The name of the street where the delivery should be made.
            prazo (int): The deadline for the delivery.
            idEstafeta (int, optional): The ID of the courier assigned to the delivery. Defaults to None.

        Returns:
            None
        """
        if idEstafeta==None or idEstafeta not in self.estafetas:
            # Escolhe o id de um estafeta aleatório
            nEstafetas = len(self.estafetas)
            random_id = random.randint(0, nEstafetas)
            self.estafetas[idEstafeta].addEntrega(random_id)
        idEntrega = len(self.entregasPendentes) + len(self.entregasConcluidas)
        self.entregasPendentes[idEntrega] = Entrega(idEntrega, peso, volume, freguesia, rua, prazo, idEstafeta)

    def addIntercecao(self, freguesia1, rua1, coordenadas1, freguesia2, rua2, coordenadas2, distancia):
        """
        Adds an intersection to the graph of the HealthPlanet.

        Args:
            freguesia1 (str): The name of the first neighborhood.
            rua1 (str): The name of the first street.
            coordenadas1 (tuple): The coordinates of the first intersection.
            freguesia2 (str): The name of the second neighborhood.
            rua2 (str): The name of the second street.
            coordenadas2 (tuple): The coordinates of the second intersection.
            distancia (float): The distance between the two intersections.

        Returns:
            None
        """
        nome1 = freguesia1 + ", " + rua1
        nome2 = freguesia2 + ", " + rua2
        self.grafo.add_edge(nome1, coordenadas1, nome2, coordenadas2, distancia)
    
    def getInfoEstafeta(self, idEstafeta):
        """
        Retrieves information about a courier in the HealthPlanet.

        Args:
            idEstafeta (int): The ID of the courier.

        Returns:
            str: The information about the courier and their deliveries.
        """
        res = self.estafetas[idEstafeta].__str__() + "\n\nEntregas:\n"
        idsEntregasConcluidas = self.estafetas[idEstafeta].getEntregasConcluidas()
        for idEntrega in idsEntregasConcluidas:
            res += self.entregasConcluidas[idEntrega].__str__() + "\n"
        idsEntregasInconcluidas = self.estafetas[idEstafeta].getEntregasInconcluidas()
        for idEntrega in idsEntregasInconcluidas:
            res += self.entregasPendentes[idEntrega].__str__() + "\n"

        return res[:-1]

    def concluirEntrega(self, idEntrega, rankingEstafeta, prazo):
        """
        Marks a delivery as completed in the HealthPlanet.

        Args:
            idEntrega (int): The ID of the delivery.
            rankingEstafeta (float): The ranking of the courier who completed the delivery.
            prazo (int): The deadline for the delivery.

        Returns:
            None
        """
        entrega = self.entregasPendentes.pop(idEntrega)
        entrega.setDateTimeEntregue(datetime.now())

        newRankingEstafeta = rankingEstafeta
        diferencaMinutos = int((entrega.getDateTimeEntregue() - entrega.getDateTimeCriada()).total_seconds() / 60) - prazo
        
        if diferencaMinutos > 0:
            if diferencaMinutos < 10:
                newRankingEstafeta -= 0.5
            elif diferencaMinutos < 25:
                newRankingEstafeta -= 1
            else:
                newRankingEstafeta -= 2

        entrega.setRankingEstafeta(newRankingEstafeta)
        entrega.getEstafeta().addEntregaRanking(rankingEstafeta)

        self.entregasConcluidas[idEntrega] = entrega
