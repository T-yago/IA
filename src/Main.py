import time
from HealthPlanet import HealthPlanet
from Estafeta import Estafeta
from Entrega import Entrega

def main():

    # Instância o grafo responsável pela gestão das entregas
    healthPlanet = HealthPlanet("Barcelos, Rua Doutor Francisco Torres")

    '''
    RUAS (11): 
        - Rua Doutor Francisco Torres (Barcelos) (41.535186, -8.616254)
        - Campo 25 de Abril (Barcelos) (41.535469, -8.615419)
        - Rua Padre Alfredo da Rocha Martins (Barcelos) (41.535896, -8.616541)
        - Rua Arquitecto Borges Vinagre (Barcelos) (41.536004, -8.614188)
        - Largo dos Capuchinhos (Barcelos) (41.534635, -8.615340)
        - Avenida dos Combatentes da Grande Guerra (Barcelos) (41.534115, -8.616281)
        - Avenida Dom Nuno Álvares Pereira (Barcelos) (41.536537, -8.618139)
        - Rua Doutor José Júlio Vieira Ramos (Arcozelo) (41.537223, -8.613382)
        - Rua Elias Garcia (Arcozelo) (41.536377, -8.611988)
        - Avenida João Duarte (Arcozelo) (41.537861, -8.615156)
        - Rua Dom Afonso (Arcozelo) (41.537089, -8.612683)
        '''

    # Insere as interceções
    healthPlanet.addIntercecao("Barcelos", "Rua Doutor Francisco Torres", (41.535186, -8.616254), "Barcelos", "Campo 25 de Abril", (41.535469, -8.615419), 0.12)
    healthPlanet.addIntercecao("Barcelos", "Rua Doutor Francisco Torres", (41.535186, -8.616254), "Barcelos", "Avenida Dom Nuno Álvares Pereira", (41.536537, -8.618139), 0.3)
    healthPlanet.addIntercecao("Barcelos", "Rua Padre Alfredo da Rocha Martins", (41.535896, -8.616541), "Barcelos", "Campo 25 de Abril", (41.535469, -8.615419), 0.15)
    healthPlanet.addIntercecao("Barcelos", "Rua Padre Alfredo da Rocha Martins", (41.535896, -8.616541), "Barcelos", "Avenida Dom Nuno Álvares Pereira", (41.536537, -8.618139), 0.2)
    healthPlanet.addIntercecao("Barcelos", "Rua Padre Alfredo da Rocha Martins", (41.535896, -8.616541), "Barcelos", "Rua Arquitecto Borges Vinagre", (41.536004, -8.614188), 0.2)
    healthPlanet.addIntercecao("Barcelos", "Rua Arquitecto Borges Vinagre", (41.536004, -8.614188), "Barcelos", "Campo 25 de Abril", (41.535469, -8.615419), 0.2)
    healthPlanet.addIntercecao("Barcelos", "Rua Arquitecto Borges Vinagre", (41.536004, -8.614188), "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), 0.15)
    healthPlanet.addIntercecao("Barcelos", "Rua Arquitecto Borges Vinagre", (41.536004, -8.614188), "Arcozelo", "Rua Elias Garcia", (41.536377, -8.611988), 0.22)
    healthPlanet.addIntercecao("Arcozelo", "Avenida João Duarte", (41.537861, -8.615156), "Barcelos", "Avenida Dom Nuno Álvares Pereira", (41.536537, -8.618139), 0.35)
    healthPlanet.addIntercecao("Arcozelo", "Avenida João Duarte", (41.537861, -8.615156), "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), 0.3)
    healthPlanet.addIntercecao("Barcelos", "Largo dos Capuchinhos", (41.534635, -8.615340), "Barcelos", "Campo 25 de Abril", (41.535469, -8.615419), 0.1)
    healthPlanet.addIntercecao("Barcelos", "Largo dos Capuchinhos", (41.534635, -8.615340), "Barcelos", "Avenida dos Combatentes da Grande Guerra", (41.534115, -8.616281), 0.1)
    healthPlanet.addIntercecao("Barcelos", "Largo dos Capuchinhos", (41.534635, -8.615340), "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), 0.35)
    healthPlanet.addIntercecao("Barcelos", "Largo dos Capuchinhos", (41.534635, -8.615340), "Arcozelo", "Rua Elias Garcia", (41.536377, -8.611988), 0.35)
    healthPlanet.addIntercecao("Barcelos", "Avenida dos Combatentes da Grande Guerra", (41.534115, -8.616281), "Barcelos", "Avenida Dom Nuno Álvares Pereira", (41.536537, -8.618139), 0.35)
    healthPlanet.addIntercecao("Barcelos", "Campo 25 de Abril", (41.535469, -8.615419), "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), 0.35)
    healthPlanet.addIntercecao("Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), "Arcozelo", "Rua Elias Garcia", (41.536377, -8.611988), 0.55)
    healthPlanet.addIntercecao("Arcozelo", "Rua Dom Afonso", (41.537089, -8.612683), "Arcozelo", "Rua Elias Garcia", (41.536377, -8.611988), 0.11)
    healthPlanet.addIntercecao("Arcozelo", "Rua Dom Afonso", (41.537089, -8.612683), "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), 0.07)

    # Insere os estafetas
    healthPlanet.addEstafeta("Beatriz", [0], 5)
    healthPlanet.addEstafeta("Paulo", [1,2,3], 5)
    healthPlanet.addEstafeta("Cris", [4,5,6,7,8], 5)
    healthPlanet.addEstafeta("Araújo", [9], 5)
    healthPlanet.addEstafeta("Pinto", [10,11], 5)
    healthPlanet.addEstafeta("Madalena", [12,13,14,15,16,17,18,19,20,21,22], 5)

    # Insere os meios de transporte disponíveis para os estafetas
    healthPlanet.addMeioTransporte("Bicicleta", 5, 10, 0.6, 0.0)
    healthPlanet.addMeioTransporte("Moto", 20, 35, 0.5, 0.125)
    healthPlanet.addMeioTransporte("Carro", 100, 50, 0.1, 0.23)

    # Insere as entregas
    healthPlanet.addEntrega(25, 45.5, "Barcelos", "Rua Doutor Francisco Torres", 1, 0)
    healthPlanet.addEntrega(4, 20, "Barcelos", "Rua Padre Alfredo da Rocha Martins", 1, 1)
    healthPlanet.addEntrega(2, 9, "Barcelos", "Rua Arquitecto Borges Vinagre", 230, 1)
    healthPlanet.addEntrega(2.5, 17, "Arcozelo", "Avenida João Duarte", 225, 1)
    healthPlanet.addEntrega(2, 67, "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", 260, 2)
    healthPlanet.addEntrega(1, 15, "Barcelos", "Largo dos Capuchinhos", 210, 2)
    healthPlanet.addEntrega(23, 10, "Barcelos", "Avenida dos Combatentes da Grande Guerra", 220, 2)
    healthPlanet.addEntrega(45, 45, "Arcozelo", "Rua Elias Garcia", 300, 2)
    healthPlanet.addEntrega(66, 54, "Arcozelo", "Rua Dom Afonso", 320, 2)
    healthPlanet.addEntrega(12, 90, "Barcelos", "Campo 25 de Abril", 270, 3)
    healthPlanet.addEntrega(8, 0.5, "Barcelos", "Avenida Dom Nuno Álvares Pereira", 400, 4)
    healthPlanet.addEntrega(9, 14.4, "Barcelos", "Avenida dos Combatentes da Grande Guerra", 227, 4)
    healthPlanet.addEntrega(19, 20.7, "Arcozelo", "Rua Dom Afonso", 325, 5)
    healthPlanet.addEntrega(4, 5.4, "Barcelos", "Largo dos Capuchinhos", 456, 5)
    healthPlanet.addEntrega(3, 21.3, "Barcelos", "Avenida Dom Nuno Álvares Pereira", 476, 5)
    healthPlanet.addEntrega(75, 10, "Barcelos", "Rua Doutor Francisco Torres", 235, 5)
    healthPlanet.addEntrega(22, 5, "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", 127, 5)
    healthPlanet.addEntrega(2.5, 1, "Arcozelo", "Rua Elias Garcia", 100, 5)
    healthPlanet.addEntrega(65.3, 0.5, "Arcozelo", "Avenida João Duarte", 67, 5)
    healthPlanet.addEntrega(23.2, 10.3, "Barcelos", "Rua Arquitecto Borges Vinagre", 200, 5)
    healthPlanet.addEntrega(2.7, 5, "Arcozelo", "Rua Dom Afonso", 245, 5)
    healthPlanet.addEntrega(0.3, 2.5, "Barcelos", "Campo 25 de Abril", 575, 5)
    healthPlanet.addEntrega(36, 4, "Barcelos", "Rua Doutor Francisco Torres", 612, 5)

    """
    print("------------------------------------------------- TESTE 1 -------------------------------------------------")
    print("DFS -> " + str(healthPlanet.grafo.procura_DFS("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("IDDFS -> " + str(healthPlanet.grafo.procura_IDDFS("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", 20, print_visited = True)) + "\n")
    print("BFS -> " + str(healthPlanet.grafo.procura_BFS("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("UCS -> " + str(healthPlanet.grafo.procura_UCS("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Dijkstra -> " + str(healthPlanet.grafo.procura_dijkstra("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Bellman Ford -> "+ str(healthPlanet.grafo.procura_bellman_ford("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Floyd Warshall -> "+ str(healthPlanet.grafo.procura_floyd_warshall("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Random Walk -> "+ str(healthPlanet.grafo.random_walk("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("A* -> " + str(healthPlanet.grafo.procura_aStar("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("IDA* -> " + str(healthPlanet.grafo.procura_IDAstar("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Greedy -> " + str(healthPlanet.grafo.procuraGreedy("Arcozelo, Rua Doutor José Júlio Vieira Ramos", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")

    print("------------------------------------------------- TESTE 2 -------------------------------------------------")
    print("\n" + "DFS -> " + str(healthPlanet.grafo.procura_DFS("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("IDDFS -> " + str(healthPlanet.grafo.procura_IDDFS("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", 20, print_visited = True)) + "\n")
    print("BFS -> " + str(healthPlanet.grafo.procura_BFS("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("UCS -> " + str(healthPlanet.grafo.procura_UCS("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Dijkstra -> " + str(healthPlanet.grafo.procura_dijkstra("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Bellman Ford -> "+ str(healthPlanet.grafo.procura_bellman_ford("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Floyd Warshall -> "+ str(healthPlanet.grafo.procura_floyd_warshall("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Random Walk -> "+ str(healthPlanet.grafo.random_walk("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("A* -> " + str(healthPlanet.grafo.procura_aStar("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("IDA* -> " + str(healthPlanet.grafo.procura_IDAstar("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")
    print("Greedy -> " + str(healthPlanet.grafo.procuraGreedy("Barcelos, Avenida Dom Nuno Álvares Pereira", "Arcozelo, Rua Elias Garcia", print_visited = True)) + "\n")

    print("------------------------------------------------- TESTE 3 -------------------------------------------------")
    print("\n" + "DFS -> " + str(healthPlanet.grafo.procura_DFS("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    print("IDDFS -> " + str(healthPlanet.grafo.procura_IDDFS("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", 20, print_visited = True)) + "\n")
    print("BFS -> " + str(healthPlanet.grafo.procura_BFS("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    print("UCS -> " + str(healthPlanet.grafo.procura_UCS("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    print("Dijkstra -> " + str(healthPlanet.grafo.procura_dijkstra("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    print("Bellman Ford -> "+ str(healthPlanet.grafo.procura_bellman_ford("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    print("Floyd Warshall -> "+ str(healthPlanet.grafo.procura_floyd_warshall("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    print("Random Walk -> "+ str(healthPlanet.grafo.random_walk("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    print("A* -> " + str(healthPlanet.grafo.procura_aStar("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    print("IDA* -> " + str(healthPlanet.grafo.procura_IDAstar("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    print("Greedy -> " + str(healthPlanet.grafo.procuraGreedy("Arcozelo, Avenida João Duarte", "Barcelos, Largo dos Capuchinhos", print_visited = True)) + "\n")
    """

    # Interface do Utilizador
    exit = False
    while not exit:
        option = input("\n\nQue operação pretende executar?\n1 -> Adicionar um estafeta;\n2 -> Adicionar uma entrega;\n3 -> Adicionar uma nova localização;\n4 -> Executar entregas.\n5 -> Ver as informações relativas a um estafeta e as suas entregas.\n6 -> Sair\n\n")
        

        try:
            option = int(option)

            if option==1:
                print("\n---ADICIONAR ESTAFETA---\n")
                nome = input("Nome: ")
                ids = eval(input("Ids das entregas a realizar (formato [1,2,3,...]): "))
                healthPlanet.addEstafeta(nome, ids, 5)
            elif option==2:
                print("\n---ADICIONAR ENTREGA---\n")
                peso = int(input("Peso: "))
                volume = int(input("Volume: "))
                freguesia = input("Freguesia: ")
                rua = input("Rua: ")
                prazo = input("Prazo (em minutos em relação à data e hora atual): ")
                healthPlanet.addEntrega(peso, volume, freguesia, rua, prazo)
            elif option==3:
                print("\n---ADICIONAR NOVA LOCALIZAÇÃO---\n")
                freguesia1 = input("Freguesia (Primeira): ")
                rua1 = input("Rua (Primeira): ")
                freguesia2 = input("Freguesia (Segunda): ")
                rua2 = input("Rua (Segunda): ")
                distancia = int(input("Distancia: "))
                healthPlanet.addLocalizacao(freguesia1, rua1, freguesia2, rua2, distancia)
            elif option==4:
                print("\n---REALIZAR ENTREGAS---\n")
                option_entregar = input("Pretende usar uma estratégia determinística? (S ou N)\n\n")
                if option_entregar.capitalize()=="S":
                    print("\n---REALIZAR ENTREGAS (determinística)---\n")
                    idEstafeta = int(input("Id do Estafeta: "))
                    idsEntregas = eval(input("Ids das Entregas que deseja fazer agora (formato [1,2,3,...]): "))
                    metodoProcura = int(input("\nQuer utilizar que método de procura?\n\nPesquisas Não Informadas:\n1 -> Depth-first search (DFS);\n2 -> Breadth-first search (BFS);\n3 -> Iterative Deepening Depth-First Search (IDDFS);\n4 -> Uniform Cost Search (UCS);\n5 -> Dijkstra's Search;\n6 -> Bellman-Ford Search;\n7 -> Floyd-Warshall Search;\n8 -> random walk Search;\n\nPesquisas Informadas:\n9 -> Greedy Search;\n10 -> A* Search;\n11 -> Iterative Deepening A* Search\n\n"))
                    visualizarExpansao = input("Pretende visualizar a expansão dos nodos? (S ou N) ")
                    if visualizarExpansao.capitalize()=="S":
                        visualizarExpansao = True
                    else:
                        visualizarExpansao = False
                    comeco = time.time()
                    result = healthPlanet.calcularMelhorRota(idEstafeta, idsEntregas, metodoProcura, visualizarExpansao)
                    fim = time.time()

                    # Calcula o tempo que demorou a executar a procura da melhor travessia para uma dada estratégia de procura
                    tempoExecucao = fim - comeco
                    tempoExecucao_minutos = int(tempoExecucao // 60)
                    tempoExecucao_segundos = int(tempoExecucao % 60)

                    print(f"\n\nINFO TRAVESSIA\n")
                    print(f"Melhor Caminho -> {result[0]}")
                    print(f"Distância Total -> {result[1]:.2f} Km.")
                    print(f"Tempo total -> {result[4]:.2f} minutos.")
                    print(f"Total dos atrasos -> {result[2]/60:.2f} minutos e {result[2]%60:.2f} segundos.")
                    print(f"CO2 total emitido -> {result[3]:.3f} Kg.")
                    print(f"\nTEMPO TOTAL A EXECUTAR A PROCURA -> {tempoExecucao_minutos} minutos e {tempoExecucao_segundos:.2f} segundos.")

                    estatisticasAvancadas = input("\n\nVer estatísticas avançadas da Travessia? (S ou N)\n\n")
                    if estatisticasAvancadas.capitalize()=="S":
                        print(f"\n\nINFO DETALHADO TRAVESSIA\n")
                        print(result[5])
                    
                    entregarEncomendas = input("\n\nDeseja executar a travessia e entregar as encomendas? (S ou N)\n\n")
                    if entregarEncomendas.capitalize()=="S":
                        healthPlanet.concluirEntregas(idEstafeta, idsEntregas, result[2], result[4])
                        print(f"\nTodas as encomendas foram entregues com sucesso.\n")

                elif option_entregar.capitalize()=="N":
                    print("\n---REALIZAR ENTREGAS (não determinística)---\n")
                    idEstafeta = int(input("Id do Estafeta: "))
                    idsEntregas = eval(input("Ids das Entregas que deseja fazer agora (formato [1,2,3,...]): "))
                    # Completar
                    

            elif option==5:
                print("\n---INFORMAÇÃO ESTAFETA---\n")
                idEstafeta = int(input("Id do Estafeta: "))
                print("\n")
                print(healthPlanet.getInfoEstafeta(idEstafeta))
            elif option==6:
                    exit = True

            else:
                print("Operação inválida. Insira uma das opções disponíveis.")
            
            if option!=6:
                continuar = input("\n\nDeseja realizar mais alguma operação? (S ou N)\n\n")
                if continuar.capitalize()=="N":
                    exit = True
        
        except ValueError:
            print("Input inválido.")







if __name__ == "__main__":
    main()