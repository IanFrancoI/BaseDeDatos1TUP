from conexion import BaseDeDatos

class Usuario:
    def __init__(self,db):
        self.db = db

    def registrar_usuario(self, Nombre, Direccion, Telefono, FechaRegistro, EstadoCuota):
        query = "INSERT INTO Usuarios (Nombre, Direccion, Telefono, FechaRegistro, EstadoCuota) VALUES (%s, %s, %s, %s, %s)"
        valores = (Nombre, Direccion, Telefono, FechaRegistro, EstadoCuota)
        self.db.ejecutar(query, valores)
        return "Usuario registrado con éxito."
    
    def actualizar_usuario(self, Id, Nombre, Direccion, Telefono, FechaRegistro, EstadoCuota):
        query = "UPDATE Usuarios SET Nombre=%s, Direccion=%s, Telefono=%s, FechaRegistro=%s, EstadoCuota=%s WHERE Id=%s"
        valores = (Nombre, Direccion, Telefono, FechaRegistro, EstadoCuota, Id)
        self.db.ejecutar(query, valores)
        return "Usuario actualizado con éxito."
    
    def ver_usuario(self, Id):
        query = "SELECT * FROM Usuarios WHERE Id = %s"
        return self.db.obtener_datos(query, (Id,))
    
    def eliminar_usuario(self, Id):
        query = "DELETE FROM Usuarios WHERE Id = %s"
        self.db.ejecutar(query, (Id,))
        return "Usuario eliminado con éxito."
    
    def ver_usuarios(self):
        query = "SELECT * FROM Usuarios"
        return self.db.obtener_datos(query)
    
    def buscar_usuario_por_nombre(self, Nombre):
        query = "SELECT * FROM Usuarios WHERE (Nombre LIKE %s)"
        valores = (f"%{Nombre}%",)
        return self.db.obtener_datos(query, valores)
    
    def ver_fecha_usuarios(self):
        query = "SELECT FechaRegistro FROM Usuarios WHERE EstadoCuota = 'Impago'"
        return self.db.obtener_datos(query)
    

