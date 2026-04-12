import json
from Procesar import generar_indice_limpio, proyectar_ingresos, formatear_catalogo_web

lista_hardware = [
    {"codigo_sn": "SN-001", "nombre": "RTX 4080", "precio_unitario": 1200.0, "stock": 5, "categoria": "Tarjetas Gráficas", "estado": "activo", "marca": "Asus"},
    {"codigo_sn": "SN-002", "nombre": "i9-13900K", "precio_unitario": 600.0, "stock": 2, "categoria": "Procesadores", "estado": "activo", "marca": "Intel"},
    {"codigo_sn": "SN-003", "nombre": "RTX 3060", "precio_unitario": 350.0, "stock": -1, "categoria": "Tarjetas Gráficas", "estado": "activo", "marca": "MSI"},
    {"codigo_sn": "SN-004", "nombre": "Monitor 4K", "precio_unitario": 450.0, "stock": 10, "categoria": "Monitores", "estado": "activo", "marca": "LG"},
    {"codigo_sn": "SN-005", "nombre": "Ryzen 7 5800X", "precio_unitario": 300.0, "stock": 8, "categoria": "Procesadores", "estado": "activo", "marca": "AMD"},
    {"codigo_sn": "SN-006", "nombre": "Teclado Mecánico", "precio_unitario": 100.0, "stock": 15, "categoria": "Periféricos", "estado": "obsoleto", "marca": "Razer"}, 
    {"codigo_sn": "SN-007", "nombre": "RX 7900 XTX", "precio_unitario": 1000.0, "stock": 2, "categoria": "Tarjetas Gráficas", "estado": "activo", "marca": "Gigabyte"},
    {"codigo_sn": "SN-008", "nombre": "i5-12400", "precio_unitario": 200.0, "stock": 20, "categoria": "Procesadores", "estado": "activo", "marca": "Intel"},
    {"codigo_sn": "SN-009", "nombre": "RTX 4090", "precio_unitario": 2000.0, "stock": 1, "categoria": "Tarjetas Gráficas", "estado": "activo", "marca": "Nvidia"},
    {"codigo_sn": "SN-010", "nombre": "Mouse Gamer", "precio_unitario": 50.0, "stock": 30, "categoria": "Periféricos", "estado": "activo", "marca": "Logitech"}
]

def ejecutar_sistema():
    try:

        indice, descartados = generar_indice_limpio(lista_hardware)
    
        proyeccion = proyectar_ingresos(indice)
        
        catalogo = formatear_catalogo_web(indice)

       
        print(f"\tSistema de Inventario: Hardware y Componentes de PC")
        print(f"\tItems descartados: {descartados}\n")
        
        print("\tCatálogo Web Formateado: ")
        print(json.dumps(catalogo, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"Se produjo un error durante la ejecución: {e}")

if __name__ == "__main__":
    ejecutar_sistema()