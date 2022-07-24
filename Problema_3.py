#==================================================================================
# Escribir una función que dada una matriz de números enteros y un número objetivo,
# retorne los indices de los 2 números que sumen ese numero objetivo. Asuma que
# habrá una solución valida en el array y no se puede usar el elemento del array 2
# veces.
#==================================================================================

def f_matriz(matriz, n_objetivo):
    
    cant = len(matriz)
    
    for i in range(cant - 1):
        
        j = i + 1
        
        for j in range(cant):
            # Realiza un recorrido de dos datos en toda la matriz
            
            suma = matriz[i] + matriz[j]
            # Suma los datos de cada recorrido
            
            if suma == n_objetivo:
                
                return(i,j)
                # Retorna los índices
            
                break
#==================================================================================

matriz_numeros = []
    # Crea la lista numeros

cantidad = int(input("Ingrese la cantidad de números a evaluar: "))
    
for i in range(cantidad):
        
    print(f"Ingrese el número de la posición {i}:")
    
    matriz_numeros.append(int(input("---> ")))
    # Guarda los datos dentro de la lista numeros

numero_objetivo = int(input("Ingrese el número objetivo: "))

i_1, i_2 = f_matriz(matriz_numeros, numero_objetivo)

print("\n"f"Los dos índices donde se encuentran los números cuya suma es igual al número objetivo, son: [{i_1}, {i_2}]")