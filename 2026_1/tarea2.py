dimension = int(input("Ingrese dimensión del cuadrado para el tablero: "))
tablero = input("Tablero: ")
cords = input("Coordenadas de inicio (x,y): ")
energia = int(input("Energía inicial:"))
x = 0
y = 0

#separa las cordenadas de un string a X e Y, separando el string en la coma
for i in range(len(cords)):
    if cords[i] == ",":
        x = int(cords[:i])
        y = int(cords[i+1:])


pos = dimension*y+x

#define un boolean para entrar en el ciclo.
condicion = (x-dimension <= 0 and y-dimension<=0) and (dimension >= 3) and ("C" in tablero) and (len(tablero) % dimension == 0) and (tablero[pos] == "T")

visitado = tablero
visitado = visitado[:pos] + "J" + visitado[pos+1:]

if condicion == False:
    print("Configuración inicial inválida")

while condicion:
    
    valid = False
    move = input("Movimiento (udlr): ")
    if move == 'u':
        y -= 1
        valid = True
    elif move == 'd':
        y += 1
        valid = True
    elif move == 'l':
        x -= 1
        valid = True
    elif move == 'r':
        x += 1
        valid = True
    else:
        print("Movimiento debe ser (u)p, (d)own, (l)eft, o (r)ight")
        valid = False
    
    #revisa si esta fuera del tablero

    
    if (x >= 0 and x-dimension <= 0) and (y-dimension <= 0 and y >=0)  and valid:
        pos = dimension*y+x
        
        
        if tablero[pos] == "C" and visitado[pos] != "J":
            print("Checkpoint alcanzado")
            energia -= 1
        elif tablero[pos] == "T" and visitado[pos] != "J":
            energia -= 1
        elif tablero[pos] == "M":
            print("Movimiento inválido")
            if move == 'u':
                y += 1
            elif move == 'd':
                y -= 1
            elif move == 'l':
                x += 1
            elif move == 'r':
                x -= 1
                        
        elif tablero[pos] == "A" and visitado[pos] != "J":
            energia -= 2
        
        if tablero[pos] != "M":
            visitado = visitado[:pos] + "J" + visitado[pos+1:]
    else:
        print("Movimiento inválido")
        if x < 0:
            x = 0
        elif x-dimension > 0:
            x = 6
        elif y < 0:
            y = 0
        elif y-dimension > 0:
            y = 6
            
    if "C" not in visitado:
        print("¡Mapa finalizado!")
        condicion = False
        
    elif energia <= 0:
        condicion = False
        print("Energía agotada")
    
#print tablero final
if (x-dimension <= 0 and y-dimension<=0) and (dimension >= 3) and ("C" in tablero) and (len(tablero) % dimension == 0) and (tablero[pos] == "T"):
    for fila in range(dimension):
      print(visitado[(fila)*dimension:(dimension)*(fila+1)])

    print("Energía final:",energia)

'''
C: Checkpoint
M: Muro
A: Agua
T: Tierra

u: arriba (up)
d: abajo (down)
l: izquierda (left)
r: derecha (right)
'''