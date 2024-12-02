from conexion import BaseDeDatos

class Prestamo:
    def __init__(self, db):
        self.db = db

    def registrar_prestamo(self, UsuarioId, LibroId, FechaPrestamo, FechaDevolucion, Multa):
        query = "INSERT INTO Prestamos (UsuarioId, LibroId, FechaPrestamo, FechaDevolucion, Multa) VALUES (%s, %s, %s, %s, %s)"
        valores = (UsuarioId, LibroId, FechaPrestamo, FechaDevolucion, Multa)
        self.db.ejecutar(query, valores)
        return "Prestamo registrado con éxito."
    
    def actualizar_prestamo(self, Id, UsuarioId, LibroId, FechaPrestamo, FechaDevolucion, Multa):
        query = "UPDATE Prestamos SET UsuarioId=%s, LibroId=%s, FechaPrestamo=%s, FechaDevolucion=%s, Multa=%s WHERE Id=%s"
        valores = (UsuarioId, LibroId, FechaPrestamo, FechaDevolucion, Multa, Id)
        self.db.ejecutar(query, valores)
        return "Prestamo actualizado con éxito."
    
    def ver_prestamo(self, Id):
        query = "SELECT * FROM Prestamos WHERE Id = %s"
        return self.db.obtener_datos(query, (Id,))
    
    def eliminar_prestamo(self, Id):
        query = "DELETE FROM Prestamos WHERE Id = %s"
        self.db.ejecutar(query, (Id,))
        return "Prestamo eliminado con éxito."
    
    def ver_prestamos(self):
        query = "SELECT * FROM Prestamos"
        return self.db.obtener_datos(query)
    