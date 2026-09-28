# modelos/producto.py
class Producto:
    def __init__(self, id_producto: str, nombre: str, precio: float, categoria: str = "General"):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    @staticmethod
    def from_dict(data: dict):
        return Producto(
            id_producto=data["id"],
            nombre=data["nombre"],
            precio=data["precio"],
            categoria=data.get("categoria", "General")
        )
