class Pilha:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "Pilha vazia!"

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "Pilha vazia!"

    def size(self):
        return len(self.itens)

pilha = Pilha()
pilha.push(10)
pilha.push(20)
print(pilha.peek())  
pilha.pop()
print(pilha.peek())  

#:V