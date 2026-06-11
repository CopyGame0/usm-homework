#pregunta 1
def lista_pedidos(nombre_pedidos):
    archivo_pedidos = open(nombre_pedidos, 'r')
    #    id_pedido, cliente, tiempo_estimado, tiempo_real, costo, reclamo, id_producto
    #e.g: 1      , Juan      ,  30           ,   45      , 8000 ,    1   ,  101

    costo = []
    contador = 0
    for linea in archivo_pedidos:
        if contador != 0:
            temp = str(linea.strip())
            temp = temp.split(";")
            temp = [temp[0],int(temp[-3])]
           # print(temp) #debug, delete later :v
            
            costo.append(temp)
        contador+=1
    #print(costo) #debug, delete later :v
    
    archivo_pedidos.close()
    return costo
    
#pregunta 2
def desempeño(nombre_pedidos, nombre_productos):
    
    tipos = {"Problemático":[],"Eficiente":[],"Costoso":[]}
    """e.g.
    {'Problemático': [[8000, 'Hamburguesa', 30, 45, 'Comida'], [12000, 'Sushi',40, 55, 'Comida']],
     'Costoso': [[8000, 'Hamburguesa', 30, 45, 'Comida'],[12000, 'Sushi', 40, 55, 'Comida']],
     'Eficiente': [[5000, 'Hamburguesa', 20,18, 'Comida'], [6000, 'Pizza', 25, 20, 'Comida']]}
    """
    
    archivos_produc = open(nombre_productos, 'r')
    #    id_producto, nombre        , categoria, precio_base
    #e.g:   101     ,Hamburguesa    ,Comida    ,5000 

    productos= {}
    for linea in archivos_produc:
        
        temp = linea.split(";")
        productos[temp[0]] = temp[1:]
        #{id_producto: [nombre, categoria, precio_base]} tendremos un indice extra, pero es un diccionario asi que no importa :P
    archivos_produc.close()

    costos_pedidos = lista_pedidos(nombre_pedidos) 
    
    archivo_pedidos = open(nombre_pedidos, 'r')

    id_pedidos = {}
    contador = 0
    for linea in archivo_pedidos:
        if contador != 0:
            temp = linea.split(";")
            id_pedidos[temp[0]] = temp[1:]
            #{id_pedido: [cliente, tiempo_estimado, tiempo_real, costo, reclamo, id_producto]}
        contador += 1
    archivo_pedidos.close() 

    lista_costos = []
    for costo in costos_pedidos:
        lista_costos.append(costo[1])
    
    promedio_costos = sum(lista_costos)/len(lista_costos)


    for pedido in id_pedidos:
        t_estimado = int(id_pedidos[pedido][1])
        t_real = int(id_pedidos[pedido][2])
        id = id_pedidos[pedido][-1].strip()

        producto =[int(id_pedidos[pedido][3]), productos[id][0], t_estimado, t_real, productos[id][1]]

        if id_pedidos[pedido][4] == "1": #revisa si hay reclamos
            tipos["Problemático"].append(producto)
        if t_real < t_estimado: # tiene retraso?
            tipos["Eficiente"].append(producto)
        if int(id_pedidos[pedido][3]) > promedio_costos: # costo mayor al promedio?
            tipos["Costoso"].append(producto)

        for tipo in tipos:
            tipos[tipo].sort()
            
    return tipos
        
#print(desempeño("pedidos.csv", "productos.csv")) #e.g, delte later :v

#Pregunta 3

def clasificar(archivo_pedidos,  archivo_productos, categoría):
    tipos = desempeño(archivo_pedidos,  archivo_productos)

    for criterio in tipos:
        archivo = open(criterio+".txt", 'w')
        contador = 0
        for producto in tipos[criterio] and contador < 10:
            temp = "#{0} pedido {1}: tiempo estimado {2} min, tiempo real {3} min, costo ${4}\n".format(contador+1, producto[1], producto[2], producto[3], producto[0])
            archivo.write(temp)

        archivo.close()

    calificados = 0
    
    for criterio in tipos:
        if tipos[criterio][-1] == categoría:
            calificados += 1
    return calificados

#fix needed, delete later :v
print(clasificar("pedidos.csv", "productos.csv", "Tecnologia")) 