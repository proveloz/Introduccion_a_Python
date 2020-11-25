def letra_o(n):
        letra1=""
        letra2=""
        #letra3=""
        #letra4=""
        a=""
        j=0
        for i in range(n):
                letra1+="*"
               # if i==(n-1):
             #           letra1+="\n"
        for i in range(n):
                if i==0 or i==(n-1):
                        letra2+="*"
                else:
                        letra2+=" "     
        a=letra1+"\n"+(letra2+"\n")*(n-2)+letra1
        print(a)
        return(a)
        
letra_o(5)