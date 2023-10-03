def imprimir(lista):
    print("Estas son las frutas que tienes en tu canasta: ")
    for item in lista:
       print(item)

lista = ["plátano", "naranja", "manzana", "limón", "guayaba"]

seguir = "SI";

while  seguir.upper() == "SI":
    print("Bienvenido a la frutería Don Carlos, selecciona una opción:\n")

    fruta = input("Ingresa una nueva fruta: ")
    lista.append(fruta)

    imprimir(lista)

    seguir = input("¿Seguir? ").upper()

