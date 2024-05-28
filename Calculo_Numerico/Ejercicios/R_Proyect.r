x <- 18
y <- 2
x + y
print (x - y)
print('*********************************************')
print('**********Bienvenidos al enlistador**********')
print('*********************************************')

print()
print("Bienvenidos al programa de listas de compras")

lista_de_compras <- c()

productos <- readline(prompt="Ingrese un producto: ")

while (productos != "exit") {
    lista_de_compras <- c(lista_de_compras, productos)
    print()
    productos <- readline(prompt="Ingrese un producto (exit): ")
}

print("Tu lista de compras es:")
print(lista_de_compras)




