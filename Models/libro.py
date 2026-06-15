# Clase libro
class libro:

    #Metodo constructor
    def __init__(self, id, titulo, autor, isbn, disponible):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    #Mostrar en la pantalla la informacion de un libro 
    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} : {estado}"



    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro {self.titulo} esta prestado")
            return True
        else:
            print(f"El libro {self.titulo} no esta disponible")
            return False

    def devolver(self):
        self.disponible = True
        print(f"El libro {self.titulo} ha sido devuelto")