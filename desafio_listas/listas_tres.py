import velocidad as v
auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]
autos=[auto1,auto2,auto3,auto4,auto5,auto6]
vel_autos=[]

    
for i in range(len(autos)):
    vel_autos.append(autos[i][1])
    #print(autos[i][1])

promedio_vel =v.promedio(vel_autos)
autos_vel_mayores_media=[]
for item in autos:
    x=autos.index(item)
    if promedio_vel < autos[x][1]:
        #autos_vel_mayores_media.append(item)
        print(item)
    else:
        pass
#print(autos_vel_mayores_media)
