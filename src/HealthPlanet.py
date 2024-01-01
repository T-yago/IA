import random
import datetime
from Graph import *
from Entrega import *
from Estafeta import *
from MeioTransporte import *

class HealthPlanet():
    def __init__(self):
        self.grafo = Grafo()
        self.estafetas = {}
        self.entregasPendentes = {}
        self.entregasConcluidas = {}
        self.meiosTransporte = {}
        self.meiosTransporte["Bicicleta"] = MeioTransporte("Bicicleta", 5, 10, 0.6)
        self.meiosTransporte["Moto"] = MeioTransporte("Moto", 20, 35, 0.5)
        self.meiosTransporte["Carro"] = MeioTransporte("Carro", 100, 50, 0.1)

    def addEstafeta(self, nomeEstafeta, entregas, ranking):
        idEstafeta = len(self.estafetas)
        newEstafeta = Estafeta(idEstafeta, nomeEstafeta, entregas, ranking)
        self.estafetas[idEstafeta] = newEstafeta
    
    def addEntrega(self, peso, volume, freguesia, rua, prazo, idEstafeta):
        if idEstafeta in self.estafetas:
            idEntrega = len(self.entregasPendentes) + len(self.entregasConcluidas)
            self.entregasPendentes[idEntrega] = Entrega(idEntrega, peso, volume, freguesia, rua, prazo, idEstafeta)
            self.estafetas[idEstafeta].addEntrega(idEntrega)

    def addLocalizacao(self, freguesia1, rua1, freguesia2, rua2, distancia):
        nome1 = freguesia1 + ", " + rua1
        nome2 = freguesia2 + ", " + rua2
        self.grafo.add_edge(nome1, nome2. distancia)

    def concluirEntrega(self, idEntrega, rankingEstafeta, prazo):
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
