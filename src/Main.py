from HealthPlanet import HealthPlanet
from Estafeta import Estafeta


def main():

    # Instância o grafo responsável pela gestão das entregas
    healthPlanet = HealthPlanet()

    # Insere as ruas das freguesias (Altera para outras ruas Tugs)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)
    healthPlanet.addLocalizacao("Vila Boa", "Travessa da Estrada", "Vila Boa", "Rua do Seminário", 4)

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

    # Insere as entregas (Altera para localizações que estejam no grafo Tuga)
    healthPlanet.addEntrega(25, 45.5, "Vila Boa", "Travessa da Estrada", 678, 0)
    healthPlanet.addEntrega(10, 20, "Vila Boa", "Travessa da Estrada", 200, 1)
    healthPlanet.addEntrega(12, 9, "Vila Boa", "Travessa da Estrada", 230, 1)
    healthPlanet.addEntrega(30, 17, "Vila Boa", "Travessa da Estrada", 225, 1)
    healthPlanet.addEntrega(2, 67, "Vila Boa", "Travessa da Estrada", 260, 2)
    healthPlanet.addEntrega(1, 15, "Vila Boa", "Travessa da Estrada", 210, 2)
    healthPlanet.addEntrega(23, 10, "Vila Boa", "Travessa da Estrada", 220, 2)
    healthPlanet.addEntrega(45, 45, "Vila Boa", "Travessa da Estrada", 300, 2)
    healthPlanet.addEntrega(66, 54, "Vila Boa", "Travessa da Estrada", 320, 2)
    healthPlanet.addEntrega(12, 90, "Vila Boa", "Travessa da Estrada", 270, 3)
    healthPlanet.addEntrega(8, 0.5, "Vila Boa", "Travessa da Estrada", 400, 4)
    healthPlanet.addEntrega(9, 14.4, "Vila Boa", "Travessa da Estrada", 227, 4)
    healthPlanet.addEntrega(19, 20.7, "Vila Boa", "Travessa da Estrada", 325, 5)
    healthPlanet.addEntrega(4, 5.4, "Vila Boa", "Travessa da Estrada", 456, 5)
    healthPlanet.addEntrega(3, 21.3, "Vila Boa", "Travessa da Estrada", 476, 5)
    healthPlanet.addEntrega(75, 10, "Vila Boa", "Travessa da Estrada", 235, 5)
    healthPlanet.addEntrega(22, 5, "Vila Boa", "Travessa da Estrada", 127, 5)
    healthPlanet.addEntrega(2.5, 1, "Vila Boa", "Travessa da Estrada", 100, 5)
    healthPlanet.addEntrega(65.3, 0.5, "Vila Boa", "Travessa da Estrada", 67, 5)
    healthPlanet.addEntrega(23.2, 10.3, "Vila Boa", "Travessa da Estrada", 200, 5)
    healthPlanet.addEntrega(2.7, 5, "Vila Boa", "Travessa da Estrada", 245, 5)
    healthPlanet.addEntrega(0.3, 2.5, "Vila Boa", "Travessa da Estrada", 575, 5)
    healthPlanet.addEntrega(36, 4, "Vila Boa", "Travessa da Estrada", 612, 5)

    # Interface do Utilizador
    exit = False
    while not exit:
        option = input("\n\nQue operação pretende executar?\n1 -> Adicionar um estafeta;\n2 -> Adicionar uma entrega;\n3 -> Adicionar uma nova localização;\n4 -> Executar entregas.\n5 -> Ver as informações relativas a um estafeta e as suas entregas.\n\n")
        
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

            else:
                print("Operação inválida. Insira uma das opções disponíveis.")

        except ValueError:
            print("Input inválido.")







if __name__ == "__main__":
    main()