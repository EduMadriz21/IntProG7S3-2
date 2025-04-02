import math

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area_base = math.pi * (radio ** 2)
volumen = area_base * altura

area_lateral = 2 * math.pi * radio * altura
area_superficial = area_lateral + (2 * area_base)

print("Radio ingresado:", radio)
print("Altura ingresada:", altura)
print("Volumen calculado:", volumen)
print("Área superficial calculada:", area_superficial)