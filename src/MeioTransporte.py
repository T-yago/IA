class MeioTransporte():
    def __init__(self, nome, pesoMax, velocidade, decrescimo, estafetas):
        self.nome = nome
        self.pesoMax = pesoMax
        self.velocidade = velocidade
        self.decrescimo = decrescimo
        self.estafetas = estafetas
    
    def getNome(self):
        return self.nome
    
    def getPesoMax(self):
        return self.pesoMax
    
    def getVelocidade(self):
        return self.velocidade
    
    def getDecrescimo(self):
        return self.decrescimo
    
    def getEstafetas(self):
        return self.estafetas
    
    def setNome(self, nome):
        self.nome = nome

    def setPesoMax(self, pesoMax):
        self.pesoMax = pesoMax

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

    def setDecrescimo(self, decrescimo):
        self.decrescimo = decrescimo

    def setEstafetas(self, estafetas):
        self.estafetas = estafetas

    def __str__(self):
        printEstafetas = ""
        for estafeta in self.estafetas:
            printEstafetas += estafeta.getNome() + ", "
        printEstafetas = printEstafetas[:-2]

        return f"Meio de Transporte ({self.nome}) - Peso Máximo = {self.pesoMax}kg e Velocidade Média = {self.velocidade}km/h, sendo que há um descréscimo de {self.decrescimo}km/h por cada kg de carga. Estafetas - {printEstafetas}"

    def __repr__(self):
        printEstafetas = ""
        for estafeta in self.estafetas:
            printEstafetas += estafeta.getNome() + ", "
        printEstafetas = printEstafetas[:-2]
    
        return f"Meio de Transporte ({self.nome}) - Peso Máximo = {self.pesoMax}kg e Velocidade Média = {self.velocidade}km/h, sendo que há um descréscimo de {self.decrescimo}km/h por cada kg de carga. Estafetas - {printEstafetas}"
    
    def __eq__(self, other):
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)
    
    def addEstafeta(self, estafeta):
        self.estafetas.append(estafeta)