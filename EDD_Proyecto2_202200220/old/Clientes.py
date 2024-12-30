class Cliente:
    def __init__(self, dpi, nombre, apellido, genero, telefono, direccion):
        self.dpi = dpi
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.telefono = telefono
        self.direccion = direccion
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"""
            dpi: {self.dpi}
            \tnombre: {self.nombre}
            \tapellido: {self.apellido}
            \tgenero: {self.genero}
            \ttelefono: {self.telefono}
            \tdireccion: {self.direccion}
            \n
        """
    
class ListaCircularDobleClientes:
    def __init__(self):
        self.primero = None

    def vacia(self):
        return self.primero == None

    def agregar(self, dpi, nombre, apellido, genero, telefono, direccion):
        if self.vacia():
            self.primero = Cliente(dpi, nombre, apellido, genero, telefono, direccion)
            self.primero.siguiente = self.primero.anterior = self.primero
        else:
            cliente = Cliente(dpi, nombre, apellido, genero, telefono, direccion)
            cliente.anterior = self.primero.anterior
            cliente.siguiente = self.primero
            self.primero.anterior.siguiente = cliente
            self.primero.anterior = cliente

    def recorrer(self):
        if self.vacia():
            print("No hay clientes")
        cliente = self.primero
        while True:
            print(cliente)
            cliente = cliente.siguiente
            if cliente == self.primero:
                break

    def eliminar(self, dpi):
        if self.vacia():
            print("No hay clientes")
        elif self.primero.dpi == dpi:
            self.primero = None
            print("Cliente eliminado")
        elif self.primero.dpi == dpi:
            ultimo = self.primero.anterior
            ultimo.siguiente = self.primero.siguiente
            self.primero = self.primero.siguiente
            self.primero.anterior = ultimo
            print("Cliente eliminado")
        else:
            cliente = self.primero
            while cliente.siguiente != self.primero and cliente.siguiente.dpi != dpi:
                cliente = cliente.siguiente
            if cliente.siguiente.dpi == dpi:
                cliente.siguiente = cliente.siguiente.siguiente
                cliente.siguiente.anterior = cliente
                print("Cliente eliminado")
            else:
                print("No se encontro el cliente")

    def buscar(self, dpi):
        if self.vacia():
            print("No hay clientes")
        elif self.primero.dpi == dpi:
            return self.primero
        else:
            cliente = self.primero
            while cliente.siguiente != self.primero and cliente.siguiente.dpi != dpi:
                cliente = cliente.siguiente
            if cliente.siguiente.dpi == dpi:
                return cliente.siguiente
            else:
                print("No se encontro el cliente")
        return None

    def generarDot(self):
        dotString = "digraph ListaEnlazada {\n"
        dotString += "rankdir=LR;\n"
        dotString += "node [shape=record];\n"
        if not self.vacia():
            cliente = self.primero
            while True:
                dotString += f"node{cliente.dpi} [label=\"DPI: {cliente.dpi} | Nombre: {cliente.nombre} | Apellido: {cliente.apellido} | Género: {cliente.genero} | Teléfono: {cliente.telefono} | Dirección: {cliente.direccion}\"];\n"
                cliente = cliente.siguiente
                if cliente == self.primero:
                    break
            cliente = self.primero
            while True:
                dotString += f"node{cliente.dpi} -> node{cliente.siguiente.dpi};\n"
                dotString += f"node{cliente.dpi} -> node{cliente.anterior.dpi};\n"
                cliente = cliente.siguiente
                if cliente == self.primero:
                    break
        dotString += "}"
        return dotString
        