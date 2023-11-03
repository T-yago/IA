class Entrega():
    def __init__(self, id, peso, volume, freguesia, rua, estafeta, rankingEstafeta):
        self.id = id
        self.peso = peso
        self.volume = volume
        self.freguesia = freguesia
        self.rua = rua
        self.estafeta = estafeta
        self.rankingEstafeta = rankingEstafeta

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
    
    def getEstafeta(self):
        return self.estafeta
    
    def getRankingEstafeta(self):
        return self.rankingEstafeta

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

    def setEstafeta(self, estafeta):
        self.estafeta = estafeta

    def setRankingEstafeta(self, rankingEstafeta):
        self.rankingEstafeta = rankingEstafeta

    def __str__(self):
        return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.freguesia}, na rua {self.rua} com o estafeta {self.estafeta.getID()}, sendo o seu ranking de {self.rankingEstafeta}."

    def __repr__(self):
        return f"Entrega nº{self.id}, {self.peso}kg e Volume = {self.volume}, em {self.freguesia}, na rua {self.rua} com o estafeta {self.estafeta.getID()}, sendo o seu ranking de {self.rankingEstafeta}."
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)