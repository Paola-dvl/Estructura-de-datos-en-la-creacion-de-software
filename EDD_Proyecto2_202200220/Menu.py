from Clientes import *
from Rutas import *
from Vehiculos import *
from Viajes import *
import os

class Menu:
    def __init__(self):
        self.clientes = ListaCircularDobleCliente()
        self.rutas = ListaAdyacenciaLugar()
        self.vehiculos = ArbolB5Vehiculo(3)
        self.viajes = ListaSimpleViaje()

        self.procesarArchivocliente()
        self.procesarArchivoruta()
        self.procesarArchivovehiculo()
        #self.clientes.agregar(Cliente("123", "Juan", "Perez", "M", "12345678", "Ciudad"))
        #self.clientes.agregar(Cliente("1234567890102", "Maria", "Gonzalez", "F", "87654321", "Ciudad2"))
        #self.rutas.agregar(Lugar("A", 5), Lugar("B", 5))
        #self.rutas.agregar(Lugar("A", 6), Lugar("C", 6))
        #self.rutas.agregar(Lugar("A", 7), Lugar("D", 7))
        #self.rutas.agregar(Lugar("A", 8), Lugar("F", 8))
        #self.rutas.agregar(Lugar("C", 1), Lugar("B", 1))
        #self.rutas.agregar(Lugar("F", 2), Lugar("B", 2))
        #self.rutas.agregar(Lugar("D", 4), Lugar("Z", 4))
        #self.rutas.agregar(Lugar("B", 7), Lugar("Z", 7))
        #self.vehiculos.insertar(("123", Vehiculo("123", "Toyota", "Corolla", 5)))

    def menu(self):
        while True:
            print("1. Clientes")
            print("2. Rutas")
            print("3. Vehiculos")
            print("4. Viajes")
            print("5. Reportes")
            print("6. Salir")
            opcion = input("Elija una opción: ")
            if opcion == "1":
                self.menuCliente()
            elif opcion == "2":
                self.menuRuta()
            elif opcion == "3":
                self.menuVehiculo()
            elif opcion == "4":
                self.menuViaje()
            elif opcion == "5":
                self.menuReporte()
            elif opcion == "6":
                break
            else:
                print("Opción inválida")
    
    def menuCliente(self):
        while True:
            print("1. Agregar")
            print("2. Mostrar")
            print("3. Buscar")
            print("4. Eliminar")
            print("5. Modificar")
            print("6. Regresar")
            opcion = input("Elija una opción: ")
            if opcion == "1":
                print("Ingrese los datos del cliente")
                dpi = input("DPI: ")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                genero = input("Genero: ")
                telefono = input("Telefono: ")
                direccion = input("Direccion: ")
                cliente = Cliente(dpi, nombre, apellido, genero, telefono, direccion)
                print(self.clientes.agregar(cliente))
            elif opcion == "2":
                self.generarGraphics(self.clientes.generarDotString())
            elif opcion == "3":
                print("Ingrese el DPI del cliente")
                cliente = self.clientes.buscar(input("DPI: "))
                if cliente is not None:
                    print(cliente)
                else:
                    print("No se encontró el cliente")
            elif opcion == "4":
                print("Ingrese el DPI del cliente")
                eliminado = self.clientes.eliminar(input("DPI: "))
                if eliminado:
                    print("Cliente eliminado")
                else:
                    print("No se encontró el cliente")
            elif opcion == "5":
                print("Ingrese el DPI del cliente")
                dpi = input("DPI: ")
                cliente = self.clientes.buscar(dpi)
                if cliente is not None:
                    print(cliente)
                    print("Ingrese los nuevos datos del cliente")
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    genero = input("Genero: ")
                    telefono = input("Telefono: ")
                    direccion = input("Direccion: ")
                    self.clientes.modificar(dpi, nombre, apellido, genero, telefono, direccion)
                    print("Cliente modificado")
                else:
                    print("No se encontró el cliente")
            elif opcion == "6":
                print("Regresando...")
                break
            else:
                print("Opción inválida")

    def menuVehiculo(self):
        while True:
            print("1. Agregar")
            print("2. Mostrar")
            print("3. Buscar")
            print("4. Eliminar")
            print("5. Modificar")
            print("6. Regresar")
            opcion = input("Elija una opción: ")
            if opcion == "1":
                print("Ingrese los datos del vehiculo")
                placa = input("Placa: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                precio = input("Precio por segundo: ")
                vehiculo = self.vehiculos.buscar(self.vehiculos.raiz, (placa,)) #Asi estaba en la documentacion :c
                if vehiculo is not None:
                    print("Ya existe un vehiculo con esa placa")
                    continue
                vehiculo = Vehiculo(placa, marca, modelo, precio)
                self.vehiculos.insertar((placa, vehiculo))
            elif opcion == "2":
                self.generarGraphics(self.vehiculos.generarDotString())
            elif opcion == "3":
                print("Ingrese la placa del vehiculo")
                vehiculo = self.vehiculos.buscar(self.vehiculos.raiz, (input("Placa:"),))
                if vehiculo is not None:
                    print(vehiculo)
                else:
                    print("No se encontró el vehiculo")
            elif opcion == "4":
                print("Ingrese la placa del vehiculo")
                placa = input("Placa: ")
                vehiculo = self.vehiculos.buscar(self.vehiculos.raiz, (placa,))
                if vehiculo is None:
                    print("No se encontró el vehiculo")
                    continue
                self.vehiculos.eliminar(self.vehiculos.raiz, (placa,))
                print("Vehiculo eliminado")
            elif opcion == "5":
                print("Ingrese la placa del vehiculo")
                placa = input("Placa: ")
                vehiculo = self.vehiculos.buscar(self.vehiculos.raiz, (placa,))
                if vehiculo is not None:
                    print(vehiculo)
                    print("Ingrese los nuevos datos del vehiculo")
                    marca = input("Marca: ")
                    modelo = input("Modelo: ")
                    precio = input("Precio por segundo: ")
                    self.vehiculos.modificar(self.vehiculos.raiz, (placa,), marca, modelo, precio)
                    print("Vehiculo modificado")
                else:
                    print("No se encontró el vehiculo")
            elif opcion == "6":
                print("Regresando...")
                break
            else:
                print("Opción inválida")

    def menuRuta(self):
        while True:
            print("1. Agregar")
            print("2. Mostrar")
            print("3. Buscar")
            print("4. Eliminar")
            print("5. Modificar")
            print("6. Regresar")
            opcion = input("Elija una opción: ")
            if opcion == "1":
                print("Ingrese los datos de la ruta")
                origen = input("Origen: ")
                destino = input("Destino: ")
                tiempo = input("Tiempo: ")
                if tiempo.isnumeric() == False:
                    print("El tiempo debe ser un número")
                    continue
                elif tiempo == "0":
                    print("El tiempo no puede ser 0")
                    continue
                elif tiempo[0] == "-":
                    print("El tiempo no puede ser negativo")
                    continue
                if self.rutas.buscar(origen, destino) is not None:
                    print("Ya existe una ruta entre esos lugares")
                    continue
                lugarOrigen = Lugar(origen, tiempo)
                lugarDestino = Lugar(destino, tiempo)
                self.rutas.agregar(lugarOrigen, lugarDestino)
            elif opcion == "2":
                self.generarGraphics(self.rutas.generarDotString())
            elif opcion == "3":
                print("Ingrese el origen de la ruta")
                origen = input("Origen: ")
                print("Ingrese el destino de la ruta")
                destino = input("Destino: ")
                ruta = self.rutas.buscar(origen, destino)
                if ruta is not None:
                    print("Ruta encontrada")
                    print(f"Origen: {origen}")
                    print(f"Destino: {destino}")
                    print(f"Tiempo: {ruta.tiempo}")
                else:
                    print("No se encontró la ruta")
            elif opcion == "4":
                print("Ingrese el origen de la ruta")
                origen = input("Origen: ")
                print("Ingrese el destino de la ruta")
                destino = input("Destino: ")
                eliminado = self.rutas.eliminar(origen, destino)
                if eliminado:
                    self.rutas.eliminar(destino, origen)
                    print("Ruta eliminada")
                else:
                    print("No se encontró la ruta")
            elif opcion == "5":
                print("Ingrese el origen de la ruta")
                origen = input("Origen: ")
                print("Ingrese el destino de la ruta")
                destino = input("Destino: ")
                ruta = self.rutas.buscar(origen, destino)
                if ruta is not None:
                    print(ruta)
                    print("Ingrese los nuevos datos de la ruta")
                    origenNuevoNombre = input("Origen (Se cambiará el nombre de origen): ")
                    destinoNuevoNombre = input("Destino (Se cambiará el nombre de destino): ")
                    tiempo = input("Tiempo: ")
                    if tiempo.isnumeric() == False:
                        print("El tiempo debe ser un número")
                        continue
                    elif tiempo == "0":
                        print("El tiempo no puede ser 0")
                        continue
                    elif tiempo[0] == "-":
                        print("El tiempo no puede ser negativo")
                        continue
                    if self.rutas.modificar(origen, origenNuevoNombre, destino, destinoNuevoNombre, tiempo):
                        print("Ruta modificada")
                    else:
                        print("No se pudo modificar la ruta, el nuevo nombre de origen o destino no es válido")
                else:
                    print("No se encontró la ruta")
            elif opcion == "6":
                print("Regresando...")
                break
            else:
                print("Opción inválida")

    def menuViaje(self):
        while True:
            print("1. Agregar")
            print("2. Mostrar")
            print("3. Buscar")
            print("4. Eliminar")
            print("5. Regresar")
            opcion = input("Elija una opción: ")
            if opcion == "1":
                print("Ingrese los datos del viaje")
                print("Lugares:")
                lugares = self.rutas.listarLugares()
                print(lugares)
                origen = input("Origen: ")
                destino = input("Destino: ")
                if origen not in lugares or destino not in lugares:
                    print("No se encontró el origen o destino")
                    continue
                fecha = input("Fecha: ")
                print("Clientes:")
                clientes = self.clientes.listarClientes()
                print(clientes)
                dpi = input("DPI del cliente: ")
                cliente = self.clientes.buscar(dpi)
                if cliente is None:
                    print("No se encontró el cliente")
                    continue
                print("Vehiculos:")
                vehiculos = self.vehiculos.listarVehiculos(self.vehiculos.raiz)
                print(vehiculos)
                placa = input("Placa del vehiculo: ")
                vehiculo = self.vehiculos.buscar(self.vehiculos.raiz, (placa,))
                if vehiculo is None:
                    print("No se encontró el vehiculo")
                    continue
                rutaOptima = self.rutas.generarRutaOptima(origen, destino)
                if rutaOptima is None:
                    print("No se encontró una ruta entre esos lugares")
                    continue
                print("Ruta óptima:")
                print(rutaOptima)
                viaje = Viaje(origen, destino, fecha, cliente, vehiculo)
                for lugar, tiempo in rutaOptima:
                    viaje.agregarRutaTomada(lugar, tiempo)
                self.viajes.insertar(viaje)
            elif opcion == "2":
                self.generarGraphics(self.viajes.generarDotString())
            elif opcion == "3":
                viajes = self.viajes.listarViajes()
                print(viajes)
                print("Ingrese el ID del viaje")
                viaje = self.viajes.buscar(input("ID: "))
                if viaje is not None:
                    print(viaje)
                    print(viaje.rutaTomada)
                else:
                    print("No se encontró el viaje")
            elif opcion == "4":
                viajes = self.viajes.listarViajes()
                print(viajes)
                print("Ingrese el ID del viaje")
                eliminado = self.viajes.eliminar(input("ID: "))
                if eliminado:
                    print("Viaje eliminado")
                else:
                    print("No se encontró el viaje")
            elif opcion == "5":
                print("Regresando...")
                break
            else:
                print("Opción inválida")

    def menuReporte(self):
        while True:
            print("1. Top Viajes")
            print("2. Top Ganancia")
            print("3. Top Clientes")
            print("4. Top Vehículos")
            print("5. Ruta de un viaje")
            print("6. Regresar")
            opcion = input("Elija una opción: ")
            if opcion == "1":
                viajes = self.viajes.listar5ViajesLargos()
                self.generarGraphics(self.viajes.generarDotStringLargos(viajes, "Top 5 Viajes más largos"))
            elif opcion == "2":
                viajes = self.viajes.listar5ViajesGanancia()
                self.generarGraphics(self.viajes.generarDotStringLargos(viajes, "Top 5 Viajes más caros"))
            elif opcion == "3":
                viajes = self.viajes.listar5ClientesViajes()
                self.generarGraphics(self.viajes.generarDotStringLargos(viajes, "Top 5 Clientes con más viajes"))
            elif opcion == "4":
                viajes = self.viajes.listar5VehiculosViajes()
                self.generarGraphics(self.viajes.generarDotStringLargos(viajes, "Top 5 Vehículos con más viajes"))
            elif opcion == "5":
                print("Viajes:")
                viajes = self.viajes.listarViajes()
                print(viajes)
                print("Ingrese el ID del viaje")
                self.generarGraphics(self.viajes.generarDotStringId(input("ID: ")))
            elif opcion == "6":
                print("Regresando...")
                break
            else:
                print("Opción inválida")

    def generarGraphics(self, dotString):
        with open("graph.dot", "w") as file:
            file.write(dotString)
        os.system("dot -Tpng graph.dot -o graph.png")
        os.system("graph.png")

    def procesarArchivocliente(self):
        with open("Clientes.txt", 'r') as file:
            lineas = file.readlines()
            for linea in lineas:
                linea = linea.strip()
                if linea: 
                    partes = linea.split(',')
                    if len(partes) == 6:  
                        id_cliente = partes[0].strip()
                        nombre = partes[1].strip()
                        apellido = partes[2].strip()
                        genero = partes[3].strip()
                        telefono = partes[4].strip()
                        direccion = partes[5].strip()
                        cliente = Cliente(id_cliente, nombre, apellido, genero, telefono, direccion)
                        self.clientes.agregar(cliente)

    def procesarArchivoruta(self):
        with open("Rutas.txt", 'r') as file:
            lineas = file.readlines()
            for linea in lineas:
                linea = linea.strip()
                if linea: 
                    partes = linea.split('/')
                    if len(partes) == 3: 
                        origen = partes[0].strip()
                        destino = partes[1].strip()
                        distancia = int(partes[2].strip().replace('%', ''))
                        lugar1 = Lugar(origen, distancia)
                        lugar2 = Lugar(destino, distancia)
                        self.rutas.agregar(lugar1, lugar2)

    def procesarArchivovehiculo(self):
        with open("Vehiculos.txt", 'r') as file:
            lineas = file.readlines()
            for linea in lineas:
                linea = linea.strip()
                if linea: 
                    partes = linea.split(';')
                    partes = partes[0].split(':')
                    if len(partes) == 4: 
                        placa = partes[0].strip()
                        marca = partes[1].strip()
                        modelo = partes[2].strip()
                        consumo = float(partes[3].strip())
                        vehiculo = Vehiculo(placa, marca, modelo, consumo)
                        print(vehiculo)
                        self.vehiculos.insertar((placa, vehiculo))
        #self.vehiculos.insertar(("123", Vehiculo("123", "Toyota", "Corolla", 5)))

if __name__ == "__main__":
    menu = Menu()
    menu.menu()