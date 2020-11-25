n = int(input("Ingrese un número para comenzar la cuenta\n"))
i = 0
suma_pares=0
while i <=n:
    if i%2 ==0:
        suma_pares = suma_pares + i
    else:
        i = i
    i+=1

print(suma_pares)