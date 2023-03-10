#algoritmo que segun el total de compra ofrece un descuento
total = float(input("Ingrese su monto total de compra\n==>"))
if total >= 100:
    desc = total - (100*0.10)
    print("¡FELICITACIONES! Su total de compras aplica para un descuento del 10%")
    print ("Su monto total menos el descuento es de", desc, "$")
elif 101 <= total <= 249:
    desc = total - (100*0.15)
    print("¡FELICITACIONES! Su total de compras aplica para un descuento del 15%")
    print ("Su monto total menos el descuento es de", desc, "$")
elif total >= 250:
    desc = total - (100*0.25)
    print("¡FELICITACIONES! Su total de compras aplica para un descuento del 25%")
    print ("Su monto total menos el descuento es de", desc, "$")
else:
    faltante = 100 - total
    print("lamentablemente su compra no aplica para un descuento, agregue", faltante, "$ a su carrito para aplicar a un descuento.")