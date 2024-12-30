class Vehiculo:
    def __init__(self, placa, marca, modelo, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"Placa: {self.placa} | Marca: {self.marca} | Modelo: {self.modelo} | Precio: {self.precio}"
    
    def __repr__(self):
        return str(self)
    
    def placa_marca(self):
        return f"{self.placa} - {self.marca}"

class NodoArbolB5Vehiculo:
    def __init__(self, hoja=False):
        self.hoja = hoja
        self.placas = []
        self.hijos = []

class ArbolB5Vehiculo:
    def __init__(self, t):
        self.raiz = NodoArbolB5Vehiculo(True)
        self.t = t
    
    def insertar(self, k):
        raiz = self.raiz
        if len(raiz.placas) == (2 * self.t) - 1:
            temp = NodoArbolB5Vehiculo()
            self.raiz = temp
            temp.hijos.insert(0, raiz)
            self.dividir_hijo(temp, 0)
            self.insertar_no_lleno(temp, k)
        else:
            self.insertar_no_lleno(raiz, k)

    def insertar_no_lleno(self, x, k):
        i = len(x.placas) - 1
        if x.hoja:
            x.placas.append((None, None))
            while i >= 0 and k[0] < x.placas[i][0]:
                x.placas[i + 1] = x.placas[i]
                i -= 1
            x.placas[i + 1] = k
        else:
            while i >= 0 and k[0] < x.placas[i][0]:
                i -= 1
            i += 1
            if len(x.hijos[i].placas) == (2 * self.t) - 1:
                self.dividir_hijo(x, i)
                if k[0] > x.placas[i][0]:
                    i += 1
            self.insertar_no_lleno(x.hijos[i], k)

    def dividir_hijo(self, x, i):
        t = self.t
        y = x.hijos[i]
        z = NodoArbolB5Vehiculo(y.hoja)
        x.hijos.insert(i + 1, z)
        x.placas.insert(i, y.placas[t - 1])
        z.placas = y.placas[t: (2 * t) - 1]
        y.placas = y.placas[0: t - 1]
        if not y.hoja:
            z.hijos = y.hijos[t: 2 * t]
            y.hijos = y.hijos[0: t]
    
    def eliminar(self, x, k):
        t = self.t
        i = 0
        while i < len(x.placas) and k[0] > x.placas[i][0]:
            i += 1
        if x.hoja:
            if i < len(x.placas) and x.placas[i][0] == k[0]:
                x.placas.pop(i)
                return
            return
        if i < len(x.placas) and x.placas[i][0] == k[0]:
            return self.eliminar_nodo_interno(x, k, i)
        elif len(x.hijos[i].placas) >= t:
            self.eliminar(x.hijos[i], k)
        else:
            if i != 0 and i + 2 < len(x.placas):
                if len(x.hijos[i - 1].placas) >= t:
                    self.eliminar_hermano(x, i, i - 1)
                elif len(x.hijos[i + 1].placas) >= t:
                    self.eliminar_hermano(x, i, i + 1)
                else:
                    self.eliminar_combinar(x, i, i + 1)
            elif i == 0:
                if len(x.hijos[i + 1].placas) >= t:
                    self.eliminar_hermano(x, i, i + 1)
                else:
                    self.eliminar_combinar(x, i, i + 1)
            elif i + 1 == len(x.hijos):
                if len(x.hijos[i - 1].placas) >= t:
                    self.eliminar_hermano(x, i, i - 1)
                else:
                    self.eliminar_combinar(x, i, i - 1)
            self.eliminar(x.hijos[i], k)
    
    def eliminar_nodo_interno(self, x, k, i):
        t = self.t
        if x.hoja:
            if x.placas[i][0] == k[0]:
                x.placas.pop(i)
                return
            return

        if len(x.hijos[i].placas) >= t:
            x.placas[i] = self.eliminar_predecesor(x.hijos[i])
            return
        elif len(x.hijos[i + 1].placas) >= t:
            x.placas[i] = self.eliminar_sucesor(x.hijos[i + 1])
            return
        else:
            self.eliminar_combinar(x, i, i + 1)
            self.eliminar_nodo_interno(x.hijos[i], k, self.t - 1)

    def eliminar_predecesor(self, x):
        if x.hoja:
            return x.placas.pop()
        n = len(x.placas) - 1
        if len(x.hijos[n].placas) >= self.t:
            self.eliminar_hermano(x, n + 1, n)
        else:
            self.eliminar_combinar(x, n, n + 1)
        return self.eliminar_predecesor(x.hijos[n])

    def eliminar_sucesor(self, x):
        if x.hoja:
            return x.placas.pop(0)
        if len(x.hijos[0].placas) >= self.t:
            self.eliminar_hermano(x, 0, 1)
        else:
            self.eliminar_combinar(x, 0, 1)
        return self.eliminar_sucesor(x.hijos[0])
    
    def eliminar_combinar(self, x, i, j):
        tmp = x.hijos[i]
        if j > i:
            rstmp = x.hijos[j]
            tmp.placas.append(x.placas[i])
            for k in range(len(rstmp.placas)):
                tmp.placas.append(rstmp.placas[k])
                if len(rstmp.hijos) > 0:
                    tmp.hijos.append(rstmp.hijos[k])
            if len(rstmp.hijos) > 0:
                tmp.hijos.append(rstmp.hijos.pop())
            nuevo = tmp
            x.placas.pop(i)
            x.hijos.pop(j)
        else:
            lstmp = x.hijos[j]
            lstmp.placas.append(x.placas[j])
            for k in range(len(tmp.placas)):
                lstmp.placas.append(tmp.placas[k])
                if len(lstmp.hijos) > 0:
                    lstmp.hijos.append(tmp.hijos[k])
            if len(lstmp.hijos) > 0:
                lstmp.hijos.append(tmp.hijos.pop())
            nuevo = lstmp
            x.placas.pop(j)
            x.hijos.pop(i)

        if x == self.raiz and len(x.placas) == 0:
            self.raiz = nuevo

    def eliminar_hermano(self, x, i, j):
        tmp = x.hijos[i]
        if i < j:
            rstmp = x.hijos[j]
            tmp.placas.append(x.placas[i])
            x.placas[i] = rstmp.placas[0]
            if len(rstmp.hijos) > 0:
                tmp.hijos.append(rstmp.hijos[0])
                rstmp.hijos.pop(0)
            rstmp.placas.pop(0)
        else:
            lstmp = x.hijos[j]
            tmp.placas.insert(0, x.placas[i - 1])
            x.placas[i - 1] = lstmp.placas.pop()
            if len(lstmp.hijos) > 0:
                tmp.hijos.insert(0, lstmp.hijos.pop())

    def mostrar(self, x, l=0):
        print(f"Nivel {l} {len(x.placas)}", end=": ")
        for i in x.placas:
            print(i, end=" ")
        print()
        l += 1
        if len(x.hijos) > 0:
            for i in x.hijos:
                self.mostrar(i, l)

    def generarDotString(self):
        dot = "digraph ArbolB5Vehiculo {\n"
        dot += "\trankdir=TB;\n"
        dot += "\tnode [shape=record];\n"
        dot += "\tlabel=\"Arbol B de Vehiculos\";\n"
        dot += self.generarDotStringNodo(self.raiz)
        dot += "}"
        return dot

    def listarVehiculos(self, x):
        vehiculos = []
        for i in x.placas:
            vehiculos.append(i)
        if len(x.hijos) > 0:
            for i in x.hijos:
                vehiculos += self.listarVehiculos(i)
        return vehiculos
    
    def generarDotStringNodo(self, x, l1=0, l2=0, pPadre=None):
        dot = ""
        nActual = f"n{l1}_{l2}"
        if pPadre is not None:
            dot += f"\t{pPadre} -> {nActual};\n"
        dot += f"\t{nActual} [label=\""
        placas = []
        for i in x.placas:
            placas.append(f"p{i[0]}")
            dot += f"<p{i[0]}>| {{ {i} }} |" if i[0] is not None else ""
        dot += "<pNULL>\"];\n"
        placas.append("pNULL")
        l1 += 1
        if len(x.hijos) > 0:
            c = 0
            for i in x.hijos:
                dot += self.generarDotStringNodo(i, l1, c, f"{nActual}:{placas[c]}")
                c += 1
        return dot
    
    def buscar(self, x, k):
        i = 0
        while i < len(x.placas) and k[0] > x.placas[i][0]:
            i += 1
        if i < len(x.placas) and k[0] == x.placas[i][0]:
            return x.placas[i]
        if x.hoja:
            return None
        return self.buscar(x.hijos[i], k)
    
    def modificar(self, x, k, marca, modelo, precio):
        i = 0
        while i < len(x.placas) and k[0] > x.placas[i][0]:
            i += 1
        if i < len(x.placas) and k[0] == x.placas[i][0]:
            x.placas[i] = (k[0], Vehiculo(k[0], marca, modelo, precio))
            return
        if x.hoja:
            return
        return self.modificar(x.hijos[i], k, marca, modelo, precio)
    
#B = ArbolB5Vehiculo(3)
#import random
#for i in range(10):
#    placaAleatoria = random.randint(1000, 9999)
#    vehiculo = Vehiculo(placaAleatoria, f"Marca {i}", f"Modelo {i}", random.randint(10000, 99999))
#    B.insertar((placaAleatoria, vehiculo))
#    B.mostrar(B.raiz)
#    print()

#print("Buscando...")
#print(B.buscar(B.raiz, (placaAleatoria,)))