print("Ingresa dos números, y te digo cual es el mayor")

while(True):

    a = input();
    b = input();

    if a == b:
        print("Los dos números son iguales, ingresa otros números")
        continue
    elif a > b:
        print("a es mayor que b");
        break
    else:
        print("b es mayor que a")
        break
