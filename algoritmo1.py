#Algoritmo que almacena una lista de objetos indefinidos hasta que el usuario lo decida.
list = []
decis = ""
opcion = int(input("Bienvenido a su lista de compras, ¿Que desea hacer?\n1. Agregar objetos a la lista de compras.\n2. Salir\n"))
match opcion:
    case 1:
        objeto = input("¿Que objeto desea agregar a su lista?\n")
        list.append(objeto)
        decis = input("¿Desea agregar otro objeto a la lista?\nEscribe \"Y\" para Si o \"N\" para No y ver su lista.\n")
        while  decis == "Y":
            objeto = input("¿Que objeto desea agregar a su lista?\n")
            list.append(objeto)
            decis = input("¿Desea agregar otro objeto a la lista?\nEscribe \"Y\" para Si o \"N\" para No y ver su lista.\n")
        else:
            if decis == "N":
                print(f"Su lista de compras contiene los siguientes objetos: {list}")
    case 2:
        print("¡Vuelva pronto!")
