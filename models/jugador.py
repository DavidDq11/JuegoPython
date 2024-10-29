class Jugador:
    # El método __init__ es como el constructor en TypeScript
    def __init__(self, nombre: str, direccion: str, telefono: str, descripcion: str, numeroJugado: int = 3):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.descripcion = descripcion
        self.numeroJugado = numeroJugado