from datetime import *

class Entrega():
    def __init__(self, id, peso, volume, freguesia, rua, prazo
                 , idEstafeta, rankingEstafeta = None, dateTimeCriada = datetime.now(), dateTimeEntregue = None):
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
        return self.id
    
    def getPeso(self):
        return self.peso
    
    def getVolume(self):
        return self.volume
    
    def getPontoDeEntrega(self):
        return self.pontoDeEntrega
    
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

    def setPontoDeEntrega(self, freguesia, rua):
        self.pontoDeEntrega = freguesia + ", " + rua

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
        if self.dateTimeEntregue != None:
            return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.pontoDeEntrega} com o estafeta {self.id}. Foi criada em {self.dateTimeCriada} com um prazo até {self.prazo} e entregue em {self.dateTimeEntregue}, dando ao estafeta uma classificação de {self.rankingEstafeta}."
        else:
            return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.pontoDeEntrega} com o estafeta {self.id}, Foi criada em {self.dateTimeCriada} com um prazo até {self.prazo} e está por entregar."
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
