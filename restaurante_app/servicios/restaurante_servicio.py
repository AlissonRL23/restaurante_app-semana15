# servicios/restaurante_servicio.py
import uuid
from servicios.archivo_servicio import ArchivoServicio
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self):
        self.archivo_usuarios = "datos/usuarios.json"
        self.archivo_productos = "datos/productos.json"
        self.archivo_ventas = "datos/ventas.json"

    def obtener_usuarios(self) -> list:
        return ArchivoServicio.cargar_json(self.archivo_usuarios)

    def obtener_productos(self) -> list:
        return ArchivoServicio.cargar_json(self.archivo_productos)

    def obtener_ventas(self) -> list:
        data = ArchivoServicio.cargar_json(self.archivo_ventas)
        return [Venta.from_dict(v) for v in data]

    def registrar_venta(self, id_usuario: str, id_producto: str) -> tuple[bool, str]:
        if not id_usuario or not id_producto:
            return False, "Debe seleccionar un usuario y un producto válidos."

        usuarios = self.obtener_usuarios()
        productos = self.obtener_productos()

        usuario = next((u for u in usuarios if u["id"] == id_usuario), None)
        producto = next((p for p in productos if p["id"] == id_producto), None)

        if not usuario:
            return False, "El usuario seleccionado no existe."
        if not producto:
            return False, "El producto seleccionado no existe."

        id_venta = f"VNT-{str(uuid.uuid4())[:8].upper()}"
        nueva_venta = Venta(
            id_venta=id_venta,
            id_usuario=usuario["id"],
            nombre_usuario=usuario["nombre"],
            id_producto=producto["id"],
            nombre_producto=producto["nombre"],
            precio=float(producto["precio"])
        )

        ventas_actuales = ArchivoServicio.cargar_json(self.archivo_ventas)
        ventas_actuales.append(nueva_venta.to_dict())
        
        exito = ArchivoServicio.guardar_json(self.archivo_ventas, ventas_actuales)
        if exito:
            return True, f"Venta {id_venta} registrada exitosamente."
        return False, "Ocurrió un error al guardar la venta."
