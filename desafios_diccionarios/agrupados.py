from collections import OrderedDict, Counter 

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
lista_valores=ventas.values()
cnt = Counter(lista_valores)  
od = OrderedDict(cnt.most_common())
diccionario3={}  
for key, value in od.items():  
    diccionario3[key]=value

print(diccionario3)