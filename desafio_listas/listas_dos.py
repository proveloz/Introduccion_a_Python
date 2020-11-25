import velocidad as v
auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]
autos=[auto1,auto2,auto3,auto4,auto5,auto6]



def datos_numericos(lista):
    lista_num_autos1=[]
    lista_num_autos2=[]
    lista_num_autos3=[]
    for i in range(len(autos)):
        lista_num_autos1.append(autos[i][1])
        lista_num_autos2.append(autos[i][2])
        lista_num_autos3.append(autos[i][4])
    return lista_num_autos1,lista_num_autos2,lista_num_autos3

a,b,c = datos_numericos(autos)
x=v.promedio(a)
y=v.promedio(b)
z=v.promedio(c)
print(x)
print(y)
print(z)