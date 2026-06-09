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
    for linea in archivo_pedidos:
        temp = linea.split(";")
        id_pedidos[temp[0]] = temp[1:]
        #{id_pedido: [cliente, tiempo_estimado, tiempo_real, costo, reclamo, id_producto]}

    
        
    
    archivo_pedidos.close() 
