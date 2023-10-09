def sumar_elementos(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento

    return suma

listaNumeros = [10, 2, 1]

print(f"La suma de los elementos es : {sumar_elementos(listaNumeros)}")