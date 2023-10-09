print("Diccionarios")

diccionario = {}
diccionario.update({"ajo en polvo": 100})
diccionario.update({"pimienta molida": 200})

# print(diccionario)

for elemento in diccionario:
    print(elemento)
    print(f"Valor: {diccionario[elemento]}")