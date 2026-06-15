#DAO : Data Access Object
#Es una clase que se encarga de acceder 
# a la base de datos y realizar las operaciones

from DataBase.conexion import Conexion
from Models.libro import libro

class LibroDAO:

    # Select * from libros
    def obtener_libros(self):
        Conexion = Conexion.obtener_conexion()
        cursor = Conexion.cursor()

        # Ejecuta la consulta
        cursor.execute("SELECT * FROM libros")
        # Obtiene los resultados
        registros = cursor.fetchall()

        # Crear una lista de clase libro 
        libros = []
        for registro in registros:
            libro = libro(
                id=registro[0],
                titulo=registro[1],
                autor=registro[2],
                isbn=registro[3],
                disponible=registro[4]
            )
            libros.append(libro)
        # Cerrar la conexion
        cursor.close()
        Conexion.close()
        return libros
    
    # Insert
    def insertar(self, libro):
        Conexion = Conexion.obtener_conexion()
        cursor = Conexion.cursor()

        sql = """
        INSERT INTO libro(titulo, autor, isbn, disponible)
        VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(sql,(
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible
        ))

        Conexion.commit()
        cursor.close()
        Conexion.close()


    def actualizar(self, libro):
        Conexion = Conexion.obtener_conexion()
        cursor = Conexion.cursor()

        sql = """
                 UPDATE libro
                 SET titulo = %s, autor=%x,
                 isbn = %s, disponible = %s
                 WHERE id = %s
        """

        cursor.execute(sql, (
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible,
            libro.id
        ))

        Conexion.commit()
        cursor.close()
        Conexion.close()

    def elimiar(self, id):
        Conexion = Conexion.obtener_conexion()
        cursor = Conexion.cursor()

        cursor.execute("DELETE FROM libro WHERE id = %s",
            (id))
        Conexion.commit()
        cursor.close()
        Conexion.close()



