
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

#for i in range(len(ventas)):

quarters={}

suma_q1=0
suma_q2=0
suma_q3=0
suma_q4=0

for k,v in ventas.items():
    if k=="Enero" or k=="Febrero" or k=="Marzo":
        suma_q1+=v
        quarters["Q1"]=suma_q1
    elif k=="Abril" or k=="Mayo" or k=="Junio":
        suma_q2+=v
        quarters["Q2"]=suma_q2
    elif k=="Julio" or k=="Agosto" or k=="Septiembre":
        suma_q3+=v
        quarters["Q3"]=suma_q3
    else:
        suma_q4+=v
        quarters["Q4"]=suma_q4
        
print(quarters) 