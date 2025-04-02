total_segundos = int(input("Ingrese la cantidad total de segundos: "))

horas = total_segundos // 3600
segundos_restantes = total_segundos % 3600

minutos = segundos_restantes // 60
segundos_finales = segundos_restantes % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_finales)