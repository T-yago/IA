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

    def addEstafeta(self, nomeEstafeta, entregas, ranking):
        idEstafeta = len(self.estafetas)
        newEstafeta = Estafeta(idEstafeta, nomeEstafeta, entregas, ranking)
        self.estafetas[idEstafeta] = newEstafeta
    
    def addMeioTransporte(self, nome, pesoMax, velocidade, decrescimo):
        self.meiosTransporte[nome] = MeioTransporte(nome, pesoMax, velocidade, decrescimo)
    
    def addEntrega(self, peso, volume, freguesia, rua, prazo, idEstafeta = None):
        if idEstafeta==None or idEstafeta not in self.estafetas:
            # Escolhe o id de um estafeta aleatório
            nEstafetas = len(self.estafetas)
            random_id = random.randint(0, nEstafetas)
            self.estafetas[idEstafeta].addEntrega(random_id)
        idEntrega = len(self.entregasPendentes) + len(self.entregasConcluidas)
        self.entregasPendentes[idEntrega] = Entrega(idEntrega, peso, volume, freguesia, rua, prazo, idEstafeta)

    def addLocalizacao(self, freguesia1, rua1, freguesia2, rua2, distancia):
        nome1 = freguesia1 + ", " + rua1
        nome2 = freguesia2 + ", " + rua2
        self.grafo.add_edge(nome1, nome2, distancia)
    
    def getInfoEstafeta(self, idEstafeta):
        res = self.estafetas[idEstafeta].__str__() + "\n\nEntregas:\n"
        idsEntregasConcluidas = self.estafetas[idEstafeta].getEntregasConcluidas()
        for idEntrega in idsEntregasConcluidas:
            res += self.entregasConcluidas[idEntrega].__str__() + "\n"
        idsEntregasInconcluidas = self.estafetas[idEstafeta].getEntregasInconcluidas()
        for idEntrega in idsEntregasInconcluidas:
            res += self.entregasPendentes[idEntrega].__str__() + "\n"

        return res[:-1]

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
