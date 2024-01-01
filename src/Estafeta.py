class Estafeta():
    def __init__(self, id, nome, idsEntregas = [], ranking = 5):
        self.id = id
        self.nome = nome
        self.nrEntregasConcluidas = len(idsEntregas)
        self.entregasInconcluidas = idsEntregas
        self.entregasConcluidas = []
        self.ranking = ranking

    def getID(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getNrEntregasConcluidas(self):
        return self.nrEntregasConcluidas
    
    def getEntregasConcluidas(self):
        return self.entregasConcluidas
    
    def getEntregasInconcluidas(self):
        return self.entregasInconcluidas
    
    def getRanking(self):
        return self.ranking
    
    def setID(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setNrEntregasConcluidas(self, nrEntregasConcluidas):
        self.nrEntregasConcluidas = nrEntregasConcluidas
    
    def setEntregasConcluidas(self, entregasConcluidas):
        self.entregasConcluidas = entregasConcluidas

    def setEntregasInconcluidas(self, entregasInconcluidas):
        self.entregasInconcluidas = entregasInconcluidas

    def setRanking(self, ranking):
        self.ranking = ranking

    def getRanking(self):
        return self.ranking

    def completeEntregas(self, entregas):

        self.ranking = self.ranking * self.nrEntregasConcluidas
        for id, ranking in entregas:
            if (id in self.entregasInconcluidas):
                self.entregasInconcluidas.remove(id)
                self.entregasConcluidas.append(id)
                self.nrEntregasConcluidas += 1
                self.ranking += ranking
        
        self.ranking = round(self.ranking / self.nrEntregasConcluidas, 2)
    
    def addEntrega(self, idEntrega):
        self.entregasInconcluidas.append(idEntrega)

    def __str__(self):
        res = f"Estafeta nº{self.id}: {self.nome}\n\n"

        res += "Ids das entregas a realizar:\n"
        for entrega in self.entregasInconcluidas:
            res += str(entrega) + "\n"
        
        res += "\nIds das entregas realizadas:\n"
        for entrega in self.entregasConcluidas:
            res += str(entrega) + "\n"
        
        res += f"\nO estafeta realizou um total de {self.nrEntregasConcluidas} obtendo um ranking total de {self.ranking}."

        return res
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
