
"""
Classe que representa um meio de transporte.
"""
class MeioTransporte():
    def __init__(self, nome, pesoMax, velocidade, decrescimo, emissaoCO2):
        """
        Inicializa uma instância da classe MeioTransporte.

        Args:
            nome (str): O nome do meio de transporte.
            pesoMax (float): O peso máximo suportado pelo meio de transporte.
            velocidade (float): A velocidade do meio de transporte.
            decrescimo (float): O decréscimo na velocidade do meio de transporte.
            emissaoCO2 (float): A emissão de CO2 do meio de transporte.
        """
        self.nome = nome
        self.pesoMax = pesoMax
        self.velocidade = velocidade
        self.decrescimo = decrescimo
        self.emissaoCO2 = emissaoCO2
    
    def getNome(self):
        """
        Retorna o nome do meio de transporte.

        :return: O nome do meio de transporte.
        """
        return self.nome
    
    def getPesoMax(self):
        """
        Retorna o peso máximo suportado pelo meio de transporte.

        :return: O peso máximo suportado pelo meio de transporte.
        """
        return self.pesoMax
    
    def getVelocidade(self):
        """
        Retorna a velocidade do meio de transporte.

        :return: A velocidade do meio de transporte.
        """
        return self.velocidade
    
    def getDecrescimo(self):
        """
        Retorna o decréscimo na velocidade do meio de transporte.

        :return: O decréscimo na velocidade do meio de transporte.
        """
        return self.decrescimo

    def getEmissaoCO2(self):
        """
        Retorna a emissão de CO2 do meio de transporte.

        :return: A emissão de CO2 do meio de transporte.
        """
        return self.emissaoCO2
    
    def setNome(self, nome):
        """
        Define o nome do meio de transporte.

        Args:
            nome (str): O novo nome do meio de transporte.
        """
        self.nome = nome

    def setPesoMax(self, pesoMax):
        """
        Define o peso máximo suportado pelo meio de transporte.

        Args:
            pesoMax (float): O novo peso máximo suportado pelo meio de transporte.
        """
        self.pesoMax = pesoMax

    def setVelocidade(self, velocidade):
        """
        Define a velocidade do meio de transporte.

        Args:
            velocidade (float): A nova velocidade do meio de transporte.
        """
        self.velocidade = velocidade

    def setDecrescimo(self, decrescimo):
        """
        Define o decréscimo na velocidade do meio de transporte.

        Args:
            decrescimo (float): O novo decréscimo na velocidade do meio de transporte.
        """
        self.decrescimo = decrescimo
    
    def setEmissaoCO2(self, emissaoCO2):
        """
        Define a emissão de CO2 do meio de transporte.

        Args:
            emissaoCO2 (float): A nova emissão de CO2 do meio de transporte.
        """
        self.emissaoCO2 = emissaoCO2

    def calculaTempoEmMinutos(self, distancia, peso):
        """
        Calcula o tempo que demorou uma deslocação, com base no peso da carga e da distância percorrida.

        Args:
            distancia (float): A distância percorrida.
            peso (float): O peso da carga.

        Returns:
            float: O tempo em minutos que demorou a deslocação.
        """
        return distancia * 60 / (self.velocidade - peso * self.decrescimo)

    def calculaEmissaoCO2(self, distancia):
        """
        Calcula o total de emissões de CO2 emitidas com base na distância percorrida.

        Args:
            distancia (float): A distância percorrida.

        Returns:
            float: O total de emissões de CO2 emitidas.
        """
        return distancia * self.emissaoCO2

    def __str__(self):
        """
        Devolve uma string representativa da informação do meio de transporte.

        Returns:
            str: Uma string representativa da informação do meio de transporte.
        """
        return f"Meio de Transporte ({self.nome}) - Peso Máximo = {self.pesoMax}kg e Velocidade Média = {self.velocidade}km/h, sendo que há um descréscimo de {self.decrescimo}km/h por cada kg de carga."
    
    def __eq__(self, other):
            """
            Verifica se dois objetos MeioTransporte são iguais.

            Args:
                other (MeioTransporte): O outro objeto a ser comparado.

            Returns:
                bool: True se os objetos forem iguais, False caso contrário.
            """
            return self.nome == other.nome

    def __hash__(self):
        """
        Retorna o valor hash do objeto com base no nome.

        :return: O valor hash do objeto.
        """
        return hash(self.nome)
