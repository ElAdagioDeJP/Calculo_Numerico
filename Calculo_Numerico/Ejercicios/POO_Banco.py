class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    def ingresar(self, monto):
        self.cantidad += monto
        print(f"Se ha ingresado {self.cantidad} a la cuenta")
    
    def retirar(self, monto):
        self.cantidad -= monto
        print(f"Se ha retirado {self.cantidad} a la cuenta")
    
    def mostrar_estatus(self):
        print(f"Titular: {self.titular} Estado: {self.cantidad}")

finalizar = ""
nombre = input("Ingrese nombre del titular:")
dinero = int(input("Cuanto dinero tiene en la cuenta: "))

cuentita = Cuenta(nombre, dinero)

while finalizar != "n":
    finalizar = input("Quiere seguir utilizando el programa (s/n)")
    if finalizar == "s":
        accion = input("Quiere retirar (r) o Quiere hacer un deposito (d)")
        if accion == "r":
            transaccion = float(input("Cuanto quiere retirar?:"))
            cuentita.retirar(transaccion)
            cuentita.mostrar_estatus()
        elif accion == "d":
            transaccion = float(input("Cuanto quiere ingresar?:"))
            cuentita.ingresar(transaccion)
            cuentita.mostrar_estatus()
        else:
            print("No lo entendi, disculpe")
    else:
        print("Error")
"""
Crear una clase llamado cuenta; atributos, persona, cantidad
metodos
un constructor(datos vacios)
los seters y los geters para cada uno de los atributos (el atributos no se puedes modificar directamente
solo ingresando y retirando dinero)
Mostrar los datos de la cuenta
Si ingresa una cantidad a la cuenta si es negativa no se hace nada
Se retira una cantidad de mas puede quedar negativas
"""
"UwU"
