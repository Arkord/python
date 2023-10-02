print("Ingresa la cantidad de números que quieres sumar, que sean pares.")

numeros = int(input())
suma = 0

# suponemos que la persona ingresa 2

for n in range(numeros):
    while(True):
        numero = int(input("ingresa un número par: "))

        if numero % 2 == 0:
            suma = suma + numero
            break

print(f"La suma es {suma}")
