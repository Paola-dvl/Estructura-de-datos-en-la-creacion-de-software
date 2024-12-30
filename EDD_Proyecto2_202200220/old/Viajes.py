import Cliente, Rutas, Vehiculos

class Viaje:
    def __init__(self, id, lugarOrigen, lugarDestino, fecha, cliente, vehiculo, rutaElegida):
        self.id = id
        self.lugarOrigen = lugarOrigen
        self.lugarDestino = lugarDestino
        self.fecha = fecha

        self.cliente = cliente
        self.vehiculo = vehiculo
        self.rutaElegida = rutaElegida

        self.siguiente = None

    def __str__(self):
        return f"""
            id: {self.id}
            \tlugar de origen: {self.lugarOrigen}
            \tlugar destino: {self.lugarDestino}
            \tfecha: {self.fecha}
            \tcliente: {self.cliente}
            \tvehiculo: {self.vehiculo}
            \n
        """
    
class RutaElegida:
    def __init__(self, lugar, tiempo):
        self.lugar = lugar
        self.tiempo = tiempo
        self.siguiente = None

    def __str__(self):
        return f'{self.lugar} / {self.tiempo}'

    def __repr__(self):
        return str(self)
    
class ListaSimpleRutaElegida:
    def __init__(self):
        self.primero = None
    
    def vacia(self):
        return self.primero == None
    
    def agregar(self, lugar, tiempo):
        if self.vacia():
            self.primero = RutaElegida(lugar, tiempo)
        else:
            ruta = RutaElegida(lugar, tiempo)
            ruta.siguiente = self.primero
            self.primero = ruta
    
class ListaSimpleViaje:
    def __init__(self):
        self.primero = None
    
    def vacia(self):
        return self.primero == None
    
    def obtenerRutaOptima(self, origen, destino):
        rutaOptima = ListaSimpleRutaElegida()
        rutaOrigen = Rutas.ruta[origen]
        if not rutaOrigen.vacia():
            tiempoAcumulado = 0
            lugaresVisitados = [[origen, tiempoAcumulado]]
            while True:
                ruta = rutaOrigen.primero
                while ruta != None:
                    if ruta.destino == destino:
                        tiempoAcumulado += ruta.tiempo
                        lugaresVisitados.append([ruta.destino, tiempoAcumulado])
                        break
                    elif ruta.destino not in [lugar[0] for lugar in lugaresVisitados]:
                        tiempoAcumulado += ruta.tiempo
                        lugaresVisitados.append([ruta.destino, tiempoAcumulado])
                        rutaOrigen = Rutas.ruta[ruta.destino]
                        break
                    ruta = ruta.siguiente
                if ruta == None:
                    break
        return rutaOptima
    
    def agregar(self, id, lugarOrigen, lugarDestino, fecha, cliente, vehiculo):    
        if self.vacia():
            rutaElegida = self.obtenerRutaOptima(lugarOrigen, lugarDestino)
            if rutaElegida.vacia():
                print("No hay rutas disponibles")
                return
            self.primero = Viaje(id, lugarOrigen, lugarDestino, fecha, cliente, vehiculo, rutaElegida)
        else:
            rutaElegida = self.obtenerRutaOptima(lugarOrigen, lugarDestino)
            if rutaElegida.vacia():
                print("No hay rutas disponibles")
                return
            viaje = Viaje(id, lugarOrigen, lugarDestino, fecha, cliente, vehiculo, rutaElegida)
            viaje.siguiente = self.primero
            self.primero = viaje