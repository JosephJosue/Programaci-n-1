#algoritmo que recopila informacion de un cliente frecuente e indica su status segun la cantidad de puntos acumulados.
name = input("Escriba su primer nombre: ")
apell = input("Escriba su apellido: ")
age = int(input("Escriba su edad: "))
point = int(input("Escriba la cantidad de puntos que ha acumulado: "))
if 0<=point<=4999:
    stat = "MEMBER"
elif 5000<=point<=9999:
    stat = "SILVER"
elif 10000<=point<=14999:
    stat = "GOLD"
elif point>15000:
    stat = "PLATINUM"
addrs = input("Escriba su direccion:")
clnt = {
    'Nombre':name,
    'Apellido':apell,
    'Edad':age,
    'Puntos acumulados':point,
    'Status':stat,
    'Direccion':addrs
}
choic = int(input("¿Desea desplegar información del cliente?\nEscriba \"1\" para Si o \"2\" para No.\n"))
if choic == 1:
    print('/////////////////////////////////////////////////////')
    print("Nombre de cliente:", clnt["Nombre"], clnt["Apellido"])
    print("Edad:", clnt["Edad"])
    print("Puntos Acumulados:", clnt["Puntos acumulados"])
    print("Dirección:", clnt["Direccion"])
    print("Status:", clnt["Status"])
    print('/////////////////////////////////////////////////////')
else:
    if choic == 2:
        print("///////////////")
        print("¡VUELVA PRONTO!")
        print("///////////////")
    else :
        print("////////////////////////")
        print("ELIJA UNA OPCIÓN VALIDA.")
        print("////////////////////////")