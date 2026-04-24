def generar_indice_limpio(lista_hardware):
    indice_hardware = {}
    cantidad_descartado = 0
 
    for item in lista_hardware:
        
        if item.get("estado") == "obsoleto" or item.get("stock", 0) < 0:
            cantidad_descartado += 1 
            continue
        
        sn = item.get("codigo_sn")
        if sn:
            indice_hardware[sn] = item
 
    return indice_hardware, cantidad_descartado


def proyectar_ingresos(indice_hardware):
    seleccionados = []
    categoriaObjetivo = ["Tarjetas Gráficas", "Procesadores"]
 
    for item in indice_hardware.values():
        if item.get("categoria") in categoriaObjetivo:
            
            item_con_calculo = item.copy() 
            item_con_calculo["valor_potencial"] = item_con_calculo["stock"] * item_con_calculo["precio_unitario"]
            seleccionados.append(item_con_calculo)
            
    # Ordenamiento: descendente por valor (-x) y ascendente por marca
    seleccionados.sort(key=lambda x: (-x["valor_potencial"], x["marca"]))
    
    return seleccionados

def formatear_catalogo_web(indice_hardware):
    catalogo_web = {}
 
    for item in indice_hardware.values():
        producto = item.copy()
        categoria = producto.pop("categoria", "otros")
 
        producto["etiqueta_escazes"] = producto.get("stock", 0) < 3
 
        if categoria not in catalogo_web:
            catalogo_web[categoria] = []
            
        catalogo_web[categoria].append(producto)
        
    return catalogo_web