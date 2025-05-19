class Calculadora:

    def __init__(self):
        print("Constructor")

    def sumar(self, numero1, numero2):
        # Recibe 2 valores, los suma y los almacena en resultado.
        resultado = numero1 + numero2
        # Imprime el texto Resultado y el valor de la variable resultado.
        print(f"Resultado: {resultado}")
        
        # Imprime el texto Resultado y el valor de la variable resultado.
        # Convierte el tipo de dato a string.
        print("Resultado: " + str(resultado))


# Crea una instancia de la clase Calculadora, es decir crea un objeto.
mi_objeto = Calculadora()

# Invoca el metodo sumar y le envia 2 numeros.
mi_objeto.sumar(10,8)

# Invoca el metodo sumar y le envia 2 cadenas.
mi_objeto.sumar("Hola","Adios")
