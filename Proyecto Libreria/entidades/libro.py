from conexion import BaseDeDatos

class Libro:
    def __init__(self, db):
        self.db = db
   
    def registrar_libro(self,Titulo, Autor, Anio, Categoria, Estado):
        query = "INSERT INTO Libros (Titulo, Autor, Anio, Categoria, Estado) VALUES (%s, %s, %s, %s, %s)"
        valores = (Titulo, Autor, Anio, Categoria, Estado)
        self.db.ejecutar(query, valores)
        return "Libro registrado con éxito."
    
    def actualizar_libro(self, Id, Titulo, Autor, Anio, Categoria, Estado):
        query = "UPDATE Libros SET Titulo=%s, Autor=%s, Anio=%s, Categoria=%s, Estado=%s WHERE Id=%s"
        valores = (Titulo, Autor, Anio, Categoria, Estado, Id)
        self.db.ejecutar(query, valores)
        return "Libro actualizado con éxito."
    
    def ver_libro(self, Id):
        query = "SELECT * FROM Libros WHERE Id = %s"
        return self.db.obtener_datos(query, (Id,))
    
    
    def eliminar_libro(self, Id):
        query = "DELETE FROM Libros WHERE Id = %s"
        self.db.ejecutar(query, (Id,))
        return "Libro eliminado con éxito."
    
    def ver_libros(self):
        query = "SELECT * FROM Libros"
        return self.db.obtener_datos(query)
    
    
    def buscar_libro_por_titulo(self, Titulo):
        query = "SELECT * FROM Libros WHERE (Titulo LIKE %s)"
        valores = (f"%{Titulo}%",)
        return self.db.obtener_datos(query, valores)
    
    def buscar_libro_por_autor(self, autor):
        query = "SELECT * FROM Libros WHERE (Autor LIKE %s)"
        valores = (f"%{autor}%",)
        return self.db.obtener_datos(query, valores)
    
