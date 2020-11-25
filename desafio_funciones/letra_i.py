def letra_i(n):
        letra1=""
        letra2=""
        a=""
        for i in range(n):
                letra1+="*"
        for i in range(n):
                if   i == (((n-1)*0.5)):
                        letra2+="*"
                else:
                        letra2+=" "
        
        print(letra1+"\n"+(letra2+"\n")*(n-2)+letra1)
        a=letra1+"\n"+(letra2+"\n")*(n-2)+letra1
        return(a)
letra_i(5)
