#Actividad 1 Caja del kiosco
# 1. Pedir nombre del cliente
nombre = input("Ingrese nombre del cliente: ")
while not nombre.isalpha() or nombre == "":
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Ingrese nombre del cliente: ")

# 2. Pedir cantidad de productos
cant_prod_str = input("Cantidad de productos a comprar: ")
while not cant_prod_str.isdigit() or int(cant_prod_str) <= 0:
    print("Error: Ingrese un número entero positivo.")
    cant_prod_str = input("Cantidad de productos a comprar: ")

cantidad_productos = int(cant_prod_str)

total_sin_desc = 0
total_con_desc = 0

# 3. Ciclo por cada producto
for i in range(1, cantidad_productos + 1):
    # Pedir precio
    precio_str = input(f"Producto {i} - Precio: ")
    while not precio_str.isdigit():
        print("Error: Ingrese un precio válido (entero).")
        precio_str = input(f"Producto {i} - Precio: ")
    
    precio = int(precio_str)
    total_sin_desc += precio

    # Pedir descuento
    tiene_desc = input("¿Tiene descuento? (S/N): ").lower()
    while tiene_desc != 's' and tiene_desc != 'n':
        print("Error: Ingrese 's' para sí o 'n' para no.")
        tiene_desc = input("¿Tiene descuento? (S/N): ").lower()

    if tiene_desc == 's':
        precio_final = precio * 0.90
    else:
        precio_final = precio
    
    total_con_desc += precio_final

# 4. Mostrar resultados
ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad_productos

print("-" * 20)
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#Actividad 2 Acceso al Campus y Menú Seguro 
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

# Login (Máximo 3 intentos)
while intentos < 3 and not acceso:
    intentos += 1
    user = input(f"Intento {intentos}/3 - Usuario: ")
    passw = input("Clave: ")

    if user == usuario_correcto and passw == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada.")
else:
    # Menú repetitivo
    opcion = ""
    while opcion != "4":
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        
        if opcion == "1":
            print("Estado: Inscripto")
        elif opcion == "2":
            nueva_clave = input("Nueva clave (mín. 6 caracteres): ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave (mín. 6 caracteres): ")
            
            confirmacion = input("Confirme nueva clave: ")
            if nueva_clave == confirmacion:
                clave_correcta = nueva_clave
                print("Clave cambiada con éxito.")
            else:
                print("Error: las claves no coinciden.")
        elif opcion == "3":
            print("Frase del día: 'El éxito es la suma de pequeños esfuerzos repetidos día tras día'.")
        elif opcion == "4":
            print("Saliendo del sistema...")
        else:
            print("Error: opción fuera de rango.")

#Actividad 3 Agenda de Turnos (Sin Listas)
# Inicialización de variables (espacios libres)
l1 = ""; l2 = ""; l3 = ""; l4 = "" # Lunes (4 turnos)
m1 = ""; m2 = ""; m3 = ""         # Martes (3 turnos)

operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: Solo letras.")
    operador = input("Nombre del operador: ")

opcion = ""
while opcion != "5":
    print(f"\n--- Agenda (Operador: {operador}) ---")
    print("1. Reservar turno\n2. Cancelar turno\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema")
    opcion = input("Opción: ")

    if opcion == "1": # Reservar
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        if dia == "1" or dia == "2":
            paciente = input("Nombre del paciente: ")
            while not paciente.isalpha():
                paciente = input("Error (solo letras). Nombre: ")
            
            # Validar si ya existe y buscar lugar libre
            if dia == "1":
                if paciente in (l1, l2, l3, l4):
                    print("Error: El paciente ya tiene turno este día.")
                elif l1 == "": l1 = paciente; print("Turno 1 asignado.")
                elif l2 == "": l2 = paciente; print("Turno 2 asignado.")
                elif l3 == "": l3 = paciente; print("Turno 3 asignado.")
                elif l4 == "": l4 = paciente; print("Turno 4 asignado.")
                else: print("Día completo.")
            else:
                if paciente in (m1, m2, m3):
                    print("Error: El paciente ya tiene turno este día.")
                elif m1 == "": m1 = paciente; print("Turno 1 asignado.")
                elif m2 == "": m2 = paciente; print("Turno 2 asignado.")
                elif m3 == "": m3 = paciente; print("Turno 3 asignado.")
                else: print("Día completo.")

    elif opcion == "2": # Cancelar
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        paciente = input("Nombre del paciente a cancelar: ")
        if dia == "1":
            if l1 == paciente: l1 = ""; print("Cancelado.")
            elif l2 == paciente: l2 = ""; print("Cancelado.")
            elif l3 == paciente: l3 = ""; print("Cancelado.")
            elif l4 == paciente: l4 = ""; print("Cancelado.")
            else: print("No se encontró el paciente.")
        elif dia == "2":
            if m1 == paciente: m1 = ""; print("Cancelado.")
            elif m2 == paciente: m2 = ""; print("Cancelado.")
            elif m3 == paciente: m3 = ""; print("Cancelado.")
            else: print("No se encontró el paciente.")

    elif opcion == "3": # Ver agenda
        dia = input("Ver día (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"1: {l1 if l1!='' else '(libre)'}\n2: {l2 if l2!='' else '(libre)'}\n3: {l3 if l3!='' else '(libre)'}\n4: {l4 if l4!='' else '(libre)'}")
        elif dia == "2":
            print(f"1: {m1 if m1!='' else '(libre)'}\n2: {m2 if m2!='' else '(libre)'}\n3: {m3 if m3!='' else '(libre)'}")

    elif opcion == "4": # Resumen
        occ_l = (1 if l1!="" else 0) + (1 if l2!="" else 0) + (1 if l3!="" else 0) + (1 if l4!="" else 0)
        occ_m = (1 if m1!="" else 0) + (1 if m2!="" else 0) + (1 if m3!="" else 0)
        print(f"Lunes: {occ_l} ocupados, {4-occ_l} libres.")
        print(f"Martes: {occ_m} ocupados, {3-occ_m} libres.")
        if occ_l > occ_m: print("El día con más turnos es Lunes.")
        elif occ_m > occ_l: print("El día con más turnos es Martes.")
        else: print("Empate en cantidad de turnos.")

#Actividad 4 Escape Room - La Bóveda
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0

nombre_agente = input("Nombre del agente: ")
while not nombre_agente.isalpha():
    nombre_agente = input("Error. Ingrese nombre (solo letras): ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\n--- Agente: {nombre_agente} | Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 ---")
    if alarma: print("¡ALERTA: ALARMA ACTIVADA!")
    
    print("1. Forzar cerradura (-20E, -2T)\n2. Hackear panel (-10E, -3T)\n3. Descansar (+15E, -1T)")
    opcion = input("Acción: ")
    
    if not opcion.isdigit():
        print("Opción inválida."); continue

    if opcion == "1":
        forzar_seguidos += 1
        energia -= 20
        tiempo -= 2
        
        if forzar_seguidos >= 3:
            alarma = True
            print("¡La cerradura se trabó! Alarma activada.")
        else:
            riesgo = False
            if energia < 40:
                print("¡Riesgo de alarma!")
                n = input("Elija número 1-3: ")
                if n == "3": alarma = True; riesgo = True
            
            if not alarma and not riesgo:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")
                
    elif opcion == "2":
        forzar_seguidos = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completo! Cerradura abierta automáticamente.")

    elif opcion == "3":
        forzar_seguidos = 0
        energia += 15
        if energia > 100: energia = 100
        tiempo -= 1
        if alarma: 
            energia -= 10
            print("El estrés de la alarma te quita energía extra.")
    else:
        print("Opción no válida.")

# Final del juego
if cerraduras_abiertas == 3:
    print("¡VICTORIA! Bóveda abierta.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se bloqueó por la alarma.")
else:
    print("DERROTA: Te quedaste sin recursos.")

#Actividad 5 Escape Room - La Arena del Gladiador
print("--- BIENVENIDO A LA ARENA ---")
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha() or nombre == "":
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Estadísticas iniciales
hp_jugador = 100
hp_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12

while hp_jugador > 0 and hp_enemigo > 0:
    print(f"\n=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {hp_jugador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}")
    print("1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opcion = input("Opción: ")
    while not (opcion.isdigit() and opcion in ["1", "2", "3"]):
        print("Error: Ingrese un número válido (1, 2 o 3).")
        opcion = input("Opción: ")

    # Lógica del Jugador
    if opcion == "1":
        danio = float(ataque_pesado)
        if hp_enemigo < 20:
            danio *= 1.5
            print("¡GOLPE CRÍTICO!")
        hp_enemigo -= int(danio)
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")
        
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            hp_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")
            
    elif opcion == "3":
        if pociones > 0:
            hp_jugador += 30
            pociones -= 1
            if hp_jugador > 100: hp_jugador = 100
            print(f"Te has curado. HP actual: {hp_jugador}")
        else:
            print("¡No quedan pociones! Pierdes el turno intentando buscar una.")

    # Turno del Enemigo (solo si sigue vivo)
    if hp_enemigo > 0:
        hp_jugador -= ataque_enemigo
        print(f">> ¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")

# Fin del Juego
if hp_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")

