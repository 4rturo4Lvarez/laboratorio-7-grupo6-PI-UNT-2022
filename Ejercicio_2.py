#=================================================================#
#   Escriba una función para transformar números arábigos a       #
#   números romanos. El numero ingresado debe ser menor a 4000.   #
#=================================================================#

Número_arábigo=int(input('Ingresar un número arábigo menor a 4000: '))

def conversión_Narábigo_Nromano(arábigo):
    Num_arábigos = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    Num_romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    romano = ''
    i = 0

    while arábigo > 0:
        for n in range(arábigo // Num_arábigos[i]):
            romano += Num_romanos[i]
            arábigo -= Num_arábigos[i]

        i += 1

    return romano

print(f'En números romanos es: {(conversión_Narábigo_Nromano(Número_arábigo))}')
