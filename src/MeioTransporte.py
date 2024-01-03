
"""
Classe que representa um meio de transporte.
"""
class MeioTransporte():

    def __init__(self, nome, pesoMax, velocidade, decrescimo):
        self.nome = nome
        self.pesoMax = pesoMax
        self.velocidade = velocidade
        self.decrescimo = decrescimo
    
    def getNome(self):
        return self.nome
    
    def getPesoMax(self):
        return self.pesoMax
    
    def getVelocidade(self):
        return self.velocidade
    
    def getDecrescimo(self):
        return self.decrescimo
    
    def setNome(self, nome):
        self.nome = nome

    def setPesoMax(self, pesoMax):
        self.pesoMax = pesoMax

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

    def setDecrescimo(self, decrescimo):
        self.decrescimo = decrescimo

    """
    Devolve uma string representativa da informação do meio de transporte
    """
    def __str__(self):
        return f"Meio de Transporte ({self.nome}) - Peso Máximo = {self.pesoMax}kg e Velocidade Média = {self.velocidade}km/h, sendo que há um descréscimo de {self.decrescimo}km/h por cada kg de carga."
    
    def __eq__(self, other):
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)
