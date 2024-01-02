class MeioTransporte():
    def __init__(self, nome, pesoMax, velocidade, decrescimo):
        """
        Initializes a new instance of the MeioTransporte class.

        Args:
            nome (str): The name of the meio de transporte.
            pesoMax (float): The maximum weight capacity of the meio de transporte in kilograms.
            velocidade (float): The average speed of the meio de transporte in kilometers per hour.
            decrescimo (float): The speed decrease per kilogram of cargo.

        """
        self.nome = nome
        self.pesoMax = pesoMax
        self.velocidade = velocidade
        self.decrescimo = decrescimo
    
    def getNome(self):
        """
        Returns the name of the MeioTransporte object.
        """
        return self.nome
    
    def getPesoMax(self):
        """
        Returns the maximum weight capacity of the MeioTransporte object in kilograms.
        """
        return self.pesoMax
    
    def getVelocidade(self):
        """
        Returns the average speed of the MeioTransporte object in kilometers per hour.
        """
        return self.velocidade
    
    def getDecrescimo(self):
        """
        Returns the speed decrease per kilogram of cargo for the MeioTransporte object.
        """
        return self.decrescimo
    
    def setNome(self, nome):
        """
        Sets the name of the MeioTransporte object.

        Args:
            nome (str): The new name of the meio de transporte.
        """
        self.nome = nome

    def setPesoMax(self, pesoMax):
        """
        Sets the maximum weight capacity of the MeioTransporte object.

        Args:
            pesoMax (float): The new maximum weight capacity in kilograms.
        """
        self.pesoMax = pesoMax

    def setVelocidade(self, velocidade):
        """
        Sets the average speed of the MeioTransporte object.

        Args:
            velocidade (float): The new average speed in kilometers per hour.
        """
        self.velocidade = velocidade

    def setDecrescimo(self, decrescimo):
        """
        Sets the speed decrease per kilogram of cargo for the MeioTransporte object.

        Args:
            decrescimo (float): The new speed decrease per kilogram.
        """
        self.decrescimo = decrescimo

    def __str__(self):
        """
        Returns a string representation of the MeioTransporte object.
        """
        return f"Meio de Transporte ({self.nome}) - Peso Máximo = {self.pesoMax}kg e Velocidade Média = {self.velocidade}km/h, sendo que há um descréscimo de {self.decrescimo}km/h por cada kg de carga."
    
    def __eq__(self, other):
        """
        Checks if two MeioTransporte objects are equal.

        Args:
            other (MeioTransporte): The other MeioTransporte object to compare.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        return self.nome == other.nome

    def __hash__(self):
        """
        Returns the hash value of the MeioTransporte object.
        """
        return hash(self.nome)
    
    def addEstafeta(self, estafeta):
        """
        Adds an estafeta to the MeioTransporte object.

        Args:
            estafeta (Estafeta): The estafeta to add.
        """
        self.estafetas.append(estafeta)