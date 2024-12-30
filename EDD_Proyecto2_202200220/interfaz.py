from Clientes import *
from Rutas import *
from Vehiculos import *
from Viajes import *
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog

class LlegaRapiditoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Llega Rapidito - Gestión de Transporte")
        self.geometry("800x600")
        self.clientes = ListaCircularDobleCliente()
        self.rutas = ListaAdyacenciaLugar()
        self.vehiculos = ArbolB5Vehiculo(3)
        self.viajes = ListaSimpleViaje()

        
        self.procesarArchivocliente()
        self.procesarArchivoruta()
        self.procesarArchivovehiculo()

        # Configuración del menú principal
        self.create_main_menu()

    
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


    def create_main_menu(self):
        tk.Label(self, text="Bienvenido a Llega Rapidito", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self, text="Cargar Rutas", command=self.load_routes).pack(pady=10)

        sections = [
            ("Clientes", self.open_clients_menu),
            ("Vehículos", self.open_vehicles_menu),
            ("Rutas", self.open_routes_menu),
            ("Viajes", self.open_trips_menu),
            ("Reportes", self.open_reports_menu)
        ]

        for text, command in sections:
            tk.Button(self, text=text, width=20, command=command).pack(pady=5)

    def load_routes(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if file_path:
            messagebox.showinfo("Cargar Rutas", f"Archivo cargado: {file_path}")
        else:
            messagebox.showwarning("Cargar Rutas", "No se seleccionó ningún archivo.")

    def open_clients_menu(self):
        ClientsMenu(self)

    def open_vehicles_menu(self):
        VehiclesMenu(self)

    def open_routes_menu(self):
        RoutesMenu(self)

    def open_trips_menu(self):
        TripsMenu(self)

    def open_reports_menu(self):
        ReportsMenu(self)

class ClientsMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestión de Clientes")
        self.geometry("600x400")

        tk.Label(self, text="Gestión de Clientes", font=("Arial", 14)).pack(pady=10)
        
        buttons = [
            ("Agregar Cliente", self.add_client),
            ("Mostrar Clientes", self.show_clients),
            ("Buscar Cliente", self.search_client),
            ("Eliminar Cliente", self.delete_client),
            ("Modificar Cliente", self.modify_client),
        ]

        for text, command in buttons:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)

    def add_client(self):
        dpi = simpledialog.askstring("Agregar Cliente", "Ingrese DPI:")
        nombre = simpledialog.askstring("Agregar Cliente", "Ingrese Nombre:")
        apellido = simpledialog.askstring("Agregar Cliente", "Ingrese Apellido:")
        genero = simpledialog.askstring("Agregar Cliente", "Ingrese Género:")
        telefono = simpledialog.askstring("Agregar Cliente", "Ingrese Teléfono:")
        direccion = simpledialog.askstring("Agregar Cliente", "Ingrese Dirección:")

        if dpi and nombre and apellido and genero and telefono and direccion:
            cliente = Cliente(dpi, nombre, apellido, genero, telefono, direccion)
            messagebox.showinfo("Agregar Cliente", self.master.clientes.agregar(cliente))
        else:
            messagebox.showwarning("Agregar Cliente", "Todos los campos son obligatorios.")

    def show_clients(self):
        dot_string = self.master.clientes.generarDotString()
        self.generate_graphics(dot_string)

    def search_client(self):
        dpi = simpledialog.askstring("Buscar Cliente", "Ingrese DPI:")
        cliente = self.master.clientes.buscar(dpi)
        if cliente:
            messagebox.showinfo("Buscar Cliente", str(cliente))
        else:
            messagebox.showwarning("Buscar Cliente", "Cliente no encontrado.")

    def delete_client(self):
        dpi = simpledialog.askstring("Eliminar Cliente", "Ingrese DPI:")
        if self.master.clientes.eliminar(dpi):
            messagebox.showinfo("Eliminar Cliente", "Cliente eliminado.")
        else:
            messagebox.showwarning("Eliminar Cliente", "Cliente no encontrado.")

    def modify_client(self):
        dpi = simpledialog.askstring("Modificar Cliente", "Ingrese DPI:")
        cliente = self.master.clientes.buscar(dpi)
        if cliente:
            nombre = simpledialog.askstring("Modificar Cliente", "Ingrese nuevo Nombre:")
            apellido = simpledialog.askstring("Modificar Cliente", "Ingrese nuevo Apellido:")
            genero = simpledialog.askstring("Modificar Cliente", "Ingrese nuevo Género:")
            telefono = simpledialog.askstring("Modificar Cliente", "Ingrese nuevo Teléfono:")
            direccion = simpledialog.askstring("Modificar Cliente", "Ingrese nueva Dirección:")

            if nombre and apellido and genero and telefono and direccion:
                self.master.clientes.modificar(dpi, nombre, apellido, genero, telefono, direccion)
                messagebox.showinfo("Modificar Cliente", "Cliente modificado.")
            else:
                messagebox.showwarning("Modificar Cliente", "Todos los campos son obligatorios.")
        else:
            messagebox.showwarning("Modificar Cliente", "Cliente no encontrado.")

    def generate_graphics(self, dot_string):
        with open("clients_graph.dot", "w") as file:
            file.write(dot_string)
        os.system("dot -Tpng clients_graph.dot -o clients_graph.png")
        os.system("clients_graph.png")
        
        
class VehiclesMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestión de Vehículos")
        self.geometry("600x400")

        tk.Label(self, text="Gestión de Vehículos", font=("Arial", 14)).pack(pady=10)

        buttons = [
            ("Agregar Vehículo", self.add_vehicle),
            ("Mostrar Vehículos", self.show_vehicles),
            ("Buscar Vehículo", self.search_vehicle),
            ("Eliminar Vehículo", self.delete_vehicle),
            ("Modificar Vehículo", self.modify_vehicle),
        ]

        for text, command in buttons:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)

    def generate_graphics(self, dot_string):
        with open("clients_graph.dot", "w") as file:
            file.write(dot_string)
        os.system("dot -Tpng clients_graph.dot -o clients_graph.png")
        os.system("clients_graph.png")

    def add_vehicle(self):
        placa = simpledialog.askstring("Agregar Vehículo", "Ingrese Placa:")
        marca = simpledialog.askstring("Agregar Vehículo", "Ingrese Marca:")
        modelo = simpledialog.askstring("Agregar Vehículo", "Ingrese Modelo:")
        precio = simpledialog.askstring("Agregar Vehículo", "Ingrese Precio por Segundo:")

        if placa and marca and modelo and precio:
            vehiculo = Vehiculo(placa, marca, modelo, precio)
            existing_vehicle = self.master.vehiculos.buscar(self.master.vehiculos.raiz, (placa,))
            if existing_vehicle:
                messagebox.showwarning("Agregar Vehículo", "Ya existe un vehículo con esa placa.")
            else:
                self.master.vehiculos.insertar((placa, vehiculo))
                messagebox.showinfo("Agregar Vehículo", "Vehículo agregado.")
        else:
            messagebox.showwarning("Agregar Vehículo", "Todos los campos son obligatorios.")

    def show_vehicles(self):
        dot_string = self.master.vehiculos.generarDotString()
        self.generate_graphics(dot_string)

    def search_vehicle(self):
        placa = simpledialog.askstring("Buscar Vehículo", "Ingrese Placa:")
        vehiculo = self.master.vehiculos.buscar(self.master.vehiculos.raiz, (placa,))
        if vehiculo:
            messagebox.showinfo("Buscar Vehículo", str(vehiculo))
        else:
            messagebox.showwarning("Buscar Vehículo", "Vehículo no encontrado.")

    def delete_vehicle(self):
        placa = simpledialog.askstring("Eliminar Vehículo", "Ingrese Placa:")
        vehiculo = self.master.vehiculos.buscar(self.master.vehiculos.raiz, (placa,))
        if vehiculo:
            self.master.vehiculos.eliminar(self.master.vehiculos.raiz, (placa,))
            messagebox.showinfo("Eliminar Vehículo", "Vehículo eliminado.")
        else:
            messagebox.showwarning("Eliminar Vehículo", "Vehículo no encontrado.")

    def modify_vehicle(self):
        placa = simpledialog.askstring("Modificar Vehículo", "Ingrese Placa:")
        vehiculo = self.master.vehiculos.buscar(self.master.vehiculos.raiz, (placa,))
        if vehiculo:
            marca = simpledialog.askstring("Modificar Vehículo", "Nueva Marca:")
            modelo = simpledialog.askstring("Modificar Vehículo", "Nuevo Modelo:")
            precio = simpledialog.askstring("Modificar Vehículo", "Nuevo Precio por Segundo:")
            self.master.vehiculos.modificar(self.master.vehiculos.raiz, (placa,), marca, modelo, precio)
            messagebox.showinfo("Modificar Vehículo", "Vehículo modificado.")
        else:
            messagebox.showwarning("Modificar Vehículo", "Vehículo no encontrado.")


class RoutesMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestión de Rutas")
        self.geometry("600x400")

        tk.Label(self, text="Gestión de Rutas", font=("Arial", 14)).pack(pady=10)

        buttons = [
            ("Agregar Ruta", self.add_route),
            ("Mostrar Rutas", self.show_routes),
            ("Buscar Ruta", self.search_route),
            ("Eliminar Ruta", self.delete_route),
            ("Modificar Ruta", self.modify_route),
        ]

        for text, command in buttons:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)

    def generate_graphics(self, dot_string):
        with open("clients_graph.dot", "w") as file:
            file.write(dot_string)
        os.system("dot -Tpng clients_graph.dot -o clients_graph.png")
        os.system("clients_graph.png")
        
    def add_route(self):
        origen = simpledialog.askstring("Agregar Ruta", "Ingrese Lugar de Origen:")
        destino = simpledialog.askstring("Agregar Ruta", "Ingrese Lugar de Destino:")
        distancia = simpledialog.askstring("Agregar Ruta", "Ingrese Distancia:")

        if origen and destino and distancia:

            ruta = self.rutas.agregar(Lugar(origen, distancia), Lugar(destino, distancia))
            messagebox.showinfo("Agregar Ruta", self.master.rutas.agregar(ruta))
        else:
            messagebox.showwarning("Agregar Ruta", "Todos los campos son obligatorios.")

    def show_routes(self):
        dot_string = self.master.rutas.generarDotString()
        self.generate_graphics(dot_string)

    def search_route(self):
        origen = simpledialog.askstring("Buscar Ruta", "Ingrese Lugar de Origen:")
        ruta = self.master.rutas.buscar(origen)
        if ruta:
            messagebox.showinfo("Buscar Ruta", str(ruta))
        else:
            messagebox.showwarning("Buscar Ruta", "Ruta no encontrada.")

    def delete_route(self):
        origen = simpledialog.askstring("Eliminar Ruta", "Ingrese Lugar de Origen:")
        if self.master.rutas.eliminar(origen):
            messagebox.showinfo("Eliminar Ruta", "Ruta eliminada.")
        else:
            messagebox.showwarning("Eliminar Ruta", "Ruta no encontrada.")

    def modify_route(self):
        origen = simpledialog.askstring("Modificar Ruta", "Ingrese Lugar de Origen:")
        ruta = self.master.rutas.buscar(origen)
        if ruta:
            destino = simpledialog.askstring("Modificar Ruta", "Nuevo Lugar de Destino:")
            distancia = simpledialog.askstring("Modificar Ruta", "Nueva Distancia:")
            self.master.rutas.modificar(origen, destino, distancia)
            messagebox.showinfo("Modificar Ruta", "Ruta modificada.")
        else:
            messagebox.showwarning("Modificar Ruta", "Ruta no encontrada.")

# Similar classes can be created for VehiclesMenu, RoutesMenu, TripsMenu, and ReportsMenu
def TripsMenu(self):
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

def ReportsMenu(self):
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

if __name__ == "__main__":
    app = LlegaRapiditoApp()
    app.mainloop()
