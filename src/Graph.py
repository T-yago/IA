import math
from queue import Queue
from Node import Node

import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random


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

    def procura_IDDFS(self, start, end, max_depth):
        """
        Iterative Deepening Depth-First Search (IDDFS) algorithm to find a path from start to end in a graph.

        IDDFS repeatedly performs a depth-first search with increasing depth limits until the goal is found.

        Args:
            start: The starting node.
            end: The target node.
            max_depth: The maximum depth to explore.

        Returns:
            A tuple containing the path and the total cost if a path is found, None otherwise.
        """
        def depth_limited_DFS(start, end, depth_limit, path=None, visited=None):
            """
            Depth-Limited DFS with a specified depth limit.

            Args:
                start: The starting node.
                end: The target node.
                depth_limit: The maximum depth to explore.
                path: The current path being explored (default is None).
                visited: A set of visited nodes to avoid cycles (default is None).

            Returns:
                A tuple containing the path and the total cost if a path is found, None otherwise.
            """
            if path is None:
                path = [start]
            if visited is None:
                visited = set([start])

            if start == end:
                custoT = self.calcula_custo(path)
                return (path, custoT)

            if depth_limit == 0:
                return None

            for (adjacente, peso) in self.m_graph[start]:
                if adjacente not in visited:
                    path.append(adjacente)
                    visited.add(adjacente)
                    result = depth_limited_DFS(adjacente, end, depth_limit - 1, path, visited)
                    if result is not None:
                        return result
                    path.pop()
                    visited.remove(adjacente)

            return None
        
        for depth_limit in range(1, max_depth + 1):
            result = depth_limited_DFS(start, end, depth_limit)
            if result is not None:
                return result
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

                return (reconst_path, round(g[end], 2))

            for neighbor, weight in self.get_neighbours(current_node):
                new_cost = g[current_node] + weight

                if neighbor not in closed_list and (neighbor not in g or new_cost < g[neighbor]):
                    g[neighbor] = new_cost
                    open_list.append((new_cost, neighbor))
                    parents[neighbor] = current_node

        print('Path does not exist!')
        return None



    def procura_dijkstra(self, start, end):
        """
        Finds the shortest path using Dijkstra's algorithm.

        Args:
            start (str): Name of the starting node.
            end (str): Name of the ending node.

        Returns:
            tuple: A tuple containing the shortest path and its cost.
        """
        # Priority queue for Dijkstra's algorithm
        priority_queue = [(0, start)]
        # Dictionary to store the cost to reach each node
        cost_to_reach = {start: 0}
        # Dictionary to store the parent of each node in the shortest path
        parents = {start: None}

        while priority_queue:
            # Get the node with the lowest cost from the priority queue
            current_cost, current_node = heapq.heappop(priority_queue)

            # Check if we reached the end node
            if current_node == end:
                # Reconstruct the path
                reconst_path = []
                while current_node is not None:
                    reconst_path.append(current_node)
                    current_node = parents[current_node]
                reconst_path.reverse()

                return reconst_path, cost_to_reach[end]

            # Explore neighbors
            for neighbor, weight in self.get_neighbours(current_node):
                new_cost = cost_to_reach[current_node] + weight

                # If the new cost is smaller than the recorded cost, update it
                if neighbor not in cost_to_reach or new_cost < cost_to_reach[neighbor]:
                    cost_to_reach[neighbor] = new_cost
                    parents[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        print('Path does not exist!')
        return None
    
    def procura_bellman_ford(self, start, end):
        """
        Finds the shortest path using the Bellman-Ford algorithm.

        Args:
            start (str): Name of the starting node.
            end (str): Name of the ending node.

        Returns:
            tuple: A tuple containing the shortest path and its cost.
        """
        # Dictionary to store the cost to reach each node
        cost_to_reach = {node.getName(): math.inf for node in self.m_nodes}
        cost_to_reach[start] = 0
        # Dictionary to store the parent of each node in the shortest path
        parents = {node.getName(): None for node in self.m_nodes}

        # Relax edges repeatedly
        for _ in range(len(self.m_nodes) - 1):
            for node in self.m_nodes:
                for neighbor, weight in self.get_neighbours(node.getName()):
                    new_cost = cost_to_reach[node.getName()] + weight
                    if new_cost < cost_to_reach[neighbor]:
                        cost_to_reach[neighbor] = new_cost
                        parents[neighbor] = node.getName()

        # Check for negative cycles
        for node in self.m_nodes:
            for neighbor, weight in self.get_neighbours(node.getName()):
                if cost_to_reach[node.getName()] + weight < cost_to_reach[neighbor]:
                    print('Negative cycle detected!')
                    return None

        # Reconstruct the path
        reconst_path = []
        current_node = end
        while current_node is not None:
            reconst_path.append(current_node)
            current_node = parents[current_node]
        reconst_path.reverse()

        return reconst_path, cost_to_reach[end]
    
    def procura_floyd_warshall(self, start, end):
        num_nodes = len(self.m_nodes)
        dist_matrix = [[math.inf] * num_nodes for _ in range(num_nodes)]
        next_node_matrix = [[None] * num_nodes for _ in range(num_nodes)]

        # Initialize distance matrix with edge weights
        for i in range(num_nodes):
            dist_matrix[i][i] = 0
            node_name = self.m_nodes[i].getName()
            for (neighbor, weight) in self.m_graph[node_name]:
                neighbor_index = self.m_nodes.index(self.get_node_by_name(neighbor))
                dist_matrix[i][neighbor_index] = weight
                next_node_matrix[i][neighbor_index] = neighbor_index

        # Floyd-Warshall algorithm
        for k in range(num_nodes):
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if dist_matrix[i][k] != math.inf and dist_matrix[k][j] != math.inf:
                        if dist_matrix[i][k] + dist_matrix[k][j] < dist_matrix[i][j]:
                            dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                            next_node_matrix[i][j] = next_node_matrix[i][k]

        # Reconstruct the path
        start_index = self.m_nodes.index(self.get_node_by_name(start))
        end_index = self.m_nodes.index(self.get_node_by_name(end))

        if next_node_matrix[start_index][end_index] is None:
            # No path exists between start and end
            return None, math.inf

        path = [start_index]
        while path[-1] != end_index:
            path.append(next_node_matrix[path[-1]][end_index])

        # Convert node indices to node names
        path_nodes = [self.m_nodes[i].getName() for i in path]

        # Return the path and distance
        distance = dist_matrix[start_index][end_index]
        return path_nodes, distance

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

        However, if the selected node is not the goal node, the algorithm dynamically expands the chosen 
        node's neighborhood, generating adjacent nodes that are directly accessible from the current position. 
        It then calculates or updates various values for each neighboring node, including the actual cost from 
        the start node to the neighbor, the heuristic estimate from that node to the goal, and the sum of these 
        two values (the f-cost).

        Subsequently, the algorithm checks whether each neighboring node is already part of the open list or the 
        closed list. Nodes that are absent from the open list or have a lower f-cost compared to their previous 
        state are considered for inclusion or update. This iterative process ensures that the algorithm continues 
        to prioritize nodes with lower estimated costs, creating an efficient search strategy.

        The A* algorithm repeats the selection step, choosing the next node with the lowest estimated cost from the 
        updated open list. This cycle continues until the goal node is eventually reached or until the open list is 
        empty, signifying that no viable path to the goal exists.

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

    def procura_IDAstar(self, start, end):
        """
        Performs an IDA* search algorithm to find the optimal path from the start node to the end node in a graph.

        The IDA* algorithm is a variant of the A* search algorithm that uses iterative deepening to find the optimal path.
        It performs a depth-limited search, gradually increasing the depth limit until a path is found or the search space is exhausted.
        At each depth limit, the algorithm expands the nodes in the graph, considering the cost of the path from the start node and the estimated cost to the target node.
        If the estimated cost exceeds the current depth limit, the search is pruned for that node.
        The algorithm continues until a path is found or it is determined that no path exists.
        
        Args:
            start: The starting node.
            end: The target node.

        Returns:
            If a path is found, returns a tuple containing the path and its cost.
            If no path is found, returns None.

        """

        def depth_limited_search(current_node, end, bound, path, g):
            f = g[current_node] + self.calcula_heuristica(current_node, end)

            if f > bound:
                return f, f

            if current_node == end:
                return "found", f

            min_cost = math.inf
            for neighbor, weight in self.get_neighbours(current_node):
                if neighbor not in path:
                    path.append(neighbor)
                    g[neighbor] = g[current_node] + weight
                    result, new_bound = depth_limited_search(neighbor, end, bound, path, g)

                    if result == "found":
                        return result, new_bound

                    min_cost = min(min_cost, result)
                    path.pop()

            return min_cost, min_cost

        bound = self.calcula_heuristica(start, end)
        path = [start]
        g = {start: 0}

        while True:
            result, new_bound = depth_limited_search(start, end, bound, path, g)

            if result == "found":
                return path, self.calcula_custo(path)

            if result == math.inf:
                print('Path does not exist!')
                return None

            bound = new_bound

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
    
    def random_walk(self, start_node, end_node):
        """
        Random walk algorithm that attempts to find a solution between start and end nodes.

        Args:
            start_node (str): Name of the starting node.
            end_node (str): Name of the ending node.

        Returns:
            tuple or None: Tuple containing the path and total cost if a solution is found, None otherwise.
        """
        current_node = start_node
        path = [current_node]
        total_cost = 0

        while current_node != end_node:
            neighbors = self.m_graph.get(current_node, [])
            unvisited_neighbors = [(neighbor, cost) for neighbor, cost in neighbors if neighbor not in path]

            if not unvisited_neighbors:
                # If there are no unvisited neighbors, backtrack
                path.pop()
                if not path:
                    # If the path is empty, no solution is found
                    return None
                current_node = path[-1]
            else:
                # Move to a random unvisited neighbor
                next_node, cost = random.choice(unvisited_neighbors)
                path.append(next_node)
                total_cost += cost
                current_node = next_node

        return path, round(total_cost, 2)