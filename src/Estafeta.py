class Estafeta():
    def __init__(self, id, nome, nrEntregas = 0, rankingTotal = 0):
        self.id = id
        self.nome = nome
        self.nrEntregas = nrEntregas
        self.rankingTotal = rankingTotal

    def getID(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getNrEntregas(self):
        return self.nrEntregas
    
    def getRankingTotal(self):
        return self.rankingTotal
    
    def getRanking(self):
        if self.nrEntregas == 0:
            return None
        
        return int(self.rankingTotal) / int(self.nrEntregas)
    
    def setID(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setNrEntregas(self, nrEntregas):
        self.nrEntregas = nrEntregas

    def setRankingTotal(self, rankingTotal):
        self.rankingTotal = rankingTotal

    def addEntregaRanking(self, ranking):
        self.nrEntregas += 1;
        self.rankingTotal += int(ranking)

    def __str__(self):
        return f"Estafeta nº{self.id}: {self.nome} (Ranking: {self.getRanking()})."
    
    def __repr__(self):
        return f"Estafeta nº{self.id}: {self.nome} (Ranking: {self.getRanking()})."
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)