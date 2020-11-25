import string
contrasena = input("Ingresa contraseña: ")
letras="abcdefghijklmnopqrstuvwxyz"
i = 0
j = 0
intento=0
while i < len(letras):
    
    if letras[i]==(contrasena[j]).lower():
        j = j+1
        i = 0
        intento+=1
        if j == len(contrasena):
            break
    else:
        i = i+1
        intento+=1

print(str(intento)+" intentos")