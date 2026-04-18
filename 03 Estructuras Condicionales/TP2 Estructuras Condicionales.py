#Actividad 1 
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Es mayor de edad")
#Actividad 2 
nota = float(input("Introduce tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
#Actividad 3
numero = int(input("Ingresa un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
#Actividad 4
edad = int(input("Introduce tu edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
#Actividad 5
password = input("Introduce una contraseña (entre 8 y 14 caracteres): ")
longitud = len(password)

if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#Actividad 6
consumo = float(input("Ingrese el consumo mensual de energía (kWh): "))

if consumo < 150:
    categoria = "Consumo bajo"
elif 150 <= consumo <= 300:
    categoria = "Consumo medio"
else:
    categoria = "Consumo alto"

print(f"Categoría: {categoria}")

if consumo > 500:
    print("Considere medidas de ahorro energético")
#Actividad 7
frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouáéíóú"

if frase[-1].lower() in vocales:
    frase += "!"

print(frase)
#Actividad 8
nombre = input("Ingrese su nombre: ")
print("Opciones: 1 (MAYÚSCULAS), 2 (minúsculas), 3 (Primera Mayúscula)")
opcion = input("Seleccione una opción (1, 2 o 3): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")
#Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    resultado = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    resultado = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    resultado = "Moderado (sentido por personas, pero generalmente sin daños)"
elif 5 <= magnitud < 6:
    resultado = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    resultado = "Muy Fuerte (puede causar daños significativos)"
else:
    resultado = "Extremo (puede causar graves daños a gran escala)"

print(f"Resultado: {resultado}")