import sqlite3

def conectar():
    # Creando conexion con el archivo
    conexion = sqlite3.connect("inventario.db")
    return conexion

def crear_tabla():
    # Crear la tabla solicitada en los requerimientos
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
        """)
        conexion.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        if 'conexion' in locals():
            conexion.close()

def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))

        conexion.commit()
        print(f"El producto '{nombre}' ha sido registrado con éxito.")
    except sqlite3.Error as error:
        print(error)
    finally:
        conexion.close()

def obtener_productos():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT id, nombre, descripcion, cantidad, precio, categoria
            FROM productos
            ORDER BY id
        """)

        productos = cursor.fetchall()
        return productos
    except sqlite3.Error as error:
        print(error)
        return []
    finally:
        conexion.close()

def obtener_producto_segun_id(id_producto):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT * FROM productos
            WHERE id = ? 
        """, (id_producto,))

        producto = cursor.fetchone()
        return producto
    except sqlite3.Error as error:
        print(error)
    finally:
        conexion.close()

def actualizar_producto(id_producto, nombre, descripcion, cantidad, precio, categoria):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        """, (nombre, descripcion, cantidad, precio, categoria, id_producto))
        
        conexion.commit()
        print("Datos del producto actualizados correctamente.")
    except sqlite3.Error as error:
        print(error)
    finally:
        conexion.close()

def eliminar_producto(id_producto):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM productos
            WHERE id = ?
        """, (id_producto,))

        conexion.commit()

        if cursor.rowcount > 0:
            print("El producto ha sido eliminado del inventario.")
        else:
            print("Producto no encontrado.")
    except sqlite3.Error as error:
        print(error)
    finally:
        conexion.close()

def obtener_reporte_bajo_stock(limite):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT id, nombre, cantidad 
            FROM productos
            WHERE cantidad <= ?
            ORDER BY cantidad ASC
        """, (limite,))

        productos_bajo_stock = cursor.fetchall()
        return productos_bajo_stock
    except sqlite3.Error as error:
        print(error)
        return []
    finally:
        conexion.close()