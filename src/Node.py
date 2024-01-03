
class Node():
    def __init__(self, name, coordenadas, id=-1):
        """
        Initializes a Node object.

        Parameters:
        - name (str): The name of the node.
        - coordenadas (tuple): The coordinates of the node.
        - id (int, optional): The ID of the node. Defaults to -1.
        """
        self.m_id = id
        self.m_name = str(name)
        self.coordenadas = coordenadas

    def __str__(self):
        """
        Returns a string representation of the Node object.

        Returns:
        - str: The string representation of the Node object.
        """
        return "node " + self.m_name

    def setId(self, id):
        """
        Sets the ID of the Node object.

        Parameters:
        - id (int): The ID to be set.
        """
        self.m_id = id

    def getId(self):
        """
        Returns the ID of the Node object.

        Returns:
        - int: The ID of the Node object.
        """
        return self.m_id

    def getName(self):
        """
        Returns the name of the Node object.

        Returns:
        - str: The name of the Node object.
        """
        return self.m_name

    def __eq__(self, other):
        """
        Checks if two Node objects are equal.

        Parameters:
        - other (Node): The other Node object to compare.

        Returns:
        - bool: True if the Node objects are equal, False otherwise.
        """
        return self.m_name == other.m_name

    def __hash__(self):
        """
        Returns the hash value of the Node object.

        Returns:
        - int: The hash value of the Node object.
        """
        return hash(self.m_name)