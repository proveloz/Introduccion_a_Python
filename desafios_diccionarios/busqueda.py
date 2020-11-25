import sys

lista_valores=sys.argv[1:]
l=[]
k=0
for i in lista_valores:
    k=int(i)
    l.append(k)
#print(l)
ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}


k=list(ventas.items())
for valor in l:
    i=0
    cont=0
    while i<len(k):
        if k[i][1] == valor:
            print(k[i][0])
            cont+=1
        i+=1
    if cont==0:
        print("no encontrado")
       