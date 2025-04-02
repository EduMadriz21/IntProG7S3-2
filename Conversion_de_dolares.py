cantidad_dolares = float(input("Ingrese la cantidad en dólares: "))

tasa_euros = 0.85  # Ejemplo
tasa_libras = 0.75  # Ejemplo
tasa_yenes = 110.0  # Ejemplo

cantidad_euros = cantidad_dolares * tasa_euros
cantidad_libras = cantidad_dolares * tasa_libras
cantidad_yenes = cantidad_dolares * tasa_yenes

print("Cantidad en dólares:", cantidad_dolares)
print("Cantidad en euros:", cantidad_euros)
print("Cantidad en libras:", cantidad_libras)
print("Cantidad en yenes:", cantidad_yenes)