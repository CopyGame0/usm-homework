def diccionario_productos(nombre_productos):
    archivos_produc = open(nombre_productos, 'r')
    #    id_producto, nombre        , categoria, precio_base
    #e.g:   101     ,Hamburguesa    ,Comida    ,5000 

    productos= {}
    for linea in archivos_produc:
        
        temp = linea.split(";")
        productos[temp[0]] = temp[1:]
        #{id_producto: [nombre, categoria, precio_base]} tendremos un indice extra, pero es un diccionario asi que no importa :P
    archivos_produc.close()

    return productos

def diccionario_pedidios(nombre_pedidos):
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
    
    return id_pedidos

#pregunta 1
def lista_pedidos(nombre_pedidos):
    pedidos = diccionario_pedidios(nombre_pedidos)

    costo = []

    for id in pedidos:
        temp = [id, int(pedidos[id][3])]
        costo.append(temp)

    #print(costo) #debug, delete later :v
    
    return costo
    
#pregunta 2
def desempeño(nombre_pedidos, nombre_productos):
    
    tipos = {"Problemático":[],"Eficiente":[],"Costoso":[]}
    """e.g.
    {'Problemático': [[8000, 'Hamburguesa', 30, 45, 'Comida'], [12000, 'Sushi',40, 55, 'Comida']],
     'Costoso': [[8000, 'Hamburguesa', 30, 45, 'Comida'],[12000, 'Sushi', 40, 55, 'Comida']],
     'Eficiente': [[5000, 'Hamburguesa', 20,18, 'Comida'], [6000, 'Pizza', 25, 20, 'Comida']]}
    """
        
    productos= diccionario_productos(nombre_productos)
   
    costos_pedidos = lista_pedidos(nombre_pedidos) 
    
    id_pedidos = diccionario_pedidios(nombre_pedidos)

    suma = 0
    cantidad = 0
    for costo in costos_pedidos:
        suma += costo[1]
        cantidad += 1
    
    promedio_costos = suma/cantidad


    for pedido in id_pedidos:
        t_estimado = int(id_pedidos[pedido][1])
        t_real = int(id_pedidos[pedido][2])
        id = id_pedidos[pedido][-1].strip()
        costo_base = int(productos[id][2])
        costo = int(id_pedidos[pedido][3])

        producto =[costo, productos[id][0], t_estimado, t_real, productos[id][1].strip()]

        if id_pedidos[pedido][4] == "1" and t_real > t_estimado: #revisa si hay reclamos
            tipos["Problemático"].append(producto)

        if t_real <= t_estimado and id_pedidos[pedido][4] == "0" and costo <= promedio_costos: # es eficiente??
            tipos["Eficiente"].append(producto)

        if costo > promedio_costos or costo > costo_base: # costo mayor al promedio?
            tipos["Costoso"].append(producto)

        for tipo in tipos:
            tipos[tipo].sort()
            
    return tipos
        
#print(desempeño("pedidos_grande.csv", "productos_grande.csv")) #e.g, delete later :v
#print(desempeño("pedidos.csv", "productos.csv")) #e.g, delete later :v

#Pregunta 3

def clasificar(archivo_pedidos,  archivo_productos, categoría):
    tipos = desempeño(archivo_pedidos,  archivo_productos)
    calificados = 0


    for criterio in tipos:
        archivo = open(criterio+".txt", 'w')
        contador = 0
        for producto in tipos[criterio] :
            if producto[-1] != categoría and contador < 10:
                temp = "#{0} pedido {1}: tiempo estimado {2} min, tiempo real {3} min, costo ${4}\n".format(contador+1, producto[1], producto[2], producto[3], producto[0])
                archivo.write(temp)
                contador+=1
            elif producto[-1] == categoría:
                calificados += 1
           
        archivo.close()
  
    return calificados

#fix needed, delete later :v
print(clasificar("pedidos_grande.csv", "productos_grande.csv", "Tecnologia")) 