import datetime
import random
from Graph import *
from Entrega import *
from Estafeta import *
from MeioTransporte import *

"""
Classe que implementa a lógica principal do sistema, fornecendo métodos para adicionar todo o tipo de entidades
(meios de transporte, ruas, estafetas, entregas) e disponibiliza os métodos para calcular as melhores rotas possíveis
para entregar um conjunto de encomendas X. A classe oferece ainda o método responsável por concluir as enrtegas e atualizar
as informações de um estafeta associadas à realização de uma travessia.
"""
class HealthPlanet():

    def __init__(self):
        self.grafo = Grafo()                        # Grafo representativo do mapa
        self.estafetas = {}                         # Estafetas (Id: Estefeta)
        self.entregasPendentes = {}                 # Entregas Pendentes (Id: Entrega)
        self.entregasConcluidas = {}                # Entregas Concluídas (Id: Entrega)
        self.meiosTransporte = {}                   # Meios de Transporte da Empresa (Nome: Meio de Transporte)


    """
    Função responsável por criar um estafeta e adicioná-lo ao dicionário de estafetas da empresa.
    """
    def addEstafeta(self, nomeEstafeta, entregas, ranking):
        idEstafeta = len(self.estafetas)
        newEstafeta = Estafeta(idEstafeta, nomeEstafeta, entregas, ranking)
        self.estafetas[idEstafeta] = newEstafeta
    
    """
    Função responsável por criar um meio de transporte e adicioná-lo ao dicionário de meios de transporte da empresa.
    """
    def addMeioTransporte(self, nome, pesoMax, velocidade, decrescimo):
        self.meiosTransporte[nome] = MeioTransporte(nome, pesoMax, velocidade, decrescimo)
    
    """
    Função responsável por criar uma entrega e adicioná-la ao dicionário de entregas pendentes da empresa.
    """
    def addEntrega(self, peso, volume, freguesia, rua, prazo, idEstafeta = None):
        if idEstafeta==None or idEstafeta not in self.estafetas:
            # Escolhe o id de um estafeta aleatório
            nEstafetas = len(self.estafetas)
            random_id = random.randint(0, nEstafetas)
            self.estafetas[idEstafeta].addEntrega(random_id)
        idEntrega = len(self.entregasPendentes) + len(self.entregasConcluidas)
        self.entregasPendentes[idEntrega] = Entrega(idEntrega, peso, volume, freguesia, rua, prazo, idEstafeta)

    """
    Função responsável por adicionar uma rua ao mapa de ruas, ou seja, adicionar um vértice representativo da rua ao grafo.
    """
    def addIntercecao(self, freguesia1, rua1, coordenadas1, freguesia2, rua2, coordenadas2, distancia):
        nome1 = freguesia1 + ", " + rua1
        nome2 = freguesia2 + ", " + rua2
        self.grafo.add_edge(nome1, coordenadas1, nome2, coordenadas2, distancia)
    
    """
    Função responsável por returnar uma string representativa de toda a informação relativa a um estafeta, incluindo ainda
    a informação relativa às entregas associadas a este, quer estejam completas ou incompletas
    """
    def getInfoEstafeta(self, idEstafeta):
        res = self.estafetas[idEstafeta].__str__() + "\n\nEntregas:\n"
        idsEntregasConcluidas = self.estafetas[idEstafeta].getEntregasConcluidas()
        for idEntrega in idsEntregasConcluidas:
            res += self.entregasConcluidas[idEntrega].__str__() + "\n"
        idsEntregasInconcluidas = self.estafetas[idEstafeta].getEntregasInconcluidas()
        for idEntrega in idsEntregasInconcluidas:
            res += self.entregasPendentes[idEntrega].__str__() + "\n"

        return res[:-1]
