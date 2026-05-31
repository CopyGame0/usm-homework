destinos_buceo = [
    ["Gran Barrera de Coral", "Australia", 9.5, ["corales", "biodiversidad", "tropical"]],
    ["Islas Galápagos", "Ecuador", 9.8, ["tiburones", "pelágicos", "corrientes"]],
    ["Agujero Azul", "Belice", 8.9, ["cuevas", "profundidad", "icónico"]],
    ["Mar Rojo", "Egipto", 9.2, ["arrecifes", "visibilidad", "naufragios"]],
    ["Raja Ampat", "Indonesia", 9.9, ["corales", "biodiversidad", "fotografía macro"]],
    ["Cozumel", "México", 8.7, ["corrientes", "paredes", "tropical"]],
    ["Islas Maldivas", "Maldivas", 9.4, ["pelágicos", "arrecifes", "lujo"]],
    ["Sipadan", "Malasia", 9.6, ["tiburones", "tortugas", "protegido"]],
    ["Silfra", "Islandia", 9.0, ["agua dulce", "visibilidad", "frío"]],
    ["Islas Similan", "Tailandia", 8.5, ["arrecifes", "biodiversidad", "tropical"]],
    ["Cenotes de Yucatán", "México", 9.3, ["cuevas", "agua dulce", "visibilidad"]],
    ["Blue Corner", "Palaos", 9.7, ["tiburones", "corrientes", "pelágicos"]],
    ["Bahía de Hanauma", "Hawái", 7.8, ["tortugas", "arrecifes", "volcánico"]],
    ["SS Thistlegorm", "Egipto", 9.5, ["naufragios", "historia", "visibilidad"]],
    ["Tubbataha Reef", "Filipinas", 9.4, ["arrecifes", "pelágicos", "protegido"]],
    ["Isla del Coco", "Costa Rica", 9.8, ["tiburones", "pelágicos", "corrientes"]],
    ["Riviera Maya", "México", 8.4, ["tortugas", "arrecifes", "tropical"]],
    ["Beqa Lagoon", "Fiyi", 8.8, ["tiburones", "corales", "tropical"]],
    ["Wolf y Darwin", "Ecuador", 9.9, ["tiburones", "pelágicos", "corrientes"]],
    ["Poor Knights Islands", "Nueva Zelanda", 8.6, ["cuevas", "biodiversidad", "frío"]]
]

# Pregunta 1

def lugares_mejor_calificados(destinos):
   best = []
   calificaciones = []
   for i in destinos:
      calificaciones.append(i[2])
   
   # Calificaicones ordenadas de mayor a menor   
   calificaciones.sort()
   calificaciones.reverse()
   
   for lugar in destinos:
      if lugar[2] >= calificaciones[4]:
         temp = list(lugar)
         temp.reverse()
         best.append(temp[-3:])
         #vamos a incluir la calificaicon (al principio) para poder hacer .sort() \(￣︶￣*\))
         
   #now we sort :D
   best.sort()
   best.reverse()
   #nos desasemos de las calificaciones y revertimos las listas (para mantener el orden original)
   for i in range(len(best)):
      temp = list(best[i][1:])
      temp.reverse()
      best[i] = list(temp)
         
   
   return best

#nota 1: comprado al ejemplo, mi solucion avezes da alrevez (e.g: [0] y [1] del output), pero solo cuando las calificaiones son iguales.
#        Espero que esto no sea contado como incorecto /_ \

#e.g:        [["Wolf y Darwin", "Ecuador"], ["Raja Ampat", "Indonesia"], ["Islas Galápagos", "Ecuador"], ["Isla del Coco", "Costa Rica"], ["Blue Corner", "Palaos"]]
#            [['Raja Ampat', 'Indonesia'], ['Wolf y Darwin', 'Ecuador'], ['Islas Galápagos', 'Ecuador'], ['Isla del Coco', 'Costa Rica'], ['Blue Corner', 'Palaos']]

print(lugares_mejor_calificados(destinos_buceo))



# Pregunta 2

def tipos_de_buceo_mejor_calificados(destinos):
   
   #Vamos a organizar 3 vezes los datos, la primera sera en tipos_1 que contendra los tipos y una lista de sus calificaciones.
   #Asi el tipo y sus calificacion tendran el mismo index, pero en listas distintas
   tipos_1 = [[],[]]
   tipos_calificados = []
   mejores_tipos = []
   
   for lugar in destinos:
      for tipo in lugar[-1]:
         #Si no esta el tipo no esta en tipos crea su index y agrega una "lista" de calificaciones
         if tipo not in tipos_1[0]:
            
            tipos_1[0].append(tipo)
            temp = [lugar[-2]]
            tipos_1[1].append(list(temp))
            
         else:
            index = tipos_1[0].index(tipo)
            tipos_1[1][index].append(lugar[-2])

   for i in range(len(tipos_1[0])):
      #ahora vamos a sumar las notas y sacar el promedio (si es solo una nota su promedio sera la nota, asi que no importa) 
      tipos_1[1][i] = sum(tipos_1[1][i])/len(tipos_1[1][i])
   
      #una vez obtenido el promedio vamos a organizar los datos en listas: [n, "tipo"] para poder usar .sort()
      temp = [tipos_1[1][i],tipos_1[0][i]]
      tipos_calificados.append(temp)
   
   tipos_calificados.sort()
   
   #ahora que los tipos estan organizados de menor a mayor, solo nesesitamos los ultimos 3
   mejores_tipos = [tipos_calificados[-1][1], tipos_calificados[-2][1],tipos_calificados[-3][1]]
      
   return mejores_tipos

print(tipos_de_buceo_mejor_calificados(destinos_buceo))



# Pregunta 3
def recomendar_lugares(destinos, calificación_mínima, lista_tipos_de_buceos):
   filtrado = []
   
   for lugar in destinos:
      if lugar[2] >= calificación_mínima:
         
         #revisa si algun tipo de el lugar esta en la lista dada
         for j in lugar[-1]:
            if j in lista_tipos_de_buceos:
               
               #creamos una variable temp para no afectar la lista original ~(￣▽￣)~
               temp = list(lugar)
               temp.reverse()
               
               #IMPORTANTE: revisa si ya existe para no tener duplicados
               if temp[-3:] not in filtrado:
                  filtrado.append(temp[-3:])
     
   filtrado.sort()
   filtrado.reverse()
   
   for i in range(len(filtrado)):
      temp = list(filtrado[i])
      temp.reverse()
      filtrado[i] = list(temp)
      
   if filtrado != []:
      return filtrado
   else:
      return "No es posible recomendar lugares. "

print(recomendar_lugares(destinos_buceo, 8.0, ["biodiversidad", "corales"]))
print(recomendar_lugares(destinos_buceo, 7.0, ["buceo en el aire"]))
