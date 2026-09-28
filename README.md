# Restaurante App - Semana 15: Manejo de Eventos

## Descripción
Evolución del proyecto `restaurante_app` enfocada en el estudio de los **conceptos fundamentales de manejo de eventos**. A través de la gestión de ventas, se conecta la acción del usuario en un botón (`command=`) con un callback, delegando la lógica al servicio correspondiente y persistiendo la información en formato JSON.

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
│   └── logo.png
├── main.py
└── README.md
