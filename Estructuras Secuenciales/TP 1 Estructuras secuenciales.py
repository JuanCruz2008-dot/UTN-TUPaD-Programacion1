#Actividad 1
print("¡Hola Mundo!")

#Actividad 2
nombre = input("Por favor, ingrese su nombre: ")

print(f"¡Hola {nombre}!")

#Actividad 3
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_de_residencia = input("Por favor, ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")
 
 #Actividad 4
import math

radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))

area_circulo = math.pi * (radio_circulo)**2
perimetro_circulo = 2 * math.pi * radio_circulo

print(f"El area del circulo es de {area_circulo} y el perimetro es de {perimetro_circulo}")

#Actividad 5
cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))
cantidad_horas = round(cantidad_segundos / 3600, 2)

print(f"El equivalente a {cantidad_segundos} segundos son {cantidad_horas} horas")

#Actividad 6

numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))

numero_por_0 = numero_a_multiplicar * 0
numero_por_1 = numero_a_multiplicar * 1
numero_por_2 = numero_a_multiplicar * 2
numero_por_3 = numero_a_multiplicar * 3
numero_por_4 = numero_a_multiplicar * 4
numero_por_5 = numero_a_multiplicar * 5
numero_por_6 = numero_a_multiplicar * 6
numero_por_7 = numero_a_multiplicar * 7
numero_por_8 = numero_a_multiplicar * 8
numero_por_9 = numero_a_multiplicar * 9

print(f"""
  {numero_a_multiplicar} x 0 = {numero_por_0}
  {numero_a_multiplicar} x 1 = {numero_por_1}
  {numero_a_multiplicar} x 2 = {numero_por_2}
  {numero_a_multiplicar} x 3 = {numero_por_3}
  {numero_a_multiplicar} x 4 = {numero_por_4}
  {numero_a_multiplicar} x 5 = {numero_por_5}
  {numero_a_multiplicar} x 6 = {numero_por_6}
  {numero_a_multiplicar} x 7 = {numero_por_7}
  {numero_a_multiplicar} x 8 = {numero_por_8}
  {numero_a_multiplicar} x 9 = {numero_por_9}
      """)