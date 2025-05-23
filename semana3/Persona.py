class Persona:

    # Atributos
    nombre : str
    edad : int
    sexo : str

    # Constructor
    def __init__(self, nombre:str,edad:int,sexo:str)-> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    # Metodos
    def decirMensaje(self, mensaje:str) -> None:
        print(f"{self.nombre} : {mensaje}")

    def informacion(self) ->None:
        print(f"Nombre : {self.nombre}")
        print(f"Edad : {self.edad}")
        print(f"sexo : {self.sexo}")

    def correr(self, velocidad:float) -> None:
        print(f"Corre a {velocidad} km/h")


# Objetos de tipo Persona
dejah = Persona("Dejah Thoris",20,"F")
john = Persona("john Carter",23,"M")

dejah.informacion()
john.informacion()

dejah.decirMensaje("Buen dia")
john.decirMensaje("Mucho gusto")

dejah.correr(9)
john.correr(11)