#Algoritmo que segun la cantidad de dinero a pagar aplica un descuento para el cliente
cantArt = int(input("¿Cuantos articulos desea comprar?: "))
if cantArt < 1:
     print("¡ERROR, no puede comprar", cantArt, "articulos!")
else:
    lista = []
    for i in range(cantArt * 2):
        nomArt = input(f"Nombre del Articulo {i + 1}: ")
        lista += [nomArt]
        precArt = float(input(f"Precio del Articulo {i + 1}: "))
        lista += [precArt]
        print(f"La lista creada es: {lista}")