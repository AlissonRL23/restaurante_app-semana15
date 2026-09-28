# modelos/usuario.py
class Usuario:
    def __init__(self, id_usuario: str, nombre: str, correo: str, rol: str = "Cliente"):
        self.id = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "rol": self.rol
        }

    @staticmethod
    def from_dict(data: dict):
        return Usuario(
            id_usuario=data["id"],
            nombre=data["nombre"],
            correo=data["correo"],
            rol=data.get("rol", "Cliente")
        )
