
"""
Classe que representa um estafeta.
"""
class Estafeta():

    def __init__(self, id, nome, idsEntregas=[], ranking=5):
        self.id = id                                                # Id do estafeta
        self.nome = nome                                            # Nome do estafeta
        self.nrEntregasConcluidas = 0                               # Número de entregas realizadas
        self.entregasInconcluidas = idsEntregas                     # Lista dos ids das entrgas por realizar
        self.entregasConcluidas = []                                # Lista dos ids das entregas realizadas
        self.ranking = ranking                                      # Ranking total do estafeta

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

    def getEntregas(self):
        return self.entregasInconcluidas + self.entregasConcluidas
    
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

    """
    Completa uma lista de entregas, atualizando as entregas inconcluídas, concluídas, o número de entregas realizadas
    e o ranking total do estafeta
    """
    def completeEntregas(self, entregas):
        self.ranking = self.ranking * self.nrEntregasConcluidas
        for id, ranking in entregas:
            if (id in self.entregasInconcluidas):
                self.entregasInconcluidas.remove(id)
                self.entregasConcluidas.append(id)
                self.nrEntregasConcluidas += 1
                self.ranking += ranking
        
        self.ranking = round(self.ranking / self.nrEntregasConcluidas, 2)
    
    """
    Adiciona uma nova entrega à lista de entregas pendentes
    """
    def addEntrega(self, idEntrega):
        self.entregasInconcluidas.append(idEntrega)

    """
        Devolve uma string representativa da informação do estafeta
        """
    def __str__(self):
        res = f"Estafeta nº{self.id}: {self.nome}\n"

        res += "Ids das entregas a realizar: "
        res += ', '.join(str(element) for element in self.entregasInconcluidas)
        
        res += "\nIds das entregas realizadas: "
        res += ', '.join(str(element) for element in self.entregasConcluidas)
        
        res += f"\nO estafeta realizou um total de {self.nrEntregasConcluidas} entregas obtendo um ranking total de {self.ranking}."

        return res
    
    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)