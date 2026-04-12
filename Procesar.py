def generar_indice_limpio(lista_hardware):
    indice_hardaware={}
    cantidad_descartado=0

    for item in lista_hardware:

        if item.get("estado")=="obsoleto" or item.get("stock", 0) < 0:
            cantidad_descartado=+1
            continue
        sn = item.get("codigo_sn")
        if sn:
            indice_hardaware[sn]= item

    return (indice_hardaware, cantidad_descartado)   
 
def proyectar_ingresos(indice_hardware):
    seleccionados= []
    categoriaObjetivo=["Tarjetas Gráficas", "Procesadores"]

    for item in indice_hardware.values():
        if item.get("Categoria") in categoriaObjetivo:
            item["valor_potencia"]= item["stock"] * item["precio_unitario"]
            seleccionados.append(item)
            
    seleccionados.sort(key=lambda x: (-x["valor_potencial"], x["marca"]))
    
    return seleccionados

def formatear_catalogo_web(indice_hardware):
    catalogo_web={}

    for item in indice_hardware.values():
        producto= item.copy(  )
        categoria= producto.pop("categoria", "otros")

        producto["etiqueta_escazes"]=producto.get("stock", 0) < 3

        if categoria not in catalogo_web:
            catalogo_web[categoria]=[]
            
            catalogo_web[categoria].append(producto)
        
    return catalogo_web
        
        
  