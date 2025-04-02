
def convertir_temperatura(fahrenheit):
  
    celsius = (fahrenheit - 32) * 5 / 9

    kelvin = celsius + 273.15
    
    return celsius, kelvin

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

celsius, kelvin = convertir_temperatura(fahrenheit)
print(f"La temperatura en Celsius es: {celsius:.2f}°C")
print(f"La temperatura en Kelvin es: {kelvin:.2f} K")