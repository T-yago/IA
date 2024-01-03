import datetime
import random
from Graph import *
from Entrega import *
from Estafeta import *
from MeioTransporte import *
from FuncoesAuxiliares import *

class HealthPlanet():
    def __init__(self, sede):
        self.sede = sede
        self.grafo = Grafo()
        self.estafetas = {}
        self.entregasPendentes = {}
        self.entregasConcluidas = {}
        self.meiosTransporte = {}
        self.coordenadas = {}

        self.coordenadas = {}

    def addEstafeta(self, nomeEstafeta, entregas, ranking):
        idEstafeta = len(self.estafetas)
        newEstafeta = Estafeta(idEstafeta, nomeEstafeta, entregas, ranking)
        self.estafetas[idEstafeta] = newEstafeta
    
    def addMeioTransporte(self, nome, pesoMax, velocidade, decrescimo, emissaoCO2):
        self.meiosTransporte[nome] = MeioTransporte(nome, pesoMax, velocidade, decrescimo, emissaoCO2)
    
    def addEntrega(self, peso, volume, freguesia, rua, prazo, idEstafeta = None):
        if idEstafeta==None or idEstafeta not in self.estafetas:
            # Escolhe o id de um estafeta aleatório
            nEstafetas = len(self.estafetas)
            random_id = random.randint(0, nEstafetas)
            self.estafetas[idEstafeta].addEntrega(random_id)
        idEntrega = len(self.entregasPendentes) + len(self.entregasConcluidas)
        self.entregasPendentes[idEntrega] = Entrega(idEntrega, peso, volume, freguesia, rua, prazo, idEstafeta)

    def addIntercecao(self, freguesia1, rua1, coordenadas1, freguesia2, rua2, coordenadas2, distancia):
        nome1 = freguesia1 + ", " + rua1
        nome2 = freguesia2 + ", " + rua2
        self.coordenadas[(freguesia1, rua1)] = coordenadas1
        self.coordenadas[(freguesia2, rua2)] = coordenadas2
        self.grafo.add_edge(nome1, nome2, distancia)
    
    def getInfoEstafeta(self, idEstafeta):
        res = self.estafetas[idEstafeta].__str__() + "\n\nEntregas:\n"
        idsEntregasConcluidas = self.estafetas[idEstafeta].getEntregasConcluidas()
        for idEntrega in idsEntregasConcluidas:
            res += self.entregasConcluidas[idEntrega].__str__() + "\n"
        idsEntregasInconcluidas = self.estafetas[idEstafeta].getEntregasInconcluidas()
        for idEntrega in idsEntregasInconcluidas:
            res += self.entregasPendentes[idEntrega].__str__() + "\n"

        return res[:-1]

    def calcularMelhorRota(self, idEstafeta, entregas, metodoDeProcura, indexTravessia = 1):

        melhorCusto = float('inf')
        melhorCaminho = []
        melhorAtraso = float('inf')
        melhorEmissaoCO2 = float('inf')
        tempoTotal = 0
        estatisticasAvancadasStrFinal = ""

        # Tenta realizar as entregas com todas as combinações possíveis de veículos de forma a obter a travessia com menos atrasos e mais ecológica
        for meioTransporte in self.meiosTransporte.values():

            custo = 0
            caminho = []
            atraso = 0
            emissaoCO2 = 0
            tempoTotalAux = 0
            estatisticasAvancadasStr = ""

            # Associa aos ids das entregas os seus pesos
            pesosEntregas = []
            for idEntrega in entregas:
                if idEntrega in self.estafetas[idEstafeta].getEntregasInconcluidas():
                    pesosEntregas.append([idEntrega, self.entregasPendentes[idEntrega].getPeso()])

            # Caso as entregas excedam a capacidade do veículo calcula todas as combinações possíveis de organizar as entregas em travessias diferentes
            entregasPrimeiraTravessiaCombinacoes = generate_combinations(pesosEntregas, meioTransporte.getPesoMax())
            for entregasPrimeiraTravessia in entregasPrimeiraTravessiaCombinacoes:
                idsEntregas = [idEntrega[0] for idEntrega in entregasPrimeiraTravessia]
                res = self.calcularMelhorRotaVeiculo(idEstafeta, idsEntregas, 1, meioTransporte)
                custo += res[1]
                caminho += res[0]
                atraso += res[2]
                emissaoCO2 += res[3]
                tempoTotalAux += res[4]
                # String que contêm dados mais específicos de cada travessia para depois apresentar ao utilizador
                estatisticasAvancadasStr += str(indexTravessia) + "ª Travessia: " + meioTransporte.getNome() + "\nEncomendas entregues: "
                for id in idsEntregas:
                    estatisticasAvancadasStr += str(id) + ", "
                estatisticasAvancadasStr = estatisticasAvancadasStr[:-2]
                estatisticasAvancadasStr += "\nPercurso: "
                for rua in caminho:
                    estatisticasAvancadasStr += rua + " -> "
                estatisticasAvancadasStr = estatisticasAvancadasStr[:-4]
                estatisticasAvancadasStr += "\nDistancia Percurso: " + str(round(custo, 2)) + " Km.\nTempo: " + str(round(tempoTotalAux, 2)) + " minutos.\nEmissao CO2: " + str(round(emissaoCO2, 3)) + " Kg.\nAtraso nas entregas: " + str(round(atraso, 2)) + " minutos.\n\n"

                # Entrega as entregas restantes se tiverem sobrado entregas no armazem
                restantesEntregas = []
                for idEntrega in entregas:
                    if idEntrega not in idsEntregas:
                        restantesEntregas.append(idEntrega)
                
                # Faz a recursiva das restantes encomendas
                if len(restantesEntregas)>0:
                    nextTravessia = self.calcularMelhorRota(idEstafeta, restantesEntregas, 1, indexTravessia+1)
                    custo += nextTravessia[1]
                    caminho += nextTravessia[0]
                    atraso += nextTravessia[2]
                    emissaoCO2 += nextTravessia[3]
                    tempoTotalAux += nextTravessia[4]
                    estatisticasAvancadasStr += nextTravessia[5]
                
                if atraso<melhorAtraso or (atraso<=melhorAtraso and emissaoCO2<melhorEmissaoCO2) or (atraso<=melhorAtraso and emissaoCO2<=melhorEmissaoCO2 and custo<melhorCusto):
                    melhorCusto = custo
                    melhorCaminho = caminho
                    melhorAtraso = atraso
                    melhorEmissaoCO2 = emissaoCO2
                    tempoTotal = tempoTotalAux
                    estatisticasAvancadasStrFinal = estatisticasAvancadasStr

        return (melhorCaminho, melhorCusto, melhorAtraso, melhorEmissaoCO2, tempoTotal, estatisticasAvancadasStrFinal)

    
    def calcularMelhorRotaVeiculo(self, idEstafeta, entregas, metodoDeProcura, meioTransporte, firstIteration=True, removeIndex = 0, pesoEntregas = 0, horaEstadoAtual = None):

        """
        Vai buscar o local de entrega de cada entrega, a data de entrega da mesma e o peso associado. Consideramos ainda que a hora de início da travessia é a hora atual. Este
        processo apenas é realizado na primeria chamada da função, poupando trabalho às iterações seguintes.

        Salientamos ainda que nesta primeira iteração, atribuímos à variável origin o nome da sede, pois assumí-mos que os estafetas saem sempre do armazem da empresa. 
        """
        if firstIteration:
            if horaEstadoAtual==None:
                horaEstadoAtual = datetime.now()

            locaisEntregas = []
            if idEstafeta in self.estafetas:
                for idEntrega in entregas:
                    locaisEntregas.append((self.entregasPendentes[idEntrega].getPontoDeEntrega(), self.entregasPendentes[idEntrega].getPrazo(), self.entregasPendentes[idEntrega].getPeso()))
                    pesoEntregas += self.entregasPendentes[idEntrega].getPeso()
            entregas = locaisEntregas
            origin = self.sede
        else:
            origin = entregas.pop(removeIndex)[0]

        # Usando DFS

        """
        Calcula o caminho mais curto pririzando caminhos sem atrasos mas mais longos, a caminhos mais curtos mas com atrasos maiores, de forma a assegurar o
        melhor serviço por parte da empresa e penalizando os estafetas ao mínimo na sua classificação (esta é calculada baseada no total dos atrasos). Priorizamos
        ainda emissões de CO2 menores a caminhos mais curtos (atrasos menores prevalecem sobre emissões de CO2 menores, pois a satisfação do cliente continua a ser
        a prioridade máxima), visto o objetivo do trabalho ser obter o resultado mais sustentável.
        """
        melhorCusto = float('inf')
        melhorCaminho = []
        melhorAtraso = float('inf')
        melhorEmissaoCO2 = float('inf')
        tempoTotal = 0
        for index, infoEntrega in enumerate(entregas):
            localEntrega = infoEntrega[0]
            prazo = infoEntrega[1]
            peso = infoEntrega[2]
            custo = 0
            caminho = []
            atraso = 0
            emissaoCO2 = 0
            tempoTotalAux = 0

            # Calcula um caminho entre dois pontos obrigatórios (entre sede e ponto de entrega ou entre pontos de entrega)
            procuraDFS = self.grafo.procura_DFS(origin, localEntrega)
            custo += procuraDFS[1]
            caminho += procuraDFS[0]
            tempoViagem = meioTransporte.calculaTempoEmMinutos(procuraDFS[1], pesoEntregas)
            horaChegada = horaEstadoAtual + timedelta(minutes=tempoViagem) # Calcula a que horas o estafeta chegou a determinado ponto tendo em conta o percurso já realizado e o peso da carga transportada
            if (prazo < horaChegada):
                atraso += (horaChegada - prazo).total_seconds() / 60
            emissaoCO2 += meioTransporte.calculaEmissaoCO2(procuraDFS[1])
            tempoTotalAux += tempoViagem

            # Executa a função para todas as ordens possíveis de visitar os pontos de entrega, assegurando o melhor resultado possível (para a estratégia de procura utilizada)
            nextEntrega = self.calcularMelhorRotaVeiculo(idEstafeta, entregas.copy(), 1, meioTransporte, False, index, pesoEntregas-peso, horaChegada)
            custo += nextEntrega[1]
            caminho += nextEntrega[0]
            atraso += nextEntrega[2]
            emissaoCO2 += nextEntrega[3]
            tempoTotalAux += nextEntrega[4]

            # Atualiza o valor da melhor travessia caso seja melhor que a anteriormente melhor registada
            if atraso<melhorAtraso or (atraso<=melhorAtraso and emissaoCO2<melhorEmissaoCO2) or (atraso<=melhorAtraso and emissaoCO2<=melhorEmissaoCO2 and custo<melhorCusto):
                melhorCusto = custo
                melhorCaminho = caminho
                melhorAtraso = atraso
                melhorEmissaoCO2 = emissaoCO2
                tempoTotal = tempoTotalAux
        
        # Utilizado para calcular o percurso de volta ao armazem, pois consideramos que o veículo tem de voltar de novo para o armazem, sendo necessário ter em conta esta travessia para o caminho mais curto
        if (len(entregas)==0):
            procuraDFS = self.grafo.procura_DFS(origin, self.sede)
            melhorCusto = procuraDFS[1]
            melhorCaminho = procuraDFS[0]
            melhorAtraso = 0
            emissaoCO2 = meioTransporte.calculaEmissaoCO2(procuraDFS[1])
            tempoTotal = meioTransporte.calculaTempoEmMinutos(procuraDFS[1], 0)
        
        return (melhorCaminho, melhorCusto, melhorAtraso, emissaoCO2, tempoTotal)
    
    
    def concluirEntregas(self, idEstafeta, idsEntregas, atrasoTotal, tempoEntrega):

        # Atualiza as informações das entregas
        rankingEntrega = 5 - atrasoTotal/10
        if rankingEntrega<=0:
                rankingEntrega = 0
        for idEntrega in idsEntregas:
            if idEntrega in self.entregasPendentes:
                entrega = self.entregasPendentes.pop(idEntrega)
                entrega.setDateTimeEntregue(entrega.getDateTimeCriada() + timedelta(minutes=tempoEntrega))
                entrega.setRankingEstafeta(rankingEntrega)
                self.entregasConcluidas[idEntrega] = entrega
        
        # Atualiza as informações do estafeta
        self.estafetas[idEstafeta].completeEntregas(idsEntregas, rankingEntrega)
