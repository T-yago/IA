from Graph import *
from Entrega import *
from Estafeta import *

class HealthPlanet():
    def __init__(self, estafetas={}, entregas = {}):
        self.estafetas = estafetas # Dicionário (ID Estafeta -> Estafeta)
        self.entregas = entregas # Dicionário (ID Entrega -> Entrega)
    
