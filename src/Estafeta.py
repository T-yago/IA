class Estafeta():
    def __init__(self, id, nome, nrEntregas = 0, ranking = 0):
        self.id = id
        self.nome = nome
        self.nrEntregas = nrEntregas
        self.ranking = ranking

    def getID(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getNrEntregas(self):
        return self.nrEntregas
    
    def getRanking(self):
        return self.ranking
    
    def setID(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setNrEntregas(self, nrEntregas):
        self.nrEntregas = nrEntregas

    def setRanking(self, ranking):
        self.ranking = ranking

    def getRanking(self):
        if self.nrEntregas == 0:
            return None
        return int(self.ranking) / int(self.nrEntregas)

    def addEntregaRanking(self, ranking):
        self.nrEntregas += 1
        self.ranking = round(((self.ranking * (self.nrEntregas-1)) + ranking) / self.nrEntregas, 2)

    def __str__(self):
        return f"Estafeta nº{self.id}: {self.nome} (Ranking: {self.ranking} em {self.nrEntregas} entregas)"
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
