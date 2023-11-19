import random
import datetime
from Graph import *
from Entrega import *
from Estafeta import *
from MeioTransporte import *

class HealthPlanet():
    def __init__(self):
        self.estafetas = {}
        self.entregasPendentes = {}
        self.entregasConcluidas = {}
        self.meiosTransporte = {}
        self.meiosTransporte["Bicicleta"] = MeioTransporte("Bicicleta", 5, 10, 0.6, [])
        self.meiosTransporte["Moto"] = MeioTransporte("Moto", 20, 35, 0.5, [])
        self.meiosTransporte["Carro"] = MeioTransporte("Carro", 100, 50, 0.1, [])

    def addEstafeta(self, nomeEstafeta, nomeMeioTransporte):
        idEstafeta = len(self.estafetas)
        meioTransporte = self.meiosTransporte[nomeMeioTransporte]
        newEstafeta = Estafeta(idEstafeta, nomeEstafeta)

        self.estafetas[idEstafeta] = newEstafeta
        meioTransporte.addEstafeta(newEstafeta.getID()) 
    
    def addEntrega(self, peso, volume, freguesia, rua, prazo):
        if peso <= 5:
            meioTransporte = self.meiosTransporte["Bicicleta"]
        elif peso <= 20:
            meioTransporte = self.meiosTransporte["Moto"]
        else:
            meioTransporte = self.meiosTransporte["Carro"]
        
        idEntrega = len(self.entregasPendentes) + len(self.entregasConcluidas)

        estafetasMT = meioTransporte.getEstafetas()
        randIndex = random.choice(range(0, len(estafetasMT)))
        estafeta = self.estafetas[estafetasMT[randIndex]]

        self.entregasPendentes[idEntrega] = Entrega(idEntrega, peso, volume, freguesia, rua, meioTransporte, prazo, estafeta)

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
