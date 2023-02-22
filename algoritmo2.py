#Algoritmo que mide el promedio de satisfaccion del cliente e indica si el cliente es detractor, neutro o promotor de el servicio
print("Del 1 al 10, 1 siendo el menor y 10 siendo el mayor califique nuestro servicio.")
score1 = int(input("¿Cuál es su grado de satisfacción con la relación calidad-precio del producto?\n"))
score2 = int(input("Este [producto/servicio] me ayuda a cumplir mis objetivos.\n"))
score3 = int(input("¿Encontro la pagina amigable con usted y se le hizo facil realizar su compra?\n"))
quest1 = (int(input("¿Pidio ayuda de nuestro servicio al cliente en linea?\nEscriba \"1\" para Si o \"2\" para No.\n")))
if quest1 == 1:
    score4 = (int(input("¿Que le parecio la atencion al cliente del 1 al 10?\n")))
else:
    if quest1 == 2:
        score4 = 10
    else :
        print("RESPUESTA INVALIDA")
score5 = int(input("¿Recomendaria nuestro servicio a otra persona?\n"))
promScor = (score1 + score2 + score3 + score4 +score5)/5
if 1<=promScor<=5:
    print("/////////////////////////////////////")
    print("El cliente es detractor del servicio.")
    print("/////////////////////////////////////")
else:
    if 6<=promScor<=8:
        print("////////////////////////////////////////")
        print("El cliente se siente neutro al servicio.")
        print("////////////////////////////////////////")
    else:
        if 9<=promScor<=10:
            print("/////////////////////////////////////////////")
            print("El cliente es promotor de nuestros servicios.")
            print("/////////////////////////////////////////////")