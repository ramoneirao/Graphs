from grafo import Grafo

# Criando grafo
grafo = Grafo()

# Add vertices
grafo.novo_Vertice('A')
grafo.novo_Vertice('B')
grafo.novo_Vertice('C')
grafo.novo_Vertice('D')
grafo.novo_Vertice('E')

# Adicionando arestas
grafo.nova_Aresta("A", "B", 1)
grafo.nova_Aresta("A", "C", 2)
grafo.nova_Aresta("B", "D", 3)
grafo.nova_Aresta("C", "D", 4)
grafo.nova_Aresta("D", "E", 5)

# Realizando a busca em profundidade
grafo.Depth_first_search()