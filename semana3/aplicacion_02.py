class Calculadora:

    def __init__(self):
        # Indica que paso por esta linea y que se ejecute la siguiente.
        pass

    def sumar(self, numero1, numero2):
        # Recibe 2 valores, los suma y los almacena en resultados.
        resultado = numero1 + numero2
        # Imprime el texto Resultado y el valor de la variable resultado.
        print(f"Resultado suma: {resultado}")

    def resta(self, numero1, numero2):
        # Recibe 2 valores, los resta y los almacena en resultados.
        resultado = numero1 - numero2
        # Imprime el texto Resultado y el valor de la variable resultado.
        return resultado

    def multiplicar(self, numero1, numero2):
        # Recibe 2 valores, los multiplica y los almacena en resultados.
        resultado = numero1 * numero2
        # Imprime el texto Resultado y el valor de la variable resultado.
        print(f"Resultado multiplicacion: {resultado}")

    def dividir(self, numero1, numero2):
        # Recibe 2 valores, los divide y los almacena en resultados.
        try:
            resultado = numero1 / numero2
            # Imprime el texto Resultado y el valor de la variable resultado.
            return resultado
        except ZeroDivisionError as error:
            print(f"Error 001: {error.args[0]}")
        except  TypeError as error:
            print(f"Error 002: {error.args[0]}")
        except Exception as error:
            # Guarda todo tipo de errores.
            print(f"Error 003: {error.args[0]}")

mi_objeto = Calculadora()
mi_objeto.sumar(10,5)
print(f"Resultado resta: {mi_objeto.resta(10,5)}")
mi_objeto.multiplicar(10,5)
print(f"Resultado dividir: {mi_objeto.dividir(10,5)}")
print(f"Resultado dividir2: {mi_objeto.dividir(numero2=0, numero1=10)}")
print(f"Resultado dividir2: {mi_objeto.dividir(numero2="Hola", numero1=10)}")
