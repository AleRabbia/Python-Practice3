#Clase
#Constructores
#Variables de instancia
#Variables de clase
#Metodo de instancia
#Metodos de clase
#Properties

class Automovil:

    __iva=0.21 #variable de clase
    def __init__(self, marca, modelo, precio, nacionalidad="SinRegistrar") -> None: #constructor
        self.marca=marca #variable de instancia
        self.modelo=modelo
        self.precio=precio
        self.nacionalidad=nacionalidad

    def mostrar(self): #metodo de instancia
        print(self.marca)
        print(self.modelo)
        print(self.precio)
        print(self.nacionalidad)

    @classmethod
    def cambiar_iva(cls, iva_nuevo): #metodo de clase
        __iva= iva_nuevo 
        print(__iva)  

    @classmethod
    def mostrar_iva(cls):
        print(cls.__iva)    

    @property
    def precio_con_iva(self):
        precio_final = self.precio + (self.precio * self.__iva)
        return precio_final
        print(precio_final)    



Automovil_fiat = Automovil("Fiat", "palio", 1000, "Argentina")
print("Automovil Fiat")
Automovil_fiat.mostrar()
Automovil_peugeot = Automovil("Peugeot", "207", 1000)
print("Automovil Peugeot")
Automovil_peugeot.mostrar()
Automovil.cambiar_iva(0.25)
print(Automovil_fiat.precio)
print(Automovil_fiat.precio_con_iva)


