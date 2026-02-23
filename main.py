import json

def cargar_inventario():
    try:
        with open("Inventario.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

inventario = cargar_inventario()
def agregar_producto():
    id_producto = input("Ingresa el ID del prodcuto: ")
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad del producto: "))
            break
        except ValueError:
            print("Error: Debes ingresar un numero entero valido. Intenta de nuevo")
    while True:
        try:
            precio = float(input("Ingresa el precio del producto: "))
            break
        except ValueError:
            print("Error: Debes ingresar un numero valido. Intenta de nuevo")
    
    inventario[id_producto] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    
    guardar_datos()

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario esta Vacio")
    else:
        print("--- INVENTARIO ACTUAL ---")
        for id_producto, info in inventario.items():
            print(f"ID: {id_producto} | Producto: {info['nombre']} | Cantidad: {info['cantidad']} | Precio: ${info['precio']:.3f}")
            
def buscar_inventario():
    id_buscar = input("Ingresa el ID del producto que deseas buscar: ")
    if id_buscar in inventario:
        info = inventario[id_buscar]
        print(f"ID: {id_buscar} | Producto: {info['nombre']} | Cantidad: {info['cantidad']} | Precio: ${info['precio']:.3f}")
    else:
        print("El producto con ese ID no se encuentra en el inventario")
            
def actualizar_producto():
    id_actualizar = input("Ingresa el ID del producto que deseas actualizar: ")
    if id_actualizar in inventario: 
        while True:
            try:
                nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
                break
            except ValueError:
                print("Error: Debes ingresar un numero valido. Intenta de nuevo")
        inventario[id_actualizar]['cantidad'] = nueva_cantidad
        print("¡Cantidad actualizada con exito!")
    else:
        print("Error: El producto con ese ID no existe en el inventario")
    guardar_datos()
        
def eliminar_producto():
    id_eliminar = input("INgrese el ID del producto que quiere eliminar: ")
    if id_eliminar in inventario:
        del inventario[id_eliminar]
        print("El producto se ha eliminado correcatamente")
    else:
        print("Error: El ID del producto no se ha encontrado o no existe")
    guardar_datos()
    
def guardar_datos():
    with open("Inventario.json", "w") as archivo:
        json.dump(inventario, archivo, indent=4)



def menu_principal():
    while True: 
        print("--- SISTEMA DE GESTION DE INVENTARIO BASICO ---")
        print("1. Agregar prodcuto")
        print("2. Mostrar inventario")
        print("3. Buscar por ID")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Elige una opcion (1/2/3/4/5/6): ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_inventario()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")


menu_principal()

    
            
