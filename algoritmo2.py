print("Ingresa la cantidad de números que quieres sumar, deben ser pares")

numeros = int(input())
suma = 0

for n in range(numeros):
    while(True):
        numero = int(input("Ingresa un número par: "))
        if numero % 2 == 0:
            suma = suma + numero
            break;
print(f"La suma es {suma}")