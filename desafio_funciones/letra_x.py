def  letra_x(n):
        letra1=""
        letras=[]
        letras2=[]
        letras3=[]
        for j in range(n):
                for i in range(n):
                        if i == j:
                                letra1+="*"
                                letras.append(letra1)
                                print(letra1)
        print(letras)
        for i in range(n):
                if i>0:
                        letras2.append(letras[i].replace("*"," ",i))
        letras2.insert(0,"*")
        print(letras2)
        for i in reversed(letras2):
                letras3.append(i)
        print(letras3)
        a=letras2[0]+letras3[1]+"\n"+letras2[1]+letras3[3]+"\n"+letras2[2]+"\n"+letras3[3]+letras2[1]+"\n"+letras3[4]+letras2[3]
        print(a)
        return(a)
letra_x(5)