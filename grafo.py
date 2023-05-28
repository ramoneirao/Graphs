class Grafo:
    def __init__(self, direcionado=True):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado
        self.tempo = 0

    def novo_Vertice(self, identificador):
        # 
        self.lista_Vertices.append(Vertice(identificador))
        
    def busca_Aresta(self, u, v):
        for w in self.lista_Arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w
            
    def busca_Vertice(self, identificador):
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i 
        else:
            return None
        
    def nova_Aresta(self, origem, destino, peso):
        origem_aux = self.busca_Aresta(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Aresta.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um dos vertices ou ambos são inválidos.")
        if self.direcionado == False:
            self.lista_Aresta.append(Aresta(destino_aux, origem_aux, peso))


    def esta_Vazio(self):
        if len(self.lista_Vertices) == 0:
            return True
        else:
            return False