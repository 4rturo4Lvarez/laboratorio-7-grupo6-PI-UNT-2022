#===================================================================================
# Realice una función que dado un entero x, retorne True si el numero es un
# palisandro. Un numero palisandro es aquel que se lee igual de izquierda a derecha
# que de derecha a izquierda.
#===================================================================================

def f_palisandro(num):
    
    lista_num = [digito for digito in str(num)]
    # Convierte cada dígito del entero a un dato de lista 
    
    lista_num_invertida = list(reversed(lista_num))
    # Invierte el orden de la lista
    
    if lista_num == lista_num_invertida:
        return(True)
    else:
        return(False)
#===================================================================================

numero = int(input("Ingrese el número a evaluar: "))

if f_palisandro(numero) == True:
    print("El número ingresado es un palisandro.")
else:
    print("El número ingresado no es un palisandro.")