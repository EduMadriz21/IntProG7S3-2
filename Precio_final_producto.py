precio_original = float(input("Ingrese el precio original del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

descuento = (precio_original * porcentaje_descuento) / 100
precio_con_descuento = precio_original - descuento

porcentaje_iva = float(input("Ingrese el porcentaje de IVA: "))
iva_calculado = (precio_con_descuento * porcentaje_iva) / 100
precio_final = precio_con_descuento + iva_calculado

print("Precio original:", precio_original)
print("Descuento aplicado:", descuento)
print("Precio con descuento:", precio_con_descuento)
print("IVA calculado:", iva_calculado)
print("Precio final:", precio_final)