class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def is_empty(self):
        return self.cabeca is None

    def insert_at_end(self, valor):
        novo_nodo = Nodo(valor)
        if self.is_empty():
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def insert_at_beginning(self, valor):
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo

    def delete(self, valor):
        if self.is_empty():
            return "Lista vazia!"
        atual = self.cabeca
        if atual.valor == valor:
            self.cabeca = atual.proximo
            return
        while atual.proximo and atual.proximo.valor != valor:
            atual = atual.proximo
        if atual.proximo:
            atual.proximo = atual.proximo.proximo

    def display(self):
        if self.is_empty():
            return "Lista vazia!"
        atual = self.cabeca
        elementos = []
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        return elementos

lista = ListaEncadeada()
lista.insert_at_end(10)
lista.insert_at_end(20)
lista.insert_at_beginning(5)
print(lista.display())
lista.delete(10)
print(lista.display()) 

#:V