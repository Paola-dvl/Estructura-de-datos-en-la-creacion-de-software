class Lugar:
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo
        self.siguiente = None

    def __str__(self):
        return f"{self.nombre}"
    
    def __repr__(self):
        return str(self)
    
class ListaSimpleLugar:
    def __init__(self):
        self.inicio = None

    def agregar(self, lugar):
        if self.inicio is None:
            self.inicio = lugar
        else:
            temp = self.inicio
            while temp.siguiente is not None:
                if temp.nombre == lugar.nombre:
                    return "Ya existe"
                temp = temp.siguiente
            if temp.nombre == lugar.nombre:
                return "Ya existe"
            temp.siguiente = lugar
        return "Agregado"

class ListaAdyacenciaLugar:
    def __init__(self):
        self.lista = {}

    def agregar(self, origen, destino):
        if origen.nombre not in self.lista:
            self.lista[origen.nombre] = ListaSimpleLugar()
        return self.lista[origen.nombre].agregar(destino)
    
    def getDotString(self):
        dot = "digraph ListaAdyacencia {\n"
        for origen in self.lista:
            temp = self.lista[origen].inicio
            while temp is not None:
                dot += f'"{origen}" -> "{temp.nombre}" [label="{temp.tiempo}"];\n'
                temp = temp.siguiente
        dot += "}"
        return dot
    
    def getDestino(self, origen, destino):
        if origen in self.lista:
            temp = self.lista[origen].inicio
            while temp is not None:
                if temp.nombre == destino:
                    return temp
                temp = temp.siguiente
        return None

    def __str__(self):
        return str(self.lista)

    def __repr__(self):
        return str(self)