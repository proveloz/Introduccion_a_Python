import sys

#lista_valores=sys.argv[1:]

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

def filter(diccionario,valor):
    diccionario2={}
    for key,values in diccionario.items():
        if values >=valor:
            diccionario2[key] = values
    return (diccionario2)

print(filter(ventas,70000))
 