from abb import ABB
from nodo import Nodo


class AVL(ABB):
    def __init__(self):
        super().__init__()

    def insertar(self, valor):
        self.raiz = self._insertar_avl(self.raiz, valor)

    def _insertar_avl(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_avl(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_avl(nodo.derecho, valor)
        else:
            return nodo

        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))
        balance = self._balance(nodo)

        # Rotación simple derecha
        if balance > 1 and valor < nodo.izquierdo.valor:
            return self._rotar_derecha(nodo)

        # Rotación simple izquierda
        if balance < -1 and valor > nodo.derecho.valor:
            return self._rotar_izquierda(nodo)

        # Rotación izquierda-derecha
        if balance > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)

        # Rotación derecha-izquierda
        if balance < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        return nodo

    def eliminar(self, valor):
        self.raiz = self._eliminar_avl(self.raiz, valor)

    def _eliminar_avl(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_avl(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_avl(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            sucesor = self._minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_avl(nodo.derecho, sucesor.valor)

        if nodo is None:
            return nodo

        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))
        balance = self._balance(nodo)

        # Izquierda - Izquierda
        if balance > 1 and self._balance(nodo.izquierdo) >= 0:
            return self._rotar_derecha(nodo)

        # Izquierda - Derecha
        if balance > 1 and self._balance(nodo.izquierdo) < 0:
            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)

        # Derecha - Derecha
        if balance < -1 and self._balance(nodo.derecho) <= 0:
            return self._rotar_izquierda(nodo)

        # Derecha - Izquierda
        if balance < -1 and self._balance(nodo.derecho) > 0:
            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        return nodo

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def _balance(self, nodo):
        if nodo is None:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def _rotar_derecha(self, y):
        x = y.izquierdo
        t2 = x.derecho

        x.derecho = y
        y.izquierdo = t2

        y.altura = 1 + max(self._altura(y.izquierdo), self._altura(y.derecho))
        x.altura = 1 + max(self._altura(x.izquierdo), self._altura(x.derecho))

        return x

    def _rotar_izquierda(self, x):
        y = x.derecho
        t2 = y.izquierdo

        y.izquierdo = x
        x.derecho = t2

        x.altura = 1 + max(self._altura(x.izquierdo), self._altura(x.derecho))
        y.altura = 1 + max(self._altura(y.izquierdo), self._altura(y.derecho))

        return y