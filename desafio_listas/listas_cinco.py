import velocidad as v
auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]
autos=[auto1,auto2,auto3,auto4,auto5,auto6]

def vel_autos(lista):
    #global autos
    vel_autos=[]
    for i in lista:
        #vel_autos.append(autos[i][1])
        x=lista.index(i)
        vel_autos.append(lista[x][1])
    return vel_autos

vp = v.promedio(vel_autos(autos))
var_vel_autos=vel_autos(autos)
def filtro_vel_mayor_prom(velocidades):
    global vp
    mayores_vel_promedio=[]
    mayores_vel_promedio = filter(lambda x: x>vp , velocidades)
    return mayores_vel_promedio

print(list(filtro_vel_mayor_prom(var_vel_autos)))
#list(filtro_vel_mayor_prom(var_vel_autos)