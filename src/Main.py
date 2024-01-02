from HealthPlanet import HealthPlanet
from Estafeta import Estafeta
from Entrega import Entrega

def main():

    # Instância o grafo responsável pela gestão das entregas
    healthPlanet = HealthPlanet()

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
    healthPlanet.addIntercecao("Arcozelo", "Avenida João Duarte", (41.537861, -8.615156), "Barcelos", "Avenida Dom Nuno Álvares Pereira", (41.536537, -8.618139), 0.35)
    healthPlanet.addIntercecao("Barcelos", "Rua Arquitecto Borges Vinagre", (41.536004, -8.614188), "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), 0.15)
    healthPlanet.addIntercecao("Arcozelo", "Avenida João Duarte", (41.537861, -8.615156), "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), 0.3)
    healthPlanet.addIntercecao("Barcelos", "Largo dos Capuchinhos", (41.534635, -8.615340), "Barcelos", "Campo 25 de Abril", (41.535469, -8.615419), 0.1)
    healthPlanet.addIntercecao("Barcelos", "Largo dos Capuchinhos", (41.534635, -8.615340), "Barcelos", "Avenida dos Combatentes da Grande Guerra", (41.534115, -8.616281), 0.1)
    healthPlanet.addIntercecao("Barcelos", "Avenida dos Combatentes da Grande Guerra", (41.534115, -8.616281), "Barcelos", "Avenida Dom Nuno Álvares Pereira", (41.536537, -8.618139), 0.35)
    healthPlanet.addIntercecao("Barcelos", "Campo 25 de Abril", (41.535469, -8.615419), "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), 0.35)
    healthPlanet.addIntercecao("Barcelos", "Largo dos Capuchinhos", (41.534635, -8.615340), "Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), 0.35)
    healthPlanet.addIntercecao("Barcelos", "Rua Arquitecto Borges Vinagre", (41.536004, -8.614188), "Arcozelo", "Rua Elias Garcia", (41.536377, -8.611988), 0.22)
    healthPlanet.addIntercecao("Arcozelo", "Rua Doutor José Júlio Vieira Ramos", (41.537223, -8.613382), "Arcozelo", "Rua Elias Garcia", (41.536377, -8.611988), 0.55)
    healthPlanet.addIntercecao("Barcelos", "Largo dos Capuchinhos", (41.534635, -8.615340), "Arcozelo", "Rua Elias Garcia", (41.536377, -8.611988), 0.35)
    healthPlanet.addIntercecao("Arcozelo", "Rua Dom Afonso", (41.537089, -8.612683), "Arcozelo", "Rua Elias Garcia", (41.536377, -8.611988), 0.11)

    # Insere os estafetas
    healthPlanet.addEstafeta("Beatriz", [0], 5)
    healthPlanet.addEstafeta("Paulo", [1,2,3], 5)
    healthPlanet.addEstafeta("Cris", [4,5,6,7,8], 5)
    healthPlanet.addEstafeta("Araújo", [9], 5)
    healthPlanet.addEstafeta("Pinto", [10,11], 5)
    healthPlanet.addEstafeta("Madalena", [12,13,14,15,16,17,18,19,20,21,22], 5)

    # Insere os meios de transporte disponíveis para os estafetas
    healthPlanet.addMeioTransporte("Bicicleta", 5, 10, 0.6)
    healthPlanet.addMeioTransporte("Moto", 20, 35, 0.5)
    healthPlanet.addMeioTransporte("Carro", 100, 50, 0.1)

    # Insere as entregas
    healthPlanet.addEntrega(25, 45.5, "Barcelos", "Rua Doutor Francisco Torres", 678, 0)
    healthPlanet.addEntrega(10, 20, "Barcelos", "Rua Padre Alfredo da Rocha Martins", 200, 1)
    healthPlanet.addEntrega(12, 9, "Barcelos", "Rua Arquitecto Borges Vinagre", 230, 1)
    healthPlanet.addEntrega(30, 17, "Arcozelo", "Avenida João Duarte", 225, 1)
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

    '''
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
                option_entregar = input("Pretende usar uma estratégia determinística? (S ou N): ")
                if option_entregar.capitalize=="S":
                    print("\n---REALIZAR ENTREGAS (determinística)---\n")
                    idEstafeta = int(input("Id do Estafeta: "))
                    idsEntregas = eval(input("Ids das Entregas que deseja fazer agora (formato [1,2,3,...]): "))
                    # Completar



                elif option_entregar.capitalize=="N":
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

        except ValueError:
            print("Input inválido.")
        '''
    
if __name__ == "__main__":
    main()