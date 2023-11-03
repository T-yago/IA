class MeioTransporte():
    def __init__(self, nome, pesoMax, velocidade):
        self.nome = nome
        self.pesoMax = pesoMax
        self.velocidade = velocidade
    
    def getNome(self):
        return self.nome
    
    def getPesoMax(self):
        return self.pesoMax
    
    def getVelocidade(self):
        return self.velocidade
    
    def setNome(self, nome):
        self.nome = nome

    def setPesoMax(self, pesoMax):
        self.pesoMax = pesoMax

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

    def __str__(self):
        return f"Meio de Transporte ({self.nome}) - Peso Máximo = {self.pesoMax}kg e Velocidade Média = {self.velocidade}km/h."

    def __repr__(self):
        return f"Meio de Transporte ({self.nome}) - Peso Máximo = {self.pesoMax}kg e Velocidade Média = {self.velocidade}km/h."
    
    def __eq__(self, other):
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)