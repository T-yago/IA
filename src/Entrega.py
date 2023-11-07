from datetime import *

class Entrega():
    def __init__(self, id, peso, volume, freguesia, rua, meioTransporte, prazo
                 , estafeta, rankingEstafeta = None, dateTimeCriada = datetime.now(), dateTimeEntregue = datetime.now()):
        self.id = id
        self.peso = peso
        self.volume = volume
        self.freguesia = freguesia
        self.rua = rua
        self.meioTransporte = meioTransporte
        self.prazo = prazo
        self.estafeta = estafeta
        self.rankingEstafeta = rankingEstafeta
        self.dateTimeCriada = dateTimeCriada
        self.dateTimeEntregue = dateTimeEntregue

    def getID(self):
        return self.id
    
    def getPeso(self):
        return self.peso
    
    def getVolume(self):
        return self.volume
    
    def getFreguesia(self):
        return self.freguesia
    
    def getRua(self):
        return self.rua
    
    def getMeioTransporte(self):
        return self.meioTransporte
    
    def getPrazo(self):
        return self.prazo

    def getEstafeta(self):
        return self.estafeta
    
    def getRankingEstafeta(self):
        return self.rankingEstafeta

    def getDateTimeCriada(self):
        return self.dateTimeCriada
    
    def getDateTimeEntregue(self):
        return self.dateTimeEntregue
    
    def setID(self, id):
        self.id = id

    def setPeso(self, peso):
        self.peso = peso
    
    def setVolume(self, volume):
        self.volume = volume

    def setFreguesia(self, freguesia):
        self.freguesia = freguesia

    def setRua(self, rua):
        self.rua = rua

    def setMeioTransporte(self, meioTransporte):
        self.meioTransporte = meioTransporte

    def setPrazo(self, prazo):
        self.prazo = prazo

    def setEstafeta(self, estafeta):
        self.estafeta = estafeta

    def setRankingEstafeta(self, rankingEstafeta):
        self.rankingEstafeta = rankingEstafeta

    def setDateTimeCriada(self, dateTimeCriada):
        self.dateTimeCriada = dateTimeCriada

    def setDateTimeEntregue(self, dateTimeEntregue):
        self.dateTimeEntregue = dateTimeEntregue

    def __str__(self):
        return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.freguesia}, na rua {self.rua} com o estafeta {self.estafeta.getID()}, sendo o seu ranking de {self.rankingEstafeta}."

    def __repr__(self):
        return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.freguesia}, na rua {self.rua} com o estafeta {self.estafeta.getID()}, sendo o seu ranking de {self.rankingEstafeta}."
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
    
    def velocidade(self):
        return self.meioTransporte.velocidade - self.meioTransporte.descrescimo