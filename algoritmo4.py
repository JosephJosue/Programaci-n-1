#Algoritmo que hace funcion de carrito de compras el cual indica la cantidad a pagar
def ImprimirArticulo(nomArt, precArt):
    print("Producto: ", nomArt, "\nPrecio: ", precArt)
lista = []
nomArt = input("Nombre del Articulo: ")
lista.append(nomArt)
precArt = float(input("Precio del Articulo: "))
total = precArt
ImprimirArticulo(nomArt, precArt)
decision = True
while decision:
    resp = input("¿Desea agregar mas articulos a su carrito? (Si - No)\n==>")
    if resp == "Si":
        nomArt = input("Nombre del Articulo: ")
        lista.append(nomArt)
        precArt = float(input("Precio del Articulo: "))
        ImprimirArticulo(nomArt, precArt)
        total += precArt
    else:
        decision = False
print("Su carrito de compras tiene los siguientes articulos:\n==>", lista)
print("Su total de compras es de:\n==>", total)
