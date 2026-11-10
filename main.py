import operaciones

# Me aseguro de que la base y la tabla existan al arrancar
operaciones.crear_tabla()

while True:
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Registrar nuevo producto")
    print("2. Visualizar datos de los productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto por ID")
    print("6. Reporte de bajo stock")
    print("7. Salir")

    opcion = input("Ingresa una opcion: ").strip()

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
            while nombre == "":
                print("El nombre no puede estar vacío.")
                nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
                
            descripcion = input("Ingrese una breve descripción: ").strip()
            
            # Validación de cantidad (entero)
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad disponible: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                        continue
                    break
                except ValueError:
                    print("Error: debe ingresar un número entero.")
                    
            # Validación de precio (real)
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: $"))
                    if precio <= 0:
                        print("El precio debe ser mayor a cero.")
                        continue
                    break
                except ValueError:
                    print("Error: debe ingresar un número válido.")
                    
            categoria = input("Ingrese la categoría del producto: ").strip().capitalize()

            operaciones.registrar_producto(nombre, descripcion, cantidad, precio, categoria)

        case "2":
            productos = operaciones.obtener_productos()
            
            if len(productos) == 0:
                print("No hay productos registrados en el inventario.")
            else:
                print("\n-- PRODUCTOS REGISTRADOS --")
                for prod in productos:
                    print(f"ID: {prod[0]} | {prod[1]} | Desc: {prod[2]} | Cant: {prod[3]} | Precio: ${prod[4]} | Cat: {prod[5]}")

        case "3":
            try:
                id_prod = int(input("Ingrese el ID del producto a modificar: "))
                producto_actual = operaciones.obtener_producto_segun_id(id_prod)
                
                if producto_actual:
                    print(f"Modificando producto: {producto_actual[1]}")
                    print("Nota: Para mantener el dato actual, simplemente volvé a escribirlo.")
                    
                    nombre_nuevo = input("Ingresa el nuevo nombre: ").strip().capitalize()
                    descripcion_nueva = input("Ingresa la nueva descripción: ").strip()
                    cantidad_nueva = int(input("Ingresa la nueva cantidad: "))
                    precio_nuevo = float(input("Ingresa el nuevo precio: $"))
                    categoria_nueva = input("Ingresa la nueva categoría: ").strip().capitalize()
                    
                    operaciones.actualizar_producto(id_prod, nombre_nuevo, descripcion_nueva, cantidad_nueva, precio_nuevo, categoria_nueva)
                else:
                    print("El ID de producto ingresado no existe.")
            except ValueError:
                print("Error: El ID, la cantidad y el precio deben ser valores numéricos.")

        case "4":
            try:
                id_prod = int(input("Ingrese el ID del producto que desea eliminar: "))
                operaciones.eliminar_producto(id_prod)
            except ValueError:
                print("Error: Debe ingresar un ID numérico entero.")

        case "5":
            try:
                id_prod = int(input("Ingrese el ID del producto: "))
                producto = operaciones.obtener_producto_segun_id(id_prod)

                if producto:
                    print("\n-- PRODUCTO ENCONTRADO --")
                    print(f"ID: {producto[0]}")
                    print(f"Nombre: {producto[1]}")
                    print(f"Descripción: {producto[2]}")
                    print(f"Cantidad: {producto[3]}")
                    print(f"Precio: ${producto[4]}")
                    print(f"Categoría: {producto[5]}")
                else:
                    print("El producto buscado no existe.")
            except ValueError:
                print("Error: Debe ingresar un ID numérico entero.")

        case "6":
            try:
                limite = int(input("Ingrese el límite de cantidad para generar el reporte: "))
                productos_reporte = operaciones.obtener_reporte_bajo_stock(limite)
                
                if len(productos_reporte) == 0:
                    print(f"No hay productos con stock igual o inferior a {limite}.")
                else:
                    print(f"\n-- REPORTE: PRODUCTOS CON STOCK <= {limite} --")
                    for prod in productos_reporte:
                        print(f"ID: {prod[0]} | Producto: {prod[1]} | Cantidad actual: {prod[2]}")
            except ValueError:
                print("Error: El límite debe ser un número entero.")

        case "7":
            print("Saliendo del programa de inventario...")
            break
            
        case _:
            print("La opción ingresada es inválida, intente de nuevo.")