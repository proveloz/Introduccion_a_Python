velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
11, 11, 12, 12, 12, 12, 13, 13,
13, 13, 14, 14, 14, 14, 15, 15,
15, 16, 16, 17, 17, 17, 18, 18,
18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
17, 28, 14, 20, 24, 28, 26, 34, 34,
46, 26, 36, 60, 80, 20, 26, 54, 32,
40, 32, 40, 50, 42, 56, 76, 84, 36,
46, 68, 32, 48, 52, 56, 64, 66, 54,
70, 92, 93, 120, 85]

lista_vel_dis= zip(velocidad,distancia)

cont_vel_baja=0
cont_velbaja_dist_sobre=0
cont_vel_sobre=0
cont_velsobre_dist_bajo=0

def promedio(lista):
    a = len(lista)
    suma=0
    for i in lista:
        suma+=i
    promedio=suma/a
    return promedio

vp=promedio(velocidad)
dp=promedio(distancia)

for x,y in zip(velocidad,distancia):
    if x<vp:
        cont_vel_baja+=1
    if x<vp and y > dp:
        cont_velbaja_dist_sobre+=1
    if x>vp:
        cont_vel_sobre+=1
    if x>vp and y < dp:
        cont_velsobre_dist_bajo+=1
    else:
        pass
print(cont_vel_baja)
print(cont_velbaja_dist_sobre)
print(cont_vel_sobre)
print(cont_velsobre_dist_bajo)
#lista_vel_dis = set(lista_vel_dis)
#print(lista_vel_dis[0][0])
#print(lista_vel_dis)