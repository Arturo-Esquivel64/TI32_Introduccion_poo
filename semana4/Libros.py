class Libros:
    autor : str
    titulo : str
    isbn : str
    disponible : bool

    def __init__(self, autor:str, titulo:str, isbn:str)-> None:
        
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn
        self.disponible = True
    
    def prestar(self)-> None:
        if self.disponible == True:
            print("Libro Prestado")
            self.disponible = False
        else:
            print("No disponible")
    
    def devolver (self)-> None:
        self.disponible=True

    def informacionLibro(self)-> None:
        print(f"Autor: {self.autor}")
        print(f"Titulo: {self.titulo}")
        print(f"Isbn: {self.isbn}")
        print(f"Estado: {self.disponible}")

libro1 = Libros ("Franz Kafka","Carta al padre","2141307011141")
libro1.prestar()
libro1.informacionLibro()
