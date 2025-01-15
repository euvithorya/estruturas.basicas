class Fila:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.itens.pop(0)
        else:
            return "Fila vazia!"

    def front(self):
        if not self.is_empty():
            return self.itens[0]
        else:
            return "Fila vazia!"

    def size(self):
        return len(self.itens)

fila = Fila()
fila.enqueue(10)
fila.enqueue(20)
print(fila.front()) 
fila.dequeue()
print(fila.front()) 
