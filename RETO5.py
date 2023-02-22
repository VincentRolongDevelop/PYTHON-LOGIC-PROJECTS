
class Tienda:
    arregloProductos = {"código": [1,2,3,4,5,6,7,8,9,10], \
        "nombre": ["Manzanas","Limones", "Peras", "Arandanos", "Tomates", "Fresas", "Helado", "Galletas", "Chocolates", "Jamon"], \
            "precio":[5000.0, 2300.0, 2700.0, 9300.0, 2100.0, 4100.0, 4500.0, 500.0, 3500.0, 15000.0], \
                "inventario": [25, 15, 33, 5, 42, 3, 41, 8, 80, 10]}
    
    def ElprecioEsMayor(self,):
        mayor = 0
        for i in range(0, len(self.arregloProductos["precio"])):
            if mayor < self.arregloProductos["precio"][i]:
                mayor = self.arregloProductos["precio"][i]
        
        indice = self.arregloProductos["precio"].index(mayor)

        return self.arregloProductos["nombre"][indice]
    
    def ElprecioEsMenor(self,):
        menor = self.arregloProductos["precio"][0]
        for i in range(0, len(self.arregloProductos["precio"])):
            if menor > self.arregloProductos["precio"][i]:
                menor = self.arregloProductos["precio"][i]
        indice = self.arregloProductos["precio"].index(menor)
        return self.arregloProductos["nombre"][indice]

    def ElprecioPromedio(self,):
        suma = 0
        for i in range(0, len(self.arregloProductos["precio"])):
            suma += self.arregloProductos["precio"][i]
        promedio = suma/len(self.arregloProductos["precio"])
        return round(promedio,1)

    def Inventario(self,):
        suma = 0
        for i in range(0, len(self.arregloProductos["precio"])):
            suma += self.arregloProductos["precio"][i]*self.arregloProductos["inventario"][i]
        return suma
    
    def AGREGAR(self,codigo, nombre, precio, inventario):
        if not codigo in self.arregloProductos["código"]:
            self.arregloProductos["código"].append(codigo)
            self.arregloProductos["nombre"].append(nombre)
            self.arregloProductos["precio"].append(precio)
            self.arregloProductos["inventario"].append(inventario)
            print(self.ElprecioEsMayor(), self.ElprecioEsMenor(), self.ElprecioPromedio(), self.Inventario())
        else:
            print("ERROR")
    
    def BORRAR(self, codigo):
        if codigo in self.arregloProductos["código"]:
            indice = self.arregloProductos["código"].index(codigo)
            del self.arregloProductos["código"][indice]
            del self.arregloProductos["nombre"][indice]
            del self.arregloProductos["precio"][indice]
            del self.arregloProductos["inventario"][indice]
            print(self.ElprecioEsMayor(), self.ElprecioEsMenor(), self.ElprecioPromedio(), self.Inventario())
        else:
            print("ERROR")

    def ACTUALIZAR(self, codigo, nombre, precio, inventario):
        if codigo in self.arregloProductos["código"]:
            if nombre in self.arregloProductos["nombre"]:
                indice = self.arregloProductos["código"].index(codigo)
                self.arregloProductos["nombre"][indice] = nombre
                self.arregloProductos["precio"][indice] = precio
                self.arregloProductos["inventario"][indice] = inventario
                print(self.ElprecioEsMayor(), self.ElprecioEsMenor(), self.ElprecioPromedio(), self.Inventario())
            else:
                print("ERROR")
        else:
            print("ERROR")

    def toString(self):
        print("\n")
        for i in range(0, len(self.arregloProductos["código"])):
            print(self.arregloProductos["código"][i],self.arregloProductos["nombre"][i]\
                ,self.arregloProductos["precio"][i]\
                    ,self.arregloProductos["inventario"][i])

tienda = Tienda()

operacion = input()
codigo, nombre, precio, arregloProductos = input().split()
codigo = int(codigo)
precio = float(precio)
arregloProductos = int(arregloProductos)

if operacion.upper() == "AGREGAR":
    tienda.AGREGAR(codigo, nombre, precio, arregloProductos)
elif operacion.upper() == "BORRAR":
    tienda.BORRAR(codigo)
elif operacion.upper() == "ACTUALIZAR":
    tienda.ACTUALIZAR(codigo, nombre, precio, arregloProductos)