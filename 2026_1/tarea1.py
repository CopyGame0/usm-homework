#descripccion del juego
print("¡Bienvenido Pysano! En este juego 2 jugadores se turnarán para dar vueltas al gimnasio, pasando por puntos de control. \n") 

#TIEMPO, juego por turnos.
tiempo1 = int(input("Tiempo jugador 1 (minutos): "))
tiempo2 = int(input("Tiempo jugador 2 (minutos): "))
tiempo_total = tiempo1 + tiempo2
print("Tiempo total del juego:", tiempo_total//60 , "horas, y", tiempo_total%60, "minutos \n")

#ENERGIA
peso1 = float(input("Peso jugador 1: "))
percepcion1= int(input("Esfuerzo percibido jugador 1 (1-10): ")) 
esfuerzo1 = 1.5+0.4*(percepcion1**1.3)
energia_1 = (tiempo1/60)*peso1*esfuerzo1
print("Energia del jugador 1:", round(energia_1, 2),  "kcal")

#ENERGIA (jugador 2)
peso2 = float(input("Peso jugador 2: "))
percepcion2= int(input("Esfuerzo percibido jugador 2 (1-10): ")) 
esfuerzo2 = 1.5+0.4*(percepcion2**1.3)
energia_2 = (tiempo2/60)*peso2*esfuerzo2
print("Energia del jugador 2:" , round(energia_2, 2), "kcal")

print("Promedio energía:", round((energia_1+energia_2)/2, 2), "\n" )

#PUNTAJE
acciones = int(input("Acciones realizadas: "))
rotaciones=int(input("Rotaciones de rol (0-5): "))
seguridad =int(input("Seguridad del juego (1-5): "))

puntaje_base = 2000 + 300*acciones + 1200*rotaciones + 1000*seguridad
print("Puntaje de base:", puntaje_base)

#sinergia
sinergia = 0.0
if puntaje_base < 10000:
    sinergia = 0.08
elif 10000 < puntaje_base and puntaje_base < 20000:
    sinergia = 0.1
else:
    sinergia = 0.12

puntaje_total = round(puntaje_base + (puntaje_base*sinergia) + esfuerzo1 + esfuerzo2, 2)
print("Puntaje sin bonos: ", puntaje_total)

bonus = 0
if seguridad >= 2:
    #bono 1
    if  45 < tiempo_total and acciones >= 25:
        bonus += 500
    #bono 2
    if rotaciones > 4 or seguridad > 3:
        bonus += 300

puntaje_total = round(puntaje_base + bonus + (puntaje_base*sinergia) + esfuerzo1 + esfuerzo2, 2)
print("Puntaje con bonos: ", puntaje_total, "\n")
    
#TIEMPO DE ARMADO
elementos_instalar = int(input("Elementos a instalar: "))
elementos_por_minuto = int(input("Elementos por minuto que puede armar: "))
print("Tardará", round(elementos_instalar/elementos_por_minuto, 1), "minutos en armar el juego")


