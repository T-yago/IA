from Graph import *
from Entrega import *
from Estafeta import *
from MeioTransporte import *

class HealthPlanet():
    estafetas = {}
    entregas = {}
    
    meiosTransporte = {}
    meiosTransporte["Bicicleta"] = MeioTransporte("Bicicleta", 5, 10)
    meiosTransporte["Moto"] = MeioTransporte("Moto", 20, 35)
    meiosTransporte["Carro"] = MeioTransporte("Carro", 100, 50)
    