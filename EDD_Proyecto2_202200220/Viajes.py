import random

class RutaTomada:
    def __init__(self, lugar, tiempo):
        self.lugar = lugar
        self.tiempo = tiempo
        self.siguiente = None

    def __str__(self):
        return f"Lugar: {self.lugar} | Tiempo: {self.tiempo}"
    
    def __repr__(self):
        return str(self)

class Viaje:
    def __init__(self, origen, destino, fecha, cliente, vehiculo):
        self.id = random.randint(10000, 99999)
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.rutaTomada = None
        self.siguiente = None

    def __str__(self):
        return f"Id: {self.id} | Origen: {self.origen} | Destino: {self.destino} | Fecha: {self.fecha} | Cliente: {self.cliente} | Vehiculo: {self.vehiculo} "
    
    def __repr__(self):
        return str(self)
    
    def agregarRutaTomada(self, lugar, tiempo):
        if self.rutaTomada == None:
            self.rutaTomada = RutaTomada(lugar, tiempo)
        else:
            tmp = self.rutaTomada
            while tmp.siguiente != None:
                tmp = tmp.siguiente
            tmp.siguiente = RutaTomada(lugar, tiempo)
    
class ListaSimpleViaje:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar(self, viaje):
        if self.inicio == None:
            self.inicio = viaje
            self.fin = viaje
        else:
            self.fin.siguiente = viaje
            self.fin = viaje

    def mostrar(self):
        tmp = self.inicio
        while tmp != None:
            print(tmp)
            tmp = tmp.siguiente

    def buscar(self, id):
        tmp = self.inicio
        while tmp != None:
            if tmp.id == id:
                return tmp
            tmp = tmp.siguiente
        return None

    def eliminar(self, id):
        if self.inicio == None:
            return False
        tmp = self.inicio
        if tmp.id == id:
            self.inicio = tmp.siguiente
            return True
        while tmp.siguiente != None:
            if tmp.siguiente.id == id:
                tmp.siguiente = tmp.siguiente.siguiente
                return True
            tmp = tmp.siguiente
        return False

    def listarViajes(self):
        viajes = []
        tmp = self.inicio
        while tmp != None:
            viajes.append(f"Id: {tmp.id} | Origen: {tmp.origen} | Destino: {tmp.destino} | Fecha: {tmp.fecha} | Cliente: {tmp.cliente} | Vehiculo: {tmp.vehiculo}")
            tmp = tmp.siguiente
        return viajes
     
    def listar5ViajesLargos(self):
        viajes = []
        tmp = self.inicio
        while tmp != None:
            cantidadDestinos = 0
            tmpRuta = tmp.rutaTomada
            while tmpRuta != None:
                cantidadDestinos += 1
                tmpRuta = tmpRuta.siguiente
            if len(viajes) < 5:
                viajes.append((f"Id: {tmp.id} - Origen: {tmp.origen}, Destino: {tmp.destino}", cantidadDestinos))
            else:
                viajes.sort(key=lambda x: x[1], reverse=True) 
                if cantidadDestinos > viajes[-1][1]:
                    viajes[-1] = (f"Id: {tmp.id} - Origen: {tmp.origen}, Destino: {tmp.destino}", cantidadDestinos)
            tmp = tmp.siguiente
        viajes.sort(key=lambda x: x[1], reverse=True)
        return viajes
     
    def listar5ViajesGanancia(self):
        viajes = []
        tmp = self.inicio
        while tmp != None:
            tiempo = 0
            tmpRuta = tmp.rutaTomada
            while tmpRuta != None:
                tiempo += tmpRuta.tiempo
                tmpRuta = tmpRuta.siguiente
            if len(viajes) < 5:
                viajes.append((f"Id: {tmp.id} - Origen: {tmp.origen}, Destino: {tmp.destino}", tiempo))
            else:
                viajes.sort(key=lambda x: x[1], reverse=True) 
                if tiempo > viajes[-1][1]:
                    viajes[-1] = (f"Id: {tmp.id} - Origen: {tmp.origen}, Destino: {tmp.destino}", tiempo)
            tmp = tmp.siguiente
        viajes.sort(key=lambda x: x[1], reverse=True)
        return viajes
    
    def listar5ClientesViajes(self):
        clientes = {}
        tmp = self.inicio
        while tmp != None:
            key = f"DPI: {tmp.cliente.dpi} - Nombre: {tmp.cliente.nombre} Apellido: {tmp.cliente.apellido}"
            if key in clientes:
                clientes[key] += 1
            else:
                clientes[key] = 1
            tmp = tmp.siguiente
        clientes = [(k, v) for k, v in clientes.items()]
        clientes.sort(key=lambda x: x[1], reverse=True)
        return clientes[:5]
    
    def listar5VehiculosViajes(self):
        vehiculos = {}
        tmp = self.inicio
        while tmp != None:
            key = f"Placa: {tmp.vehiculo[1].placa} - Marca: {tmp.vehiculo[1].marca}"
            if key in vehiculos:
                vehiculos[key] += 1
            else:
                vehiculos[key] = 1
            tmp = tmp.siguiente
        vehiculos = [(k, v) for k, v in vehiculos.items()]
        vehiculos.sort(key=lambda x: x[1], reverse=True)
        return vehiculos[:5]

    def generarDotString(self):
        dot = "digraph G {\n"
        dot += "\tnode [shape=record];\n"
        dot += "\tlabel=\"Viajes\";\n"
        tmp = self.inicio
        while tmp != None:
            c = 0
            tiempoAnterior = None
            tmpRuta = tmp.rutaTomada
            while tmpRuta != None:
                if tiempoAnterior != None:
                    dot += f"\tn{tmp.id}_{c} [label=\"{{ Lugar: {tmpRuta.lugar} | Tiempo: {tiempoAnterior} + {tmpRuta.tiempo} = {tiempoAnterior + tmpRuta.tiempo} }} | <p>\"];\n"
                else:
                    tiempoAnterior = tmpRuta.tiempo
                    dot += f"\tn{tmp.id}_{c} [label=\"{{ Lugar: {tmpRuta.lugar} | Tiempo: {tmpRuta.tiempo} }} | <p>\"];\n"
                if c > 0:
                    dot += f"\tn{tmp.id}_{c-1}:p -> n{tmp.id}_{c};\n"
                tiempoAnterior += tmpRuta.tiempo
                tmpRuta = tmpRuta.siguiente
                c += 1
            tmp = tmp.siguiente
        dot += "}"
        return dot

    def generarDotStringId(self, id):
        dot = "digraph G {\n"
        dot += "\tnode [shape=record];\n"
        dot += "\tlabel=\"Ruta de un viaje\";\n"
        tmp = self.inicio
        while tmp != None:
            if str(tmp.id) == id:
                c = 0
                tiempoAnterior = None
                tmpRuta = tmp.rutaTomada
                while tmpRuta != None:
                    if tiempoAnterior != None:
                        dot += f"\tn{tmp.id}_{c} [label=\"{{ Lugar: {tmpRuta.lugar} | Tiempo: {tiempoAnterior} + {tmpRuta.tiempo} = {tiempoAnterior + tmpRuta.tiempo} }} | <p>\"];\n"
                    else:
                        tiempoAnterior = tmpRuta.tiempo
                        dot += f"\tn{tmp.id}_{c} [label=\"{{ Lugar: {tmpRuta.lugar} | Tiempo: {tmpRuta.tiempo} }} | <p>\"];\n"
                    if c > 0:
                        dot += f"\tn{tmp.id}_{c-1}:p -> n{tmp.id}_{c};\n"
                    tiempoAnterior += tmpRuta.tiempo
                    tmpRuta = tmpRuta.siguiente
                    c += 1
                break
            tmp = tmp.siguiente
        dot += "}"
        return dot

    def generarDotStringLargos(self, idList, titulo):
        dot = "digraph G {\n"
        dot += "\tnode [shape=record];\n"
        dot += "\tlabel=\"Top Viajes\";\n"
        dot += "\tn [label=\"{"
        dot += f" {titulo}"
        for id, cantidad in idList:
            dot += f" | {{{id} | Cantidad: {cantidad} }}"
        dot += "}\"];\n"
        dot += "}"
        return dot
    

