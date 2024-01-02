import math
from queue import Queue

import networkx as nx
import matplotlib.pyplot as plt

class Node():
    def __init__(self, name, coordenadas, id=-1):
        self.m_id = id
        self.m_name = str(name)
        self.coordenadas = coordenadas

    def __str__(self):
        return "node " + self.m_name

    def setId(self, id):
        self.m_id = id

    def getId(self):
        return self.m_id

    def getName(self):
        return self.m_name

    def __eq__(self, other):
        return self.m_name == other.m_name

    def __hash__(self):
        return hash(self.m_name)

class Grafo():

    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}

    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
            return out
        
    def get_node_by_name(self, name):
        for node in self.m_nodes:
            if node.m_name == name:
                return node
            else:
                return None

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    def desenha(self):
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

    def getNodes(self):
        return self.m_nodes

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

    def calcula_custo(self, caminho):
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return round(custo,2)

    def procura_DFS(self, start, end, path = [], visited = set()):
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

    def procura_DFS_iterativo(self, start, end):
        visited = set()
        parents = {}

        def dfs_recursive(node):
            nonlocal visited, parents

            if node == end:
                return True

            visited.add(node)

            for neighbor, _ in self.getNeighbours(node):
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

            for neighbor, _ in self.getNeighbours(current_node):
                if neighbor not in visited:
                    stack.append(neighbor)
                    parents[neighbor] = current_node

        print('Path does not exist!')
        return None

    def procura_BFS(self, start, end):
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

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista
    
    def calcHeuristica(self, start, end):
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

    def procura_aStar(self, start, end):
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
                    calc_heurist[v] = g[v] + self.calcHeuristica(v, end)
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

            for (m, weight) in self.getNeighbours(n):
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
        open_list = set([start])
        closed_list = set([])
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or self.calcHeuristica(v, end) < self.calcHeuristica(n, end):
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

            for (m, weight) in self.getNeighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    def procura_UCS(self, start, end):
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

            for neighbor, weight in self.getNeighbours(current_node):
                new_cost = g[current_node] + weight

                if neighbor not in closed_list and (neighbor not in g or new_cost < g[neighbor]):
                    g[neighbor] = new_cost
                    open_list.append((new_cost, neighbor))
                    parents[neighbor] = current_node

        print('Path does not exist!')
        return None