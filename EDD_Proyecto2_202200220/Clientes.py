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
        return f"DPI: {self.dpi} \n Nombre: {self.nombre} \n Apellido: {self.apellido} \n Genero: {self.genero} \n Telefono: {self.telefono} \n Direccion: {self.direccion}"
    
    def __repr__(self):
        return str(self)
    
    def dpi_nombre(self):
        return f"{self.dpi} - {self.nombre} {self.apellido}"

class ListaCircularDobleCliente:
    def __init__(self):
        self.inicio = None

    def buscar(self, dpi):
        if self.inicio is None:
            return None
        temp = self.inicio
        while temp.siguiente is not self.inicio:
            if temp.dpi == dpi:
                return temp
            temp = temp.siguiente
        if temp.dpi == dpi:
            return temp
        return None

    def agregar(self, cliente):
        if self.inicio is None:
            self.inicio = cliente
            self.inicio.siguiente = self.inicio
            self.inicio.anterior = self.inicio
        else:
            temp = self.inicio
            while temp.siguiente is not self.inicio:
                if temp.dpi == cliente.dpi:
                    return "Ya existe"
                temp = temp.siguiente
            if temp.dpi == cliente.dpi:
                return "Ya existe"
            temp.siguiente = cliente
            cliente.anterior = temp
            cliente.siguiente = self.inicio
            self.inicio.anterior = cliente
        return "Agregado"
    
    def eliminar(self, dpi):
        if self.inicio is None:
            return False
        if self.inicio.dpi == dpi:
            if self.inicio.siguiente == self.inicio:
                self.inicio = None
            else:
                self.inicio.anterior.siguiente = self.inicio.siguiente
                self.inicio.siguiente.anterior = self.inicio.anterior
                self.inicio = self.inicio.siguiente
            return True
        temp = self.inicio
        while temp.siguiente is not self.inicio:
            if temp.siguiente.dpi == dpi:
                temp.siguiente = temp.siguiente.siguiente
                temp.siguiente.anterior = temp
                return True
            temp = temp.siguiente
        return False
    
    def modificar(self, dpi, nombre, apellido, genero, telefono, direccion):
        cliente = self.buscar(dpi)
        if cliente is not None:
            cliente.nombre = nombre
            cliente.apellido = apellido
            cliente.genero = genero
            cliente.telefono = telefono
            cliente.direccion = direccion
            return True
        return False
    
    def listarClientes(self):
        clientes = []
        if self.inicio is not None:
            temp = self.inicio
            while temp.siguiente is not self.inicio:
                clientes.append(temp)
                temp = temp.siguiente
            clientes.append(temp)
        return clientes
    
    def generarDotString(self):
        dot = "digraph ListaClientes {\n"
        dot += "\trankdir=LR;\n"
        dot += "\tnode [shape=record];\n"
        dot += "\tlabel=\"Lista Circular Doble de Clientes\";\n"
        if self.inicio is not None:
            temp = self.inicio
            while temp.siguiente is not self.inicio:
                dot += f"\"{temp.dpi}\" -> \"{temp.siguiente.dpi}\"\n"
                dot += f"\"{temp.siguiente.dpi}\" -> \"{temp.dpi}\"\n"
                dot += f"\"{temp.dpi}\" [label=\"DPI: {temp.dpi} | Nombre: {temp.nombre} | Apellido: {temp.apellido} | Genero: {temp.genero} | Telefono: {temp.telefono} | Direccion: {temp.direccion}\"]\n"
                temp = temp.siguiente
            dot += f"\"{temp.dpi}\" -> \"{temp.siguiente.dpi}\"\n"
            dot += f"\"{temp.siguiente.dpi}\" -> \"{temp.dpi}\"\n"
            dot += f"\"{temp.dpi}\" [label=\"DPI: {temp.dpi} | Nombre: {temp.nombre} | Apellido: {temp.apellido} | Genero: {temp.genero} | Telefono: {temp.telefono} | Direccion: {temp.direccion}\"]\n"
        else:
            dot += "empty [label=\"Lista Vacia\"]\n"
        dot += "}"
        return dot