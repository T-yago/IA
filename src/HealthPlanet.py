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
        
        idEntrega = len(self.entregasPendentes)

        estafetasMT = meioTransporte.getEstafetas()
        randIndex = random.choice(range(0, len(estafetasMT)))
        estafeta = self.estafetas[estafetasMT[randIndex]]

        self.entregasPendentes[idEntrega] = Entrega(idEntrega, peso, volume, freguesia, rua, meioTransporte, prazo, estafeta)

    def concluirEntrega(self, idEntrega, rankingEstafeta, prazo):
        entrega = self.entregasPendentes.pop(idEntrega)

        entrega.setRankingEstafeta(rankingEstafeta)
        entrega.setDateTimeEntregue(datetime.now())

        entrega.getEstafeta().addEntregaRanking(rankingEstafeta)

        self.entregasConcluidas[idEntrega] = entrega

        # FALTA VERIFICAR O PRAZO

hp = HealthPlanet()

hp.addEstafeta("Joao1", "Carro")
hp.addEstafeta("Joao2", "Moto")
hp.addEstafeta("Joao3", "Moto")
hp.addEstafeta("Joao4", "Carro")
hp.addEstafeta("Joao5", "Bicicleta")

hp.addEntrega(3, 30, "Barcelos", "Rua Dr", 10)
hp.addEntrega(20, 30, "Barcelos", "Rua Dr", 10)
hp.addEntrega(90, 30, "Barcelos", "Rua Dr", 10)

for entrega in hp.entregasPendentes.values():
    print(entrega)