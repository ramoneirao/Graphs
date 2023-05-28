class Vertice():
    def __init__(self, id):
        self.id = id
        self.input = 0
        self.output = 0 
        self.visitado = False 
        self.predecessor = []
    
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setInput(self, inp):
        self.input = inp

    def setOutput(self, out):
        self.output = out

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado
    