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

    def modificar(self, lugar, lugarNuevoNombre, tiempo=None):
        if self.inicio is None:
            return False
        temp = self.inicio
        while temp is not None:
            if temp.nombre == lugar:
                temp.nombre = lugarNuevoNombre
                if tiempo is not None:
                    temp.tiempo = tiempo
                return True
            temp = temp.siguiente
        return False

    def agregar(self, lugar):
        if self.inicio is None:
            self.inicio = lugar
        else:
            temp = self.inicio
            while temp.siguiente is not None:
                if temp.nombre == lugar.nombre:
                    return f"Ya existe {lugar.nombre}"
                temp = temp.siguiente
            if temp.nombre == lugar.nombre:
                return f"Ya existe {lugar.nombre}"
            temp.siguiente = lugar
        return f"Agregado {lugar.nombre}"
    
    def eliminar(self, lugar):
        if self.inicio is None:
            return False
        if self.inicio.nombre == lugar:
            self.inicio = self.inicio.siguiente
            return True
        temp = self.inicio
        while temp.siguiente is not None:
            if temp.siguiente.nombre == lugar:
                temp.siguiente = temp.siguiente.siguiente
                return True
            temp = temp.siguiente
        return False
    
    def buscar(self, lugar):
        if self.inicio is None:
            return None
        temp = self.inicio
        while temp is not None:
            if temp.nombre == lugar:
                return temp
            temp = temp.siguiente
        return None

class ListaAdyacenciaLugar:
    def __init__(self):
        self.lista = {}

    def buscar(self, origen, destino):
        if origen in self.lista:
            return self.lista[origen].buscar(destino)

    def eliminar(self, origen, destino):
        if origen in self.lista:
            return self.lista[origen].eliminar(destino)
        return False

    def agregar(self, origen, destino):
        if origen.nombre not in self.lista:
            self.lista[origen.nombre] = ListaSimpleLugar()
        self.lista[origen.nombre].agregar(destino)
        if destino.nombre not in self.lista:
            self.lista[destino.nombre] = ListaSimpleLugar()
        self.lista[destino.nombre].agregar(origen)
    
    def modificar(self, origen, origenNuevoNombre, destino, destinoNuevoNombre, tiempo):
        if origen != origenNuevoNombre and origenNuevoNombre in self.lista:
            return False
        if destino != destinoNuevoNombre and destinoNuevoNombre in self.lista:
            return False
        if origen in self.lista:
            lista_origen = self.lista[origen]
            if lista_origen.modificar(destino, destinoNuevoNombre, tiempo):
                if origenNuevoNombre != origen:
                        self.lista[origenNuevoNombre] = self.lista.pop(origen)
        if destino in self.lista:
            lista_destino = self.lista[destino]
            if lista_destino.modificar(origen, origenNuevoNombre, tiempo):
                if destinoNuevoNombre != destino:
                    self.lista[destinoNuevoNombre] = self.lista.pop(destino)
        for lugar in self.lista:
            self.lista[lugar].modificar(origen, origenNuevoNombre)
            self.lista[lugar].modificar(destino, destinoNuevoNombre)
        return True
    
    def listarLugares(self):
        lugares = []
        for lugar in self.lista:
            lugares.append(lugar)
        return lugares
    
    def generarRutaOptima(self, origen, destino):
        rutaOptima = []
        lugarActual = self.lista[origen].inicio
        while lugarActual != None:
            #print(f"Lugar actual: {lugarActual.nombre}, tiempo: {lugarActual.tiempo}")
            rutaActual = [(origen, 0)]
            rutaActual.append((lugarActual.nombre, lugarActual.tiempo))
            if lugarActual.nombre == destino:
                if not rutaOptima or lugarActual.tiempo < sum([ruta[1] for ruta in rutaOptima]):
                    rutaOptima = rutaActual.copy()
            else:
                rutaOptima = self.generarRutaOptimaRecursiva(lugarActual.nombre, destino, rutaActual, rutaOptima,  lugarActual.tiempo)
            lugarActual = lugarActual.siguiente
        return rutaOptima
    
    def generarRutaOptimaRecursiva(self, origen, destino, rutaActual, rutaOptima, tiempo):
        lugarActual = self.lista[origen].inicio
        while lugarActual != None:
            #print(f"Deste {origen}, Lugar actual: {lugarActual.nombre}, tiempo: {lugarActual.tiempo}, tiempo total {tiempo}")
            if lugarActual.nombre in [ruta[0] for ruta in rutaActual]:
                lugarActual = lugarActual.siguiente
                continue
            tiempo += lugarActual.tiempo
            rutaActual.append((lugarActual.nombre, lugarActual.tiempo))
            if lugarActual.nombre == destino:
                if not rutaOptima or tiempo < sum([ruta[1] for ruta in rutaOptima]):
                    rutaOptima = rutaActual.copy()
            else:
                rutaOptima = self.generarRutaOptimaRecursiva(lugarActual.nombre, destino, rutaActual, rutaOptima, tiempo)
            rutaActual.pop()
            tiempo -= lugarActual.tiempo
            lugarActual = lugarActual.siguiente
        return rutaOptima
    
    def generarDotString(self):
        dot = "digraph ListaAdyacencia {\n"
        dot += "\tedge [dir=both];\n"
        dot += "\tlabel=\"Lista Adyacencia de Rutas\";\n"
        relaciones = set() 
        for origen in self.lista:
            temp = self.lista[origen].inicio
            while temp is not None:
                relacion = tuple(sorted((origen, temp.nombre)))
                if relacion not in relaciones:
                    dot += f'  "{origen}" -> "{temp.nombre}" [label="{temp.tiempo}"];\n'
                    relaciones.add(relacion)
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