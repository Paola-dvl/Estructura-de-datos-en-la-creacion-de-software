import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class LlegaRapiditoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Llega Rapidito - Gestión de Transporte")
        self.geometry("800x600")

        # Configuración del menú principal
        self.create_main_menu()

    def create_main_menu(self):
        # Etiqueta de bienvenida
        tk.Label(self, text="Bienvenido a Llega Rapidito", font=("Arial", 16)).pack(pady=10)

        # Botón para cargar rutas
        tk.Button(self, text="Cargar Rutas", command=self.load_routes).pack(pady=10)

        # Botones para acceder a las secciones
        sections = [("Clientes", self.open_clients_menu),
                    ("Vehículos", self.open_vehicles_menu),
                    ("Viajes", self.open_trips_menu),
                    ("Reportes", self.open_reports_menu)]

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

        # Botones de operaciones CRUD
        operations = [("Agregar Cliente", self.add_client),
                      ("Modificar Cliente", self.modify_client),
                      ("Eliminar Cliente", self.delete_client),
                      ("Mostrar Cliente", self.show_client),
                      ("Mostrar Lista Circular", self.show_graph)]

        for text, command in operations:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)

    def add_client(self):
        messagebox.showinfo("Clientes", "Agregar Cliente")

    def modify_client(self):
        messagebox.showinfo("Clientes", "Modificar Cliente")

    def delete_client(self):
        messagebox.showinfo("Clientes", "Eliminar Cliente")

    def show_client(self):
        messagebox.showinfo("Clientes", "Mostrar Cliente")

    def show_graph(self):
        dot_code = self.clients.generate_dot()
        with open("circular_list.dot", "w") as file:
        file.write(dot_code)
        import subprocess
        subprocess.run(["dot", "-Tpng", "circular_list.dot", "-o", "circular_list.png"])
        messagebox.showinfo("Mostrar Lista Circular", "Se ha generado el gráfico de la lista circular.")


class VehiclesMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestión de Vehículos")
        self.geometry("600x400")

        tk.Label(self, text="Gestión de Vehículos", font=("Arial", 14)).pack(pady=10)

        # Botones de operaciones CRUD
        operations = [("Agregar Vehículo", self.add_vehicle),
                      ("Modificar Vehículo", self.modify_vehicle),
                      ("Eliminar Vehículo", self.delete_vehicle),
                      ("Mostrar Vehículo", self.show_vehicle),
                      ("Mostrar Árbol B", self.show_graph)]

        for text, command in operations:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)

    def add_vehicle(self):
        messagebox.showinfo("Vehículos", "Agregar Vehículo")

    def modify_vehicle(self):
        messagebox.showinfo("Vehículos", "Modificar Vehículo")

    def delete_vehicle(self):
        messagebox.showinfo("Vehículos", "Eliminar Vehículo")

    def show_vehicle(self):
        messagebox.showinfo("Vehículos", "Mostrar Vehículo")

    def show_graph(self):
        messagebox.showinfo("Vehículos", "Mostrar Árbol B (Graphviz)")


class TripsMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestión de Viajes")
        self.geometry("600x400")

        tk.Label(self, text="Gestión de Viajes", font=("Arial", 14)).pack(pady=10)

        # Botones de operaciones
        operations = [("Crear Viaje", self.create_trip),
                      ("Mostrar Lista de Viajes", self.show_graph)]

        for text, command in operations:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)

    def create_trip(self):
        messagebox.showinfo("Viajes", "Crear Viaje")

    def show_graph(self):
        messagebox.showinfo("Viajes", "Mostrar Lista de Viajes (Graphviz)")


class ReportsMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Reportes")
        self.geometry("600x400")

        tk.Label(self, text="Reportes", font=("Arial", 14)).pack(pady=10)

        # Botones de reportes
        reports = [("Top Viajes", self.top_trips),
                   ("Top Ganancia", self.top_revenue),
                   ("Top Clientes", self.top_clients),
                   ("Top Vehículos", self.top_vehicles),
                   ("Ruta de un Viaje", self.route_of_trip)]

        for text, command in reports:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)

    def top_trips(self):
        messagebox.showinfo("Reportes", "Top Viajes")

    def top_revenue(self):
        messagebox.showinfo("Reportes", "Top Ganancia")

    def top_clients(self):
        messagebox.showinfo("Reportes", "Top Clientes")

    def top_vehicles(self):
        messagebox.showinfo("Reportes", "Top Vehículos")

    def route_of_trip(self):
        messagebox.showinfo("Reportes", "Ruta de un Viaje")


if __name__ == "__main__":
    app = LlegaRapiditoApp()
    app.mainloop()

class ClientsMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestión de Clientes")
        self.geometry("600x400")

        tk.Label(self, text="Gestión de Clientes", font=("Arial", 14)).pack(pady=10)

        # Estructura de datos para clientes (Lista circular)
        self.clients = CircularList()

        # Botones de operaciones CRUD
        operations = [("Agregar Cliente", self.add_client),
                      ("Mostrar Cliente", self.show_client)]

        for text, command in operations:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)

    def add_client(self):
        # Ventana de entrada para agregar cliente
        def save_client():
            name = name_entry.get()
            email = email_entry.get()
            if name and email:
                self.clients.add(Client(name, email))
                messagebox.showinfo("Agregar Cliente", f"Cliente '{name}' agregado con éxito.")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")

        add_window = tk.Toplevel(self)
        add_window.title("Agregar Cliente")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Nombre:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(add_window)
        email_entry.pack(pady=5)

        tk.Button(add_window, text="Guardar", command=save_client).pack(pady=10)

    def show_client(self):
        # Ventana de entrada para buscar cliente
        def search_client():
            name = name_entry.get()
            client = self.clients.find(name)
            if client:
                messagebox.showinfo("Mostrar Cliente", f"Cliente encontrado:\n\nNombre: {client.name}\nEmail: {client.email}")
            else:
                messagebox.showerror("Error", f"No se encontró al cliente '{name}'.")

        search_window = tk.Toplevel(self)
        search_window.title("Mostrar Cliente")
        search_window.geometry("300x150")

        tk.Label(search_window, text="Nombre del Cliente:").pack(pady=5)
        name_entry = tk.Entry(search_window)
        name_entry.pack(pady=5)

        tk.Button(search_window, text="Buscar", command=search_client).pack(pady=10)


class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class CircularList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def add(self, client):
        new_node = self.Node(client)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def find(self, name):
        if not self.head:
            return None
        temp = self.head
        while True:
            if temp.data.name == name:
                return temp.data
            temp = temp.next
            if temp == self.head:
                break
        return None

class VehiclesMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestión de Vehículos")
        self.geometry("600x400")

        tk.Label(self, text="Gestión de Vehículos", font=("Arial", 14)).pack(pady=10)

        # Estructura de datos para vehículos (Árbol B)
        self.vehicles = BTree(order=5)

        # Botones de operaciones CRUD
        operations = [("Agregar Vehículo", self.add_vehicle),
                      ("Mostrar Vehículo", self.show_vehicle)]

        for text, command in operations:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)

    def add_vehicle(self):
        def save_vehicle():
            plate = plate_entry.get()
            brand = brand_entry.get()
            model = model_entry.get()
            price = price_entry.get()

            if plate and brand and model and price:
                self.vehicles.insert(Vehicle(plate, brand, model, float(price)))
                messagebox.showinfo("Agregar Vehículo", f"Vehículo con placa '{plate}' agregado con éxito.")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")

        add_window = tk.Toplevel(self)
        add_window.title("Agregar Vehículo")
        add_window.geometry("300x250")

        tk.Label(add_window, text="Placa:").pack(pady=5)
        plate_entry = tk.Entry(add_window)
        plate_entry.pack(pady=5)

        tk.Label(add_window, text="Marca:").pack(pady=5)
        brand_entry = tk.Entry(add_window)
        brand_entry.pack(pady=5)

        tk.Label(add_window, text="Modelo:").pack(pady=5)
        model_entry = tk.Entry(add_window)
        model_entry.pack(pady=5)

        tk.Label(add_window, text="Precio por Segundo (Q):").pack(pady=5)
        price_entry = tk.Entry(add_window)
        price_entry.pack(pady=5)

        tk.Button(add_window, text="Guardar", command=save_vehicle).pack(pady=10)

    def show_vehicle(self):
        def search_vehicle():
            plate = plate_entry.get()
            vehicle = self.vehicles.search(plate)
            if vehicle:
                messagebox.showinfo("Mostrar Vehículo", f"Vehículo encontrado:\n\nPlaca: {vehicle.plate}\nMarca: {vehicle.brand}\nModelo: {vehicle.model}\nPrecio: Q{vehicle.price}")
            else:
                messagebox.showerror("Error", f"No se encontró el vehículo con placa '{plate}'.")

        search_window = tk.Toplevel(self)
        search_window.title("Mostrar Vehículo")
        search_window.geometry("300x150")

        tk.Label(search_window, text="Placa del Vehículo:").pack(pady=5)
        plate_entry = tk.Entry(search_window)
        plate_entry.pack(pady=5)

        tk.Button(search_window, text="Buscar", command=search_vehicle).pack(pady=10)


class Vehicle:
    def __init__(self, plate, brand, model, price):
        self.plate = plate
        self.brand = brand
        self.model = model
        self.price = price


class BTree:
    class Node:
        def __init__(self):
            self.keys = []
            self.children = []
            self.is_leaf = True

    def __init__(self, order):
        self.root = self.Node()
        self.order = order

    def insert(self, vehicle):
        # Lógica para insertar en un árbol B
        pass

    def search(self, plate):
        # Lógica para buscar en un árbol B
        pass


class RoutesMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestión de Rutas")
        self.geometry("600x400")

        tk.Label(self, text="Gestión de Rutas", font=("Arial", 14)).pack(pady=10)

        # Grafo de rutas (Lista de adyacencia)
        self.routes = Graph()

        tk.Button(self, text="Cargar Rutas", width=25, command=self.load_routes).pack(pady=5)
        tk.Button(self, text="Mostrar Grafo", width=25, command=self.show_graph).pack(pady=5)

    def load_routes(self):
        file_path = filedialog.askopenfilename(title="Seleccionar archivo de rutas")
        if file_path:
            self.routes.load_from_file(file_path)
            messagebox.showinfo("Cargar Rutas", "Rutas cargadas con éxito.")

    def show_graph(self):
        self.routes.visualize()

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, origin, destination, time):
        if origin not in self.adjacency_list:
            self.adjacency_list[origin] = []
        self.adjacency_list[origin].append((destination, time))

    def load_from_file(self, file_path):
        with open(file_path, "r") as file:
            for line in file.readlines():
                parts = line.strip().split(" / ")
                if len(parts) == 3:
                    origin, destination, time = parts
                    self.add_edge(origin, destination, int(time))

    def visualize(self):
        # Generar el gráfico con Graphviz
        pass


class TripsMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestión de Viajes")
        self.geometry("600x400")

        tk.Label(self, text="Gestión de Viajes", font=("Arial", 14)).pack(pady=10)

        # Lista simple de viajes
        self.trips = LinkedList()

        tk.Button(self, text="Crear Viaje", width=25, command=self.create_trip).pack(pady=5)
        tk.Button(self, text="Mostrar Viajes", width=25, command=self.show_trips).pack(pady=5)

    def create_trip(self):
        # Implementar creación de viajes
        pass

    def show_trips(self):
        # Implementar visualización de viajes
        pass

class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def add(self, trip):
        new_node = self.Node(trip)
        if not self.head:
            self.head = new_node
        else: 
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
