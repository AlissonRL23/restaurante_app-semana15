# modelos/venta.py
from datetime import datetime

class Venta:
    def __init__(self, id_venta: str, id_usuario: str, nombre_usuario: str, 
                 id_producto: str, nombre_producto: str, precio: float, fecha: str = None):
        self.id_venta = id_venta
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> dict:
        return {
            "id_venta": self.id_venta,
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "id_producto": self.id_producto,
            "nombre_producto": self.nombre_producto,
            "precio": self.precio,
            "fecha": self.fecha
        }

    @staticmethod
    def from_dict(data: dict):
        return Venta(
            id_venta=data["id_venta"],
            id_usuario=data["id_usuario"],
            nombre_usuario=data["nombre_usuario"],
            id_producto=data["id_producto"],
            nombre_producto=data["nombre_producto"],
            precio=data["precio"],
            fecha=data["fecha"]
        )
