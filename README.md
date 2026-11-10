# Proyecto Final - Python

Este es mi proyecto final para el curso Python de Buenos Aires Aprende.

El programa consiste en un inventario sencillo de productos. La información se guarda en una base de datos SQLite para que no se pierda al cerrar el programa.

## Qué se puede hacer

Desde el menú principal se puede:

- Agregar productos.
- Ver todos los productos cargados.
- Buscar un producto por su ID.
- Modificar los datos de un producto.
- Eliminar productos.
- Ver qué productos tienen poco stock.

## Cómo ejecutarlo

Se necesita tener Python instalado. Desde la carpeta del proyecto, ejecutar:

```bash
python main.py
```

La base de datos utilizada es `inventario.db`. Si la tabla todavía no existe, el programa la crea automáticamente al iniciarse.

## Archivos principales

```text
.
├── main.py
├── operaciones.py
└── inventario.db
```

- `main.py`: contiene el menú y la interacción con el usuario.
- `operaciones.py`: contiene las funciones para trabajar con la base de datos.
- `inventario.db`: base de datos con los productos de ejemplo.
