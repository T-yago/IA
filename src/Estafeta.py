class Estafeta():
    """
    Represents a delivery person.

    Attributes:
        id (int): The ID of the estafeta.
        nome (str): The name of the estafeta.
        idsEntregas (list): The list of IDs of the deliveries that are yet to be completed.
        ranking (int): The ranking of the estafeta.
        nrEntregasConcluidas (int): The number of completed deliveries.
        entregasInconcluidas (list): The list of IDs of the deliveries that are yet to be completed.
        entregasConcluidas (list): The list of IDs of the completed deliveries.
    """

    def __init__(self, id, nome, idsEntregas=[], ranking=5):
        """
        Initializes a new instance of the Estafeta class.

        Args:
            id (int): The ID of the estafeta.
            nome (str): The name of the estafeta.
            idsEntregas (list, optional): The list of IDs of the deliveries that are yet to be completed. Defaults to an empty list.
            ranking (int, optional): The ranking of the estafeta. Defaults to 5.
        """
        self.id = id
        self.nome = nome
        self.nrEntregasConcluidas = 0
        self.entregasInconcluidas = idsEntregas
        self.entregasConcluidas = []
        self.ranking = ranking

    def getID(self):
        """
        Gets the ID of the estafeta.

        Returns:
            int: The ID of the estafeta.
        """
        return self.id
    
    def getNome(self):
        """
        Gets the name of the estafeta.

        Returns:
            str: The name of the estafeta.
        """
        return self.nome
    
    def getNrEntregasConcluidas(self):
        """
        Gets the number of completed deliveries.

        Returns:
            int: The number of completed deliveries.
        """
        return self.nrEntregasConcluidas
    
    def getEntregasConcluidas(self):
        """
        Gets the list of IDs of the completed deliveries.

        Returns:
            list: The list of IDs of the completed deliveries.
        """
        return self.entregasConcluidas
    
    def getEntregasInconcluidas(self):
        """
        Gets the list of IDs of the deliveries that are yet to be completed.

        Returns:
            list: The list of IDs of the deliveries that are yet to be completed.
        """
        return self.entregasInconcluidas

    def getEntregas(self):
        """
        Gets the list of all deliveries (completed and yet to be completed).

        Returns:
            list: The list of all deliveries.
        """
        return self.entregasInconcluidas + self.entregasConcluidas
    
    def getRanking(self):
        """
        Gets the ranking of the estafeta.

        Returns:
            int: The ranking of the estafeta.
        """
        return self.ranking
    
    def setID(self, id):
        """
        Sets the ID of the estafeta.

        Args:
            id (int): The ID of the estafeta.
        """
        self.id = id

    def setNome(self, nome):
        """
        Sets the name of the estafeta.

        Args:
            nome (str): The name of the estafeta.
        """
        self.nome = nome

    def setNrEntregasConcluidas(self, nrEntregasConcluidas):
        """
        Sets the number of completed deliveries.

        Args:
            nrEntregasConcluidas (int): The number of completed deliveries.
        """
        self.nrEntregasConcluidas = nrEntregasConcluidas
    
    def setEntregasConcluidas(self, entregasConcluidas):
        """
        Sets the list of IDs of the completed deliveries.

        Args:
            entregasConcluidas (list): The list of IDs of the completed deliveries.
        """
        self.entregasConcluidas = entregasConcluidas

    def setEntregasInconcluidas(self, entregasInconcluidas):
        """
        Sets the list of IDs of the deliveries that are yet to be completed.

        Args:
            entregasInconcluidas (list): The list of IDs of the deliveries that are yet to be completed.
        """
        self.entregasInconcluidas = entregasInconcluidas

    def setRanking(self, ranking):
        """
        Sets the ranking of the estafeta.

        Args:
            ranking (int): The ranking of the estafeta.
        """
        self.ranking = ranking

    def completeEntregas(self, entregas):
        """
        Completes the deliveries and updates the ranking of the estafeta.

        Args:
            entregas (list): The list of deliveries to be completed, each represented as a tuple of (id, ranking).
        """
        self.ranking = self.ranking * self.nrEntregasConcluidas
        for id, ranking in entregas:
            if (id in self.entregasInconcluidas):
                self.entregasInconcluidas.remove(id)
                self.entregasConcluidas.append(id)
                self.nrEntregasConcluidas += 1
                self.ranking += ranking
        
        self.ranking = round(self.ranking / self.nrEntregasConcluidas, 2)
    
    def addEntrega(self, idEntrega):
        """
        Adds a delivery to the list of deliveries that are yet to be completed.

        Args:
            idEntrega (int): The ID of the delivery to be added.
        """
        self.entregasInconcluidas.append(idEntrega)

    def __str__(self):
        """
        Returns a string representation of the estafeta.

        Returns:
            str: A string representation of the estafeta.
        """
        res = f"Estafeta nº{self.id}: {self.nome}\n"

        res += "Ids das entregas a realizar: "
        res += ', '.join(str(element) for element in self.entregasInconcluidas)
        
        res += "\nIds das entregas realizadas: "
        res += ', '.join(str(element) for element in self.entregasConcluidas)
        
        res += f"\nO estafeta realizou um total de {self.nrEntregasConcluidas} entregas obtendo um ranking total de {self.ranking}."

        return res
    
    def __eq__(self, other):
        """
        Checks if two estafetas are equal based on their IDs.

        Args:
            other (Estafeta): The other estafeta to compare.

        Returns:
            bool: True if the estafetas are equal, False otherwise.
        """
        return self.id == other.id

    def __hash__(self):
        """
        Returns the hash value of the estafeta based on its ID.

        Returns:
            int: The hash value of the estafeta.
        """
        return hash(self.id)