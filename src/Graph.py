import math
from queue import Queue
from Node import Node

import networkx as nx
import matplotlib.pyplot as plt

class Grafo():
    """
    This class represents a graph.

    Attributes:
        m_nodes (list): List of nodes in the graph.
        m_directed (bool): Flag indicating whether the graph is directed or not.
        m_graph (dict): Dictionary representing the graph structure.
    """

    def __init__(self, directed=False):
        """
        Initializes a new instance of the Grafo class.

        Args:
            directed (bool, optional): Flag indicating whether the graph is directed or not. Defaults to False.
        """
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}

    def __str__(self):
        """
        Returns a string representation of the graph.

        Returns:
            str: String representation of the graph.
        """
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
            return out
        
    def get_node_by_name(self, name):
        """
        Retrieves a node from the graph based on its name.

        Args:
            name (str): Name of the node to retrieve.

        Returns:
            Node: The node with the specified name, or None if not found.
        """
        for node in self.m_nodes:
            if node.m_name == name:
                return node
            else:
                return None

    def imprime_aresta(self):
        """
        Prints the edges of the graph.

        Returns:
            str: String representation of the graph's edges.
        """
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    def desenha(self):
        """
        Draws the graph using networkx and matplotlib.
        """
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    def add_edge(self, node1, coordenadas1, node2, coordenadas2, weight):
        """
        Adds an edge to the graph.

        Args:
            node1 (str): Name of the first node.
            coordenadas1 (tuple): Coordinates of the first node.
            node2 (str): Name of the second node.
            coordenadas2 (tuple): Coordinates of the second node.
            weight (float): Weight of the edge.
        """
        n1 = Node(node1, coordenadas1)
        n2 = Node(node2, coordenadas2)
        if (n1 not in self.m_nodes):
            self.m_nodes.append(n1)
            self.m_graph[node1] = list()
        else:
            n1 = self.get_node_by_name(node1)

        if (n2 not in self.m_nodes):
            self.m_nodes.append(n2)
            self.m_graph[node2] = list()
        else:
            n2 = self.get_node_by_name(node2)

        self.m_graph[node1].append((node2, weight))


        if not self.m_directed:
            self.m_graph[node2].append((node1, weight))

    def get_arc_cost(self, node1, node2):
        """
        Retrieves the cost of an arc between two nodes.

        Args:
            node1 (str): Name of the first node.
            node2 (str): Name of the second node.

        Returns:
            float: The cost of the arc between the two nodes.
        """
        custoT = math.inf
        a = self.m_graph[node1]
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo
        return custoT

    def calcula_custo(self, caminho):
        """
        Calculates the cost of a given path in the graph.

        Args:
            caminho (list): List of nodes representing the path.

        Returns:
            float: The cost of the path.
        """
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return round(custo,2)
    
    def get_neighbours(self, nodo):
        """
        Retrieves the neighbors of a given node.

        Args:
            nodo (str): Name of the node.

        Returns:
            list: List of tuples representing the neighbors and their weights.
        """
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista

    def calcula_heuristica(self, start, end):
        """
        Calculates the heuristic value between two nodes, using the Haversine formula.

        Args:
            start (str): Name of the starting node.
            end (str): Name of the ending node.

        Returns:
            float: The heuristic value between the two nodes.
        """
        (latA_deg, lonA_deg) = (0.0,0.0)
        (latB_deg,lonB_deg) = (0.0,0.0)

        for node in self.m_nodes:
            if node.m_name == start:
                (latA_deg,lonA_deg) = node.coordenadas
            if node.m_name == end:
                (latB_deg,lonB_deg) = node.coordenadas

        latA = math.radians(latA_deg)
        lonA = math.radians(lonA_deg)
        latB = math.radians(latB_deg)
        lonB = math.radians(lonB_deg)
        a = math.sin((latB - latA) / 2)**2 + math.cos(latA) * math.cos(latB) * math.sin((lonB - lonA) / 2)**2

        return 6371000 * 2 * math.asin(math.sqrt(a)) / 1000

# PROCURAS NÃO INFORMADAS

    def procura_DFS(self, start, end, path = [], visited = set()):
        """
        Depth-First Search (DFS) algorithm to find a path from start to end in a graph.

        DFS explores the graph by traversing as far as possible along each branch before backtracking.
        It starts at the given 'start' node and explores its neighbors recursively until it reaches the 'end' node or
        there are no more unvisited neighbors. If the 'end' node is found, it returns the path from 'start' to 'end'.
        Otherwise, it returns None.

        Args:
            start: The starting node.
            end: The target node.
            path: The current path being explored (default = []).
            visited: A set of visited nodes to avoid cycles (default = set()).

        Returns:
            A tuple containing the path and the total cost if a path is found, None otherwise.
        """
        path.append(start)
        visited.add(start)

        if start == end:
            custoT = self.calcula_custo(path)
            return (path, custoT)

        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:  
                    return resultado

        path.pop()
        return None
    
    def procura_IDDFS(self, start, end, max_depth):
        def DLS_Recursive(self, current_node, end, depth_limit, visited, path):
            if current_node == end:
                return "found"

            if depth_limit == 0:
                return "depth_limit_exceeded"

            for neighbor, _ in self.get_neighbours(current_node):
                if neighbor not in visited:
                    path.append(neighbor)
                    visited.add(neighbor)

                    result = self.DLS_Recursive(neighbor, end, depth_limit - 1, visited, path)

                    if result == "found" or result != "depth_limit_exceeded":
                        return result

                    path.pop()

            return "not_found"
        
        def procura_DLS(self, start, end, depth_limit):
            visited = set()
            path = [start]

            result = self.DLS_Recursive(start, end, depth_limit, visited, path)

            if result == "found":
                return path, self.calcula_custo(path)

            print('Path does not exist within depth limit!')
            return None
        

        for depth_limit in range(max_depth + 1):
            result = self.procura_DLS(start, end, depth_limit)

            if result is not None:
                return result

        print('Path does not exist within the specified depth limit!')
        return None

    def procura_DFS_iterativo(self, start, end):
        visited = set()
        parents = {}

        def dfs_recursive(node):
            nonlocal visited, parents

            if node == end:
                return True

            visited.add(node)

            for neighbor, _ in self.get_neighbours(node):
                if neighbor not in visited:
                    parents[neighbor] = node
                    if dfs_recursive(neighbor):
                        return True

            return False

        if dfs_recursive(start):
            reconst_path = []
            current_node = end
            while current_node != start:
                reconst_path.append(current_node)
                current_node = parents[current_node]
            reconst_path.append(start)
            reconst_path.reverse()

            return (reconst_path, self.calcula_custo(reconst_path))

        print('Path does not exist!')
        return None

    def procura_DFS_stack(self, start, end):
        stack = [start]
        visited = set()
        parents = {}

        while stack:
            current_node = stack.pop()

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == end:
                reconst_path = []
                while current_node != start:
                    reconst_path.append(current_node)
                    current_node = parents[current_node]
                reconst_path.append(start)
                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path))

            for neighbor, _ in self.get_neighbours(current_node):
                if neighbor not in visited:
                    stack.append(neighbor)
                    parents[neighbor] = current_node

        print('Path does not exist!')
        return None

    def procura_BFS(self, start, end):
        """
        Performs a breadth-first search to find a path between two nodes.

        Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. 
        It starts at the root node and explores all the neighbor nodes at the present depth before moving on to the nodes at the next depth level.

        Args:
            start (str): Name of the starting node.
            end (str): Name of the ending node.

        Returns:
            tuple: Tuple containing the path and its cost, or None if no path is found.
        """
        visited = set()
        fila = Queue()

        fila.put(start)
        visited.add(start)

        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            custo = self.calcula_custo(path)
        return (path, custo)
    
    def procura_UCS(self, start, end):
        """
        Performs Uniform Cost Search (UCS) algorithm to find the shortest path from start to end in a graph.

        UCS works by exploring the graph in a breadth-first manner, considering the lowest cost of each path.
        It maintains an open list of nodes to be explored, sorted by their cumulative cost.
        The algorithm continues until the open list is empty or the target node is reached.
        During the exploration, it keeps track of the parents of each node to reconstruct the path later.

        Parameters:
        - start: The starting node.
        - end: The target node.

        Returns:
        - A tuple containing the shortest path from start to end and its cost.
            If no path exists, returns None.
        """

        open_list = [(0, start)]
        closed_list = set()
        parents = {}
        g = {start: 0}

        while open_list:
            open_list.sort()
            cost, current_node = open_list.pop(0)

            if current_node in closed_list:
                continue

            closed_list.add(current_node)

            if current_node == end:
                reconst_path = []
                while current_node != start:
                    reconst_path.append(current_node)
                    current_node = parents[current_node]
                reconst_path.append(start)
                reconst_path.reverse()

                return (reconst_path, g[end])

            for neighbor, weight in self.get_neighbours(current_node):
                new_cost = g[current_node] + weight

                if neighbor not in closed_list and (neighbor not in g or new_cost < g[neighbor]):
                    g[neighbor] = new_cost
                    open_list.append((new_cost, neighbor))
                    parents[neighbor] = current_node

        print('Path does not exist!')
        return None

# PROCURAS INFORMADAS

    def procura_aStar(self, start, end):
        """
        Finds the shortest path from the start node to the end node using the A* algorithm.

        The A* algorithm is an informed search algorithm that uses heuristics to guide the search
        towards the goal node. It maintains two lists: an open list and a closed list. The open list
        contains the nodes that are yet to be explored, while the closed list contains the nodes that
        have already been explored.

        The algorithm starts by initializing the open list with the start node. It then iteratively
        selects the node with the lowest estimated cost (based on the sum of the actual cost from the
        start node and the heuristic estimate to the goal node) from the open list. If the selected node
        is the goal node, the algorithm reconstructs the path from the start node to the goal node and
        returns it along with the cost of the path.

        If the open list becomes empty before reaching the goal node, it means that there is no path
        from the start node to the goal node, and the algorithm returns None.

        The A* algorithm is commonly used in pathfinding problems, where finding the shortest path
        between two points in a graph is required.
        
        Parameters:
            start (Node): The starting node.
            end (Node): The target node.

        Returns:
            tuple: A tuple containing the shortest path as a list of nodes and the cost of the path.
        """
        open_list = {start}
        closed_list = set([])
        g = {}

        g[start] = 0

        parents = {}
        parents[start] = start
        n = None
        while len(open_list) > 0:
            calc_heurist = {}
            flag = 0
            for v in open_list:
                if n == None:
                    n = v
                else:
                    flag = 1
                    calc_heurist[v] = g[v] + self.calcula_heuristica(v, end)
            if flag == 1:
                min_estima = min(calc_heurist, key=calc_heurist.get)
                n = min_estima
            if n == None:
                print('Path does not exist!')
                return None

            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path))

            for (m, weight) in self.get_neighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    def procuraGreedy(self, start, end):
        """
        Performs a greedy search algorithm to find the shortest path from the start node to the end node.

        Greedy search works by always choosing the node that appears to be closest to the target based on a heuristic function.
        It expands the search by considering the neighbors of the current node and selecting the one with the lowest heuristic value.
        This process continues until the target node is reached or there are no more nodes to explore.

        Parameters:
        - start: The starting node of the search.
        - end: The target node to reach.

        Returns:
        - If a path is found, returns a tuple containing the path as a list of nodes and the total cost of the path.
        - If no path is found, returns None.
        """

        open_list = set([start])
        closed_list = set([])
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or self.calcula_heuristica(v, end) < self.calcula_heuristica(n, end):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path))

            for (m, weight) in self.get_neighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    def procura_IDAstar(self, start, end):
        
        def depth_limited_search(self, current_node, end, bound, path):
            f = self.calcula_custo(path) + self.getH(current_node)

            if f > bound:
                return f, f

            if current_node == end:
                return "found", f

            min_cost = math.inf
            for neighbor, weight in self.get_neighbours(current_node):
                if neighbor not in path:
                    path.append(neighbor)
                    result, new_bound = self.depth_limited_search(neighbor, end, bound, path)
                    
                    if result == "found":
                        return result, new_bound

                    min_cost = min(min_cost, result)
                    path.pop()

            return min_cost, min_cost
        
        bound = self.getH(start)
        path = [start]
        
        while True:
            result, new_bound = self.depth_limited_search(start, end, bound, [])
            
            if result == "found":
                return path, self.calcula_custo(path)
            
            if result == math.inf:
                print('Path does not exist!')
                return None

            bound = new_bound