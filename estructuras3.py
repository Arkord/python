print("Listas de dos dimensiones o matrices")

matriz =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print(matriz)

for lista in matriz:
    #print(lista)
    for elemento in lista:
        print(elemento)

print("Acceder por x,y o fila columna: ")
print(matriz[1][1])