""" 
" Alcance de las variables.
" Tipo de dato String.
" Los nombres de las variables deben ser significativos.
"  
"""

class variables:
 # self = su alcance es toda la clase.
    # ↓ variable inicializada. texto : str = variable declarada
    texto : str = 'Este es un "texto"' # Si inicias con ' o " debes terminar con lo mismo

    def __init__(self,cadena:str):
        self.cadena = cadena
        self.texto = "Otro texto"

    def contarCaracteres(self,texto:str)-> None:
        # len = la longitud de la variable
        print(len(texto)) # 4
        print(len(self.cadena)) # 5
        print(len(self.texto)) # 10
        print(len(self.otro_texto))

    def caracter(self,posicion:int) -> None:
        print(self.cadena[posicion])

    otro_texto = "MMMMMMM"



mi_objeto = variables("adios")
mi_objeto.contarCaracteres("Hola")
mi_objeto.caracter(3) 