print("Estructuras de 2 dimensiones")

lista = ["Ajo molido", "Sal", "Pimienta"]
cantidadGramos = [100, 200, 50]

listaResultante = []
listaResultante.append(lista)
listaResultante.append(cantidadGramos)

for elemento in zip(lista, cantidadGramos):
    print(elemento)