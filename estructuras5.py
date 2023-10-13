print("Diccionarios")

diccionario = {}
diccionario.update({"ajo en polvo": 100})
diccionario.update({"pimienta molida": 200})
diccionario.update({
    "lista": ["item1", "item2", "item3"]
})

diccionario["pimienta molida"] = 500

# diccionario.popitem()
# diccionario.items
# print(diccionario["pimienta molida"])
# diccionario.get("pimienta molida")
# diccionario.popitem()
# diccionario.pop("lista")

print(diccionario.values())
print(diccionario.keys())
print(diccionario.items())

# for elemento in diccionario:
#     print(elemento)
#     print(f"Valor: {diccionario[elemento]}")