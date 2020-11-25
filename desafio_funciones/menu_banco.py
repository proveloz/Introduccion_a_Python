import sys
import random

saldo = 0
def consultar():
    return saldo

def depositar(s,cantidad):
    global saldo
    saldo+= cantidad
    return saldo

def girar(s,c):
    global saldo
    #if saldo is 0:
    saldo-=c
    return saldo

def mostrar_menu():
    print("Bienvenido al portal del Banco Amigo. Escoja una opcion")
    print("1.Consultar Saldo")
    print("2.Hacer deposito")
    print("3.Realizar giro")
    print("4.Salir\n")

def validar_menu(opcion):
    while opcion != "1" and opcion != "2" and opcion != "3"and opcion != "4" : 
        print("Opcion inválida: Por favor ingrese 1, 2 , 3 o 4.")
        opcion = input("")
    else:
        pass

while True:
    mostrar_menu()
    opc = input("")
    validar_menu(opc)
    if opc == "1":
        print (consultar())
    elif opc == "2":
        s=int(consultar())
        cant = int (input(""))
        print (depositar(s,cant))
    elif opc == "3":
        s=int(consultar())
        c = int(input(""))
        g=False
        if s == 0:
            print ("No puede realizar giros. Su saldo es 0")
        elif s > 0:
            while g == False:
                if s>=c:
                    girar(s,c)
                    print (consultar())
                    g = True
                else: 
                    print("No se puede girar esta cantidad.Su saldo es de "+str(saldo))
                    c = int(input(""))
                    g = False
                
    elif opc == "4":
        sys.exit()
        
