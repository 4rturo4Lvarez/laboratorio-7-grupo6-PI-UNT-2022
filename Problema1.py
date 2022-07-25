def producto_matrices(m1, m2):
    FILA_MATRIZ1 = len(m1)
    FILA_MATRIZ2 = len(m2)
    COLUMNA_MATRIZ1 = len(m1[0])
    COLUMNA_MATRIZ2 = len(m2[0])
    if COLUMNA_MATRIZ1 != FILA_MATRIZ2:
        return None

    m3 = []
    for indicador_fila in range(FILA_MATRIZ2):
        m3.append([])
        for indicador_columna in range(COLUMNA_MATRIZ2):
            m3[indicador_fila].append(" ")

    for contador_fila in range(COLUMNA_MATRIZ2):
        for indicador_fila in range(FILA_MATRIZ1):
            suma = 0
            for indicador_columna in range(COLUMNA_MATRIZ1):
                suma += m1[indicador_fila][indicador_columna] * m2[indicador_columna][contador_fila]
            m3[indicador_fila][contador_fila] = suma
    return m3


def Mostrar():
    if almacenar:
        print('\nSu matriz resultante es: ')
        for fila in almacenar:
            for valor in fila:
                print(valor, end=" ")
            print("")
    else:
        print("Introduzca otras matrices que se puedan multiplicar")


print('Ingrese el orden de la MATRIZ 1:')
NUMERO_FILA_MATRIZ1 = int(input("\tIntroduce el número de filas: "))
NUMERO_COLUMNA_MATRIZ1 = int(input("\tIntroduce el número de columnas: "))

matriz1 = []
for i in range(NUMERO_FILA_MATRIZ1):
    matriz1.append([0] * NUMERO_COLUMNA_MATRIZ1)

print('\n Ingrese la Matriz 1')
for i in range(NUMERO_FILA_MATRIZ1):
    for j in range(NUMERO_COLUMNA_MATRIZ1):
        matriz1[i][j] = int(input('\t\tElemento (%d,%d): ' % (i, j)))

print('Ingrese el orden de la MATRIZ 2:')
NUMERO_FILA_MATRIZ2 = int(input("\tIntroduce el número de filas: "))
NUMERO_COLUMNA_MATRIZ2 = int(input("\tIntroduce el número de columnas: "))

matriz2 = []
for i in range(NUMERO_FILA_MATRIZ2):
    matriz2.append([0] * NUMERO_COLUMNA_MATRIZ2)


print('\n Ingrese la Matriz 2')
for i in range(NUMERO_FILA_MATRIZ2):
    for j in range(NUMERO_COLUMNA_MATRIZ2):
        matriz2[i][j] = int(input('\t\tElemento (%d,%d): ' % (i, j)))

almacenar = producto_matrices(matriz1, matriz2)
Mostrar()