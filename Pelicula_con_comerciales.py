duracion_pelicula = float(input("Ingrese la duración de la película en minutos: "))
duracion_comerciales_previos = float(input("Ingrese la duración de los comerciales previos en minutos: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
duracion_pausa = float(input("Ingrese la duración de cada pausa comercial en minutos: "))

total_comerciales = cantidad_pausas * duracion_pausa

duracion_total = duracion_pelicula + duracion_comerciales_previos + total_comerciales

print("Duración original de la película:", duracion_pelicula)
print("Duración de los comerciales totales:", duracion_comerciales_previos + total_comerciales)
print("Tiempo total de la proyección:", duracion_total)