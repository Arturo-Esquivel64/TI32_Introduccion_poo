class Mayor_de_3:
    
    def __init__(self):
        pass
    
    def mayor(self, numero1:int, numero2:int, numero3:int)->None:
        pass
        if numero1>numero2:
        
            if numero1>numero3:
                print(numero1)

            elif numero2>numero3:
                print(numero2)

            else:
                print(numero3)

        elif numero2>numero3:
            print(numero2)

        else:
            print(numero3)

    



mi_objeto = Mayor_de_3()
mi_objeto.mayor(1,2,3)
mi_objeto.mayor(1,4,2)
mi_objeto.mayor(5,1,2)
mi_objeto.mayor(6,1,1)
mi_objeto.mayor(1,1,7)
mi_objeto.mayor(1,8,1)
mi_objeto.mayor(9,9,1)
mi_objeto.mayor(10,1,10)
mi_objeto.mayor(1,11,11)
mi_objeto.mayor(12,12,12)