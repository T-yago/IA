import datetime
import random
from Graph import *
from Entrega import *
from Estafeta import *
from MeioTransporte import *
from FuncoesAuxiliares import *

"""
Classe que implementa a lógica principal do sistema, fornecendo métodos para adicionar todo o tipo de entidades
(meios de transporte, ruas, estafetas, entregas) e disponibiliza os métodos para calcular as melhores rotas possíveis
para entregar um conjunto de encomendas X. A classe oferece ainda o método responsável por concluir as enrtegas e atualizar
as informações de um estafeta associadas à realização de uma travessia.
"""
class HealthPlanet():
    def __init__(self, sede):
        self.sede = sede                            # Nome da rua onde fica o armazem da empresa (os veículos saem e retornam sempre lá)
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
    def addMeioTransporte(self, nome, pesoMax, velocidade, decrescimo, emissaoCO2):
        self.meiosTransporte[nome] = MeioTransporte(nome, pesoMax, velocidade, decrescimo, emissaoCO2)
    
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

    """
    Função responsável por calcular qual a melhor combinação de veículos a utilizar, bem como qual a melhor distribuição de encomendas que
    leva em cada viagem, de forma a obter a travessia com menos atrasos e mais ecológica. Esta devolve para além da distância associada a
    essa travessia, o tempo total da mesma, a emissão total de CO2 na mesma, o tempo total de atraso em relação aos prazos associados a cada
    entrega e ainda uma string que fornece uma análise mais detalhada da travessia.

    Importante salientar que como solução ótima nós consideramos a solução com um total de tempos de atraso menor, sendo que em caso de empate consideramos
    a travessia com menor emissões de CO2, e ainda se houver empate, a travessia que percorra uma menor distância. Isto, porque apesar do objetivo,
    ser encontrar a travessia mais ecológica, nós consideramos que minimizar os atrasos nas entregas é a prioridade máxima, de forma a assegurar um bom
    serviço e deixar os clientes o mais satisfeitos possíveis.
    """
    def calcularMelhorRota(self, idEstafeta, entregas, metodoDeProcura, visualizarExpansao, indexTravessia = 1):

        melhorCusto = float('inf')
        melhorCaminho = []
        melhorAtraso = float('inf')
        melhorEmissaoCO2 = float('inf')
        tempoTotal = 0
        estatisticasAvancadasStrFinal = ""

        # Tenta realizar as entregas com todas as combinações possíveis de veículos e todas as combinações de encomendas que leva em cada viagem de forma a obter a travessia com menos atrasos e mais ecológica
        for meioTransporte in self.meiosTransporte.values():

            custo = 0
            caminho = []
            atraso = 0
            emissaoCO2 = 0
            tempoTotalAux = 0
            estatisticasAvancadasStr = ""

            # Associa aos ids das entregas os seus pesos, para poder executar a seguir a função generate_combinations
            pesosEntregas = []
            for idEntrega in entregas:
                if idEntrega in self.estafetas[idEstafeta].getEntregasInconcluidas():
                    pesosEntregas.append([idEntrega, self.entregasPendentes[idEntrega].getPeso()])

            # Calcula todas as combinações possíveis de organizar as entregas em travessias diferentes
            entregasPrimeiraTravessiaCombinacoes = generate_combinations(pesosEntregas, meioTransporte.getPesoMax())
            for entregasPrimeiraTravessia in entregasPrimeiraTravessiaCombinacoes:
                idsEntregas = [idEntrega[0] for idEntrega in entregasPrimeiraTravessia]
                res = self.calcularMelhorRotaVeiculo(idEstafeta, idsEntregas, metodoDeProcura, meioTransporte, visualizarExpansao)
                custo += res[1]
                caminho = res[0]
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
                estatisticasAvancadasStr += "\nDistancia Percurso: " + str(round(custo, 2)) + " Km.\nTempo: " + str(tempoTotalAux/60) + " minutos e " + str(round(tempoTotalAux%60, 2)) + " segundos.\nEmissao CO2: " + str(round(emissaoCO2, 3)) + " Kg.\nAtraso nas entregas: " + str(round(atraso, 2)) + " minutos.\n\n"

                # Entrega as entregas restantes se tiverem sobrado entregas no armazem
                restantesEntregas = []
                for idEntrega in entregas:
                    if idEntrega not in idsEntregas:
                        restantesEntregas.append(idEntrega)
                
                # Faz a recursiva das restantes encomendas, podendo estas ser entregues com o mesmo meio de transporte ou não, dependendo de qual traz o melhor resultado
                if len(restantesEntregas)>0:
                    nextTravessia = self.calcularMelhorRota(idEstafeta, restantesEntregas, metodoDeProcura, visualizarExpansao, indexTravessia+1)
                    custo += nextTravessia[1]
                    caminho += nextTravessia[0]
                    atraso += nextTravessia[2]
                    emissaoCO2 += nextTravessia[3]
                    tempoTotalAux += nextTravessia[4]
                    estatisticasAvancadasStr += nextTravessia[5]
                
                # Atualiza o valor da melhor travessia caso seja melhor que a anteriormente melhor registada
                if atraso<melhorAtraso or (atraso<=melhorAtraso and emissaoCO2<melhorEmissaoCO2) or (atraso<=melhorAtraso and emissaoCO2<=melhorEmissaoCO2 and custo<melhorCusto):
                    melhorCusto = custo
                    melhorCaminho = caminho
                    melhorAtraso = atraso
                    melhorEmissaoCO2 = emissaoCO2
                    tempoTotal = tempoTotalAux
                    estatisticasAvancadasStrFinal = estatisticasAvancadasStr

        return (melhorCaminho, melhorCusto, melhorAtraso, melhorEmissaoCO2, tempoTotal, estatisticasAvancadasStrFinal)

    
    def calcularMelhorRotaVeiculo(self, idEstafeta, entregas, metodoDeProcura, meioTransporte, visualizarExpansao, firstIteration=True, removeIndex = 0, pesoEntregas = 0, horaEstadoAtual = None):

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
            if metodoDeProcura==1:
                procuraRes = self.grafo.procura_DFS(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==2: 
                procuraRes = self.grafo.procura_BFS(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==3: 
                procuraRes = self.grafo.procura_IDDFS(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==4: 
                procuraRes = self.grafo.procura_UCS(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==5: 
                procuraRes = self.grafo.procura_dijkstra(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==6: 
                procuraRes = self.grafo.procura_bellman_ford(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==7: 
                procuraRes = self.grafo.procura_floyd_warshall(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==8: 
                procuraRes = self.grafo.random_walk(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==9: 
                procuraRes = self.grafo.procuraGreedy(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==10: 
                procuraRes = self.grafo.procura_aStar(origin, localEntrega, print_visited=visualizarExpansao)
            elif metodoDeProcura==11: 
                procuraRes = self.grafo.procura_IDAstar(origin, localEntrega, print_visited=visualizarExpansao)
            custo += procuraRes[1]
            caminho += procuraRes[0]
            tempoViagem = meioTransporte.calculaTempoEmMinutos(procuraRes[1], pesoEntregas)
            horaChegada = horaEstadoAtual + timedelta(minutes=tempoViagem) # Calcula a que horas o estafeta chegou a determinado ponto tendo em conta o percurso já realizado e o peso da carga transportada
            if (prazo < horaChegada):
                atraso += (horaChegada - prazo).total_seconds() / 60
            emissaoCO2 += meioTransporte.calculaEmissaoCO2(procuraRes[1])
            tempoTotalAux += tempoViagem

            # Executa a função para todas as ordens possíveis de visitar os pontos de entrega, assegurando o melhor resultado possível (para a estratégia de procura utilizada)
            nextEntrega = self.calcularMelhorRotaVeiculo(idEstafeta, entregas.copy(), metodoDeProcura, meioTransporte, visualizarExpansao, False, index, pesoEntregas-peso, horaChegada)
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
            if metodoDeProcura==1:
                procuraRes = self.grafo.procura_DFS(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==2:
                procuraRes = self.grafo.procura_BFS(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==3: 
                procuraRes = self.grafo.procura_IDDFS(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==4: 
                procuraRes = self.grafo.procura_UCS(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==5: 
                procuraRes = self.grafo.procura_dijkstra(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==6: 
                procuraRes = self.grafo.procura_bellman_ford(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==7: 
                procuraRes = self.grafo.procura_floyd_warshall(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==8: 
                procuraRes = self.grafo.random_walk(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==9: 
                procuraRes = self.grafo.procuraGreedy(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==10: 
                procuraRes = self.grafo.procura_aStar(origin, self.sede, print_visited=visualizarExpansao)
            elif metodoDeProcura==11: 
                procuraRes = self.grafo.procura_IDAstar(origin, self.sede, print_visited=visualizarExpansao)
            melhorCusto = procuraRes[1]
            melhorCaminho = procuraRes[0]
            melhorAtraso = 0
            emissaoCO2 = meioTransporte.calculaEmissaoCO2(procuraRes[1])
            tempoTotal = meioTransporte.calculaTempoEmMinutos(procuraRes[1], 0)
        
        return (melhorCaminho, melhorCusto, melhorAtraso, emissaoCO2, tempoTotal)
    
    """
    Completa uma lista de entregas, removendo as entregas concluídas do dicionário de entregas pendentes e adicionando as mesmas
    ao dicionário de entregas concluídas. Atualiza ainda as informações do estafeta responsável por ter entregue as encomendas, bem
    como as informações das próprias entregas, nomeadamente, o ranking das entregas associado às mesmas e as suas datas de entrega.
    """
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
