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
            temp = [int(temp[0]),int(temp[-3])]
           # print(temp) #debug, delete later :v
            
            costo.append(temp)
        contador+=1
    #print(costo) #debug, delete later :v
    
    archivo_pedidos.close()
    return costo
    
#pregunta 2
def desempeño(nombre_pedidos, nombre_productos):
    
    tipos = {"Problemático":[],"Eficiente":[],"Costoso":[]}
    
    archivos_produc = open(nombre_productos, 'r')
    #    id_producto, nombre        , categoria, precio_base
    #e.g:   101     ,Hamburguesa    ,Comida    ,5000 
    
    costos = lista_pedidos(nombre_pedidos) 
    
    
    archivos_produc.close()
