import math
from queue import Queue
from Node import Node

import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random

"""
Classe que representa o mapa da localidade, através de um grafo.
"""
class Grafo():

    def __init__(self, directed=False):
        self.m_nodes = []                   # Nodos
        self.m_directed = directed          # Indica se o grafo é direcionado ou não
        self.m_graph = {}                   # Estrutura do grafo

    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out
        
    def get_node_by_name(self, name):
        for node in self.m_nodes:
            if node.m_name == name:
                return node
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
        return custo
    
    def get_neighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista

    """
    Função que calcula a heurística para um dado node dado um destino. Esta representa a distância entre os dois nodes (ruas),
    dado que nós guardamos as coordenadas geográficas de cada rua.
    """
    def calcula_heuristica(self, start, end):
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

    def procura_DFS(self, start, end, path=None, visited=None):
        """
        Algoritmo de Pesquisa em Profundidade (DFS) para encontrar um caminho de start a end num grafo.

        O DFS explora o grafo, percorrendo o máximo possível ao longo de cada ramo antes de retroceder.
        Começa no nó 'start' fornecido e explora os seus vizinhos recursivamente até atingir o nó 'end' ou
        não haver mais vizinhos não visitados. Se o nó 'end' for encontrado, retorna o caminho de 'start' a 'end', e o custo total.
        Caso contrário, retorna None.

        Args:
            start: O nó de partida.
            end: O nó de destino.
            path: O caminho atual em exploração (padrão = None).
            visited: Um conjunto de nós visitados para evitar ciclos (padrão = None).

        Returns:
            Um tuplo contendo o caminho e o custo total se um caminho for encontrado, caso contrário, retorna None.
    """
        if path is None:
            path = []
        if visited is None:
            visited = set()

        path.append(start)
        visited.add(start)

        if start == end:
            custoT = self.calcula_custo(path)
            if print_visited:
                print("Nodos Visitados: " + str(visited))
            return (path, custoT)

        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:  
                    return resultado

        path.pop()
        return None

    def procura_IDDFS(self, start, end, max_depth):
        """
        Algoritmo de Pesquisa em Profundidade Iterativa com Limite (IDDFS) para encontrar um caminho de start a end num grafo.

        O IDDFS realiza repetidas pesquisas em profundidade com limites de profundidade crescentes até encontrar o objetivo.

        Args:
            start: O nó de partida.
            end: O nó de destino.
            max_depth: A profundidade máxima a explorar.

        Returns:
            Um tuplo contendo o caminho e o custo total se um caminho for encontrado, caso contrário, retorna None. 
        """
        def depth_limited_DFS(start, end, depth_limit, path=None, visited=None):
            if path is None:
                path = [start]
            if visited is None:
                visited = set([start])

            if start == end:
                custoT = self.calcula_custo(path)
                return ((path, custoT),visited)

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
            func_return = depth_limited_DFS(start, end, depth_limit)
            if func_return is not None:
                (result, visited) = func_return
                if print_visited:
                    print("Nodos Visitados: " + str(visited))
                return result
        return None

    def procura_BFS(self, start, end):
        """
        Realiza uma pesquisa em largura para encontrar um caminho entre dois nós.

        A pesquisa em largura (BFS) é um algoritmo para percorrer ou pesquisar estruturas de dados de árvores ou grafos que 
        começa no nó raiz e explora todos os nós vizinhos na profundidade atual antes de passar para os nós no próximo nível de profundidade.

        Args:
            start (str): Nome do nó de partida.
            end (str): Nome do nó de destino.

        Returns:
            tuple: Tuplo contendo o caminho e o seu custo, ou None se nenhum caminho for encontrado.
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
        
        if print_visited:
            print("Nodos Visitados: " + str(visited))
        return (path, custo)
    
    def procura_UCS(self, start, end):
        """
        Executa o algoritmo de Busca de Custo Uniforme (UCS) para encontrar o caminho mais curto de start a end num grafo.

        O UCS funciona explorando o grafo de maneira em largura, considerando o menor custo de cada caminho.
        Mantém uma lista aberta de nós a serem explorados, ordenados pelo custo cumulativo.
        O algoritmo continua até que a lista aberta esteja vazia ou o nó alvo seja alcançado.
        Durante a exploração, mantém estado dos pais de cada nó para reconstruir o caminho posteriormente.

        Parâmetros:
        - start: O nó de partida.
        - end: O nó de destino.

        Retorna:
        - Um tuplo contendo o caminho mais curto de start a end e o seu custo.
        Se nenhum caminho existir, retorna None.
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

                if print_visited:
                    print("Nodos Visitados: " + str(closed_list))
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
        Encontra o caminho mais curto usando o algoritmo de Dijkstra.
        Ele usa uma fila de prioridade para explorar os nós de forma ordenada, mantendo um registro dos 
        custos acumulados e dos pais de cada nó no caminho mais curto. O processo continua até que o nó 
        de destino seja alcançado ou todos os nós sejam explorados. O caminho mais curto é então reconstruído
        a partir dos pais registrados.

        Parâmetros:
        - start (str): Nome do nó de partida.
        - end (str): Nome do nó de destino.

        Retorna:
        - tuple: Um tuplo contendo o caminho mais curto e seu custo.
        """
        priority_queue = [(0, start)]
        # Dicionario que guarda o custo para chegar a cada node
        cost_to_reach = {start: 0}
        # Dictionário para guardar o pai de cada node no caminho mais curto
        parents = {start: None}
        visited = set()
        
        while priority_queue:
        # Obtém o nó com menor custo da fila de prioridade
            current_cost, current_node = heapq.heappop(priority_queue)

            # Verifica se alcançamos o nó de destino
            if current_node == end:
                # Reconstrói o caminho
                reconst_path = []
                while current_node is not None:
                    reconst_path.append(current_node)
                    current_node = parents[current_node]
                reconst_path.reverse()

                if print_visited:
                    print("Nodos Visitados: " + str(visited))
                return reconst_path, round(cost_to_reach[end],2)

            # Explora os vizinhos
            for neighbor, weight in self.get_neighbours(current_node):
                new_cost = cost_to_reach[current_node] + weight

                # Se o novo custo for menor que o custo registrado, atualiza-o
                if neighbor not in cost_to_reach or new_cost < cost_to_reach[neighbor]:
                    cost_to_reach[neighbor] = new_cost
                    parents[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        print('Path does not exist!')
        return None
    
    """
    Encontra o caminho mais curto entre dois nós usando o algoritmo de Floyd-Warshall.
    Calcula o caminho mais curto entre todos os pares de nós no grafo.

    Este algoritmo utiliza uma abordagem dinâmica para encontrar o caminho mais curto entre todos os pares de nós.
    Inicializa uma matriz de distâncias com os pesos das arestas existentes e as atualiza iterativamente para considerar
    caminhos intermediários. O caminho e o custo total entre os nós de partida e destino são recuperados a partir das
    matrizes geradas durante o processo.

    Parâmetros:
        start (str): Nome do nó de partida.
        end (str): Nome do nó de destino.
        print_visited (bool, opcional): Indica se deve imprimir os nós visitados durante a execução (padrão = False).

    Retorna:
        tuple ou None: Tuplo contendo o caminho e o custo total se uma solução for encontrada, None caso contrário.
    """
    def procura_floyd_warshall(self, start, end, print_visited=False):
        num_nodes = len(self.m_nodes)
        dist_matrix = [[math.inf] * num_nodes for _ in range(num_nodes)]
        next_node_matrix = [[None] * num_nodes for _ in range(num_nodes)]

        for i in range(num_nodes):
            dist_matrix[i][i] = 0
            node_name = self.m_nodes[i].getName()
            for (neighbor, weight) in self.m_graph[node_name]:
                neighbor_index = self.m_nodes.index(self.get_node_by_name(neighbor))
                dist_matrix[i][neighbor_index] = weight
                next_node_matrix[i][neighbor_index] = neighbor_index

        for k in range(num_nodes):
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if dist_matrix[i][k] != math.inf and dist_matrix[k][j] != math.inf:
                        if dist_matrix[i][k] + dist_matrix[k][j] < dist_matrix[i][j]:
                            dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                            next_node_matrix[i][j] = next_node_matrix[i][k]

        start_index = self.m_nodes.index(self.get_node_by_name(start))
        end_index = self.m_nodes.index(self.get_node_by_name(end))

        if next_node_matrix[start_index][end_index] is None:
            return None, math.inf

        path = [start_index]
        while path[-1] != end_index:
            path.append(next_node_matrix[path[-1]][end_index])

        path_nodes = [self.m_nodes[i].getName() for i in path]

        distance = dist_matrix[start_index][end_index]

        if print_visited:
            print("Nós Visitados: " + str(set(node_name for path_node in path_nodes for node_name in path_node)))
        return path_nodes, round(distance, 2)

    
    def procura_bellman_ford(self, start, end):
        """
        Encontra o caminho mais curto usando o algoritmo de Bellman-Ford.

        O algoritmo de Bellman-Ford encontra o caminho mais curto entre dois nós em um grafo, mesmo quando há arestas com pesos negativos.
        Ele utiliza a técnica de relaxamento, iterativamente, sobre todas as arestas do grafo para encontrar as distâncias mais curtas.

        Parâmetros:
        - start (str): Nome do nó de partida.
        - end (str): Nome do nó de destino.

        Retorna:
        - tuple: Um tuplo contendo o caminho mais curto e seu custo.
        """
            # Dicionário para armazenar o custo para alcançar cada nó
        custo_para_alcancar = {node.getName(): math.inf for node in self.m_nodes}
        custo_para_alcancar[start] = 0
            # Dicionário para armazenar o pai de cada nó no caminho mais curto
        pais = {node.getName(): None for node in self.m_nodes}

        # Relaxa as arestas repetidamente
        for _ in range(len(self.m_nodes) - 1):
            for node in self.m_nodes:
                for vizinho, peso in self.get_neighbours(node.getName()):
                    novo_custo = custo_para_alcancar[node.getName()] + peso
                    if novo_custo < custo_para_alcancar[vizinho]:
                        custo_para_alcancar[vizinho] = novo_custo
                        pais[vizinho] = node.getName()

        # Verifica ciclos negativos
        for node in self.m_nodes:
            for vizinho, peso in self.get_neighbours(node.getName()):
                if custo_para_alcancar[node.getName()] + peso < custo_para_alcancar[vizinho]:
                    print('Ciclo negativo detetado!')
                    return None

        # Reconstrói o caminho
        caminho_reconstruido = []
        no_atual = end
        while no_atual is not None:
            caminho_reconstruido.append(no_atual)
            no_atual = pais[no_atual]
        caminho_reconstruido.reverse()

        return caminho_reconstruido, custo_para_alcancar[end]


# PROCURAS INFORMADAS

    def procura_aStar(self, start, end):
        """
        O algoritmo A* efetivamente utiliza listas abertas e fechadas para otimizar a busca. A lista aberta armazena nós
        que ainda precisam ser explorados, priorizando aqueles com menores custos estimados. A lista fechada, por sua vez,
        registra os nós já explorados, evitando revisões desnecessárias. Isso melhora significativamente a eficiência do
        algoritmo, garantindo que a busca se concentre em áreas mais promissoras do grafo, economizando recursos computacionais.
        Ao iterativamente selecionar e expandir nós, o A* equilibra a busca entre a exploração de novas possibilidades e a
        reutilização de informações previamente analisadas, resultando em um método eficaz para encontrar o caminho mais curto.
        Parâmetros: start (Node) - nó de partida, end (Node) - nó de destino.
        Retorna: tuplo com caminho (lista de nós) e custo.
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

                if print_visited:
                    print("Nodos Visitados: " + str(closed_list))
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
        Realiza um algoritmo de pesquisa IDA* para encontrar o caminho ótimo do nó de partida ao nó de destino num grafo.

        O algoritmo IDA* é uma variante do algoritmo de pesquisa A* que utiliza aprofundamento iterativo para encontrar o caminho ótimo.
        Ele realiza uma pesquisa com limite de profundidade, aumentando gradualmente o limite de profundidade até encontrar um caminho ou até que o espaço de pesquisa seja esgotado.
        Em cada limite de profundidade, o algoritmo expande os nós no grafo, considerando o custo do caminho desde o nó de partida e o custo estimado até o nó de destino.
        Se o custo estimado exceder o limite de profundidade atual, a pesquisa é interrompida para esse nó.
        O algoritmo continua até encontrar um caminho ou determinar que nenhum caminho existe.
        
        Parâmetros:
            start: O nó de partida.
            end: O nó de destino.

        Retorna:
            Se encontrar um caminho, retorna um tuplo com o caminho e seu custo.
            Se não encontrar um caminho, retorna None.

        """

        def depth_limited_search(current_node, end, bound, path, g, visited):
            f = g[current_node] + self.calcula_heuristica(current_node, end)

            if f > bound:
                return f, f

            if current_node == end:
                return "found", f

            min_cost = math.inf
            for neighbor, weight in self.get_neighbours(current_node):
                if neighbor not in path:
                    path.append(neighbor)
                    visited.add(neighbor)
                    g[neighbor] = g[current_node] + weight
                    result, new_bound = depth_limited_search(neighbor, end, bound, path, g, visited)

                    if result == "found":
                        return result, new_bound

                    min_cost = min(min_cost, result)
                    path.pop()

            return min_cost, min_cost

        bound = self.calcula_heuristica(start, end)
        path = [start]
        g = {start: 0}
        visited = set([start])

        while True:
            result, new_bound = depth_limited_search(start, end, bound, path, g, visited)

            if result == "found":
                if print_visited:
                    print("Nodos Visitados: " + str(visited))
                return path, self.calcula_custo(path)

            if result == math.inf:
                print('Path does not exist!')
                return None

            bound = new_bound

    def procuraGreedy(self, start, end):
        """
        Realiza um algoritmo de pesquisa gulosa para encontrar o caminho mais curto do nó de partida ao nó de destino.

        A pesquisa gulosa funciona escolhendo sempre o nó que parece estar mais próximo do destino com base numa função heurística.
        Expande a pesquisa considerando os vizinhos do nó atual e selecionando aquele com o valor heurístico mais baixo.
        Este processo continua até atingir o nó de destino ou não houver mais nós para explorar.

        Parâmetros:
        - start: O nó de partida da pesquisa.
        - end: O nó de destino a alcançar.

        Retorna:
        - Se encontrar um caminho, retorna um tuplo com o caminho como uma lista de nós e o custo total do caminho.
        - Se não encontrar um caminho, retorna None.
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

                if print_visited:
                    print("Nodos Visitados: " + str(closed_list))
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
        Algoritmo de passeio aleatório que tenta encontrar uma solução entre os nós de início e fim.

        Parâmetros:
            start_node (str): Nome do nó de partida.
            end_node (str): Nome do nó de destino.

        Retorna:
            tuple ou None: Tuplo contendo o caminho e o custo total se uma solução for encontrada, None caso contrário.
        """
        current_node = start_node
        path = [current_node]
        total_cost = 0

        while current_node != end_node:
            neighbors = self.m_graph.get(current_node, [])
            unvisited_neighbors = [(neighbor, cost) for neighbor, cost in neighbors if neighbor not in path]

            if not unvisited_neighbors:
                # Se não houver mais vizinhos por visitar, backtrack
                path.pop()
                if not path:
                    # If the path is empty, no solution is found
                    return None
                current_node = path[-1]
            else:
                # Move para um vizinho ainda não visitado aleatorio 
                next_node, cost = random.choice(unvisited_neighbors)
                path.append(next_node)
                total_cost += cost
                current_node = next_node

        return path, round(total_cost, 2)