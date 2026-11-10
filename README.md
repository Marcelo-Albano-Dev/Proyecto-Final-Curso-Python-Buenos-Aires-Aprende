# Proyecto Final - Curso Python Buenos Aires Aprende

Sistema de inventario desarrollado en Python con SQLite para registrar y administrar productos.

## Funcionalidades

- Registrar nuevos productos.
- Visualizar todos los productos.
- Buscar un producto por ID.
- Actualizar los datos de un producto.
- Eliminar productos.
- Generar reportes de productos con bajo stock.
- Persistir la información en la base de datos `inventario.db`.

## Requisitos

- Python 3.10 o superior.

No se necesitan paquetes externos: el proyecto utiliza `sqlite3`, incluido en Python.

## Ejecución

Desde la carpeta del proyecto, ejecutar:

```bash
python main.py
```

La aplicación crea automáticamente la tabla `productos` si todavía no existe.

## Estructura del proyecto

```text
.
├── main.py          # Menú principal e interacción con el usuario
├── operaciones.py   # Operaciones sobre la base de datos
└── inventario.db    # Base SQLite con los productos cargados
```

## Modelo de datos

La tabla `productos` contiene los siguientes campos:

- `id`: identificador único.
- `nombre`: nombre del producto.
- `descripcion`: descripción breve.
- `cantidad`: stock disponible.
- `precio`: precio del producto.
- `categoria`: categoría del producto.
