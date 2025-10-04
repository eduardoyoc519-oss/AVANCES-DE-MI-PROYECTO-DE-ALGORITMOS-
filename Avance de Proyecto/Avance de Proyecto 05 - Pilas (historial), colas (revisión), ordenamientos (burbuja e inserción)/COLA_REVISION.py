# implementacion de una cola para mi proyectp
#este nos servira para la revison de las colas que llegen de nuestro clientes 
class cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        # usamos insert(0, item) para que los nuevos elementos queden al principio
        # y pop() elimine el mas antiguo 
        self.items.insert(0, item)
        print(f"cola de revision: {self.items}")

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def tamano(self):
        return len(self.items)
    
    