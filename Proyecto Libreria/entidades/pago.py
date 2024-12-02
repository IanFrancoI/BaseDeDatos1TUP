from conexion import BaseDeDatos

class Pago:
    def __init__(self, db):
        self.db = db

    def registrar_pago(self, UsuarioId, FechaPago, Monto):
        query = "INSERT INTO Pagos (UsuarioId, FechaPago, Monto) VALUES (%s, %s, %s)"
        valores = (UsuarioId, FechaPago, Monto)
        self.db.ejecutar(query, valores)
        return "Pago registrado con éxito."
    
    def actualizar_pago(self, Id, UsuarioId, FechaPago, Monto):
        query = "UPDATE Pagos SET UsuarioId=%s, FechaPago=%s, Monto=%s WHERE Id=%s"
        valores = (UsuarioId, FechaPago, Monto, Id)
        self.db.ejecutar(query, valores)
        return "Pago actualizado con éxito."
    
    def ver_pago(self, Id):
        query = "SELECT * FROM Pagos WHERE Id = %s"
        return self.db.obtener_datos(query, (Id,))
    
    def eliminar_pago(self, Id):
        query = "DELETE FROM Pagos WHERE Id = %s"
        self.db.ejecutar(query, (Id,))
        return "Pago eliminado con éxito."
    
    def ver_pagos(self):
        query = "SELECT * FROM Pagos"
        return self.db.obtener_datos(query)