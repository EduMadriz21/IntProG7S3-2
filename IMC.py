peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

imc = peso / (altura ** 2)

imc = round(imc, 2)

print("Peso ingresado:", peso)
print("Altura ingresada:", altura)
print("IMC calculado:", imc)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 24.9:
    clasificacion = "Peso normal"
elif 25 <= imc < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print("Clasificación del IMC:", clasificacion)