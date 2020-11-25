import pandas as pd

df= pd.read_csv("athlete_events.csv")  


######### EJERCICIO 1 ##################
ejercicio_1 = df.shape
#print(ejercicio1)
########################################

######### EJERCICIO 2 ##################
ejercicio_2 = len(df["Games"].value_counts())
print(ejercicio_2)
########################################

######### EJERCICIO 3 ##################
ejercicio_3 = df["Season"].value_counts()/len(df)
#print(ejercicio3)
########################################

######### EJERCICIO 4 ##################
#df_year = df["Year"].min()
#df_year= df["Year"].min()
ej4_c=df[df["Season"]=="Summer"]
minimo_summer= ej4_c.Year.min()
ejercicio_4= ej4_c[ej4_c["Year"]==minimo_summer]["City"].unique()
print(ejercicio_4)
#ejercicio_4a=ejercicio_4.loc[:,["Year","Season","City"]].head(1)
#ejercicio_4a=df[df["Year"]==df_year]["City"].unique()
#print(ejercicio_4)
#ej4=df['Year'].unique().min()
#ejercicio_4=df.loc[(df["Year"]==ej4) & (df["Season"]=="Summer"),["City"]].drop_duplicates()
#print(ejercicio_4)
########################################
######### EJERCICIO 5 ##################
ej5_c=df[df["Season"]=="Winter"]
minimo_winter= ej5_c.Year.min()
ejercicio_5= ej5_c[ej5_c["Year"]==minimo_winter]["City"].unique()
#print(minimo_winter)
print(ejercicio_5)
########################################

######### EJERCICIO 6 ##################
ejercicio_6=pd.value_counts(df["Team"]).head(10)
#print(ejercicio_6)

#f_Team = df[df["Team"]==]

########################################

######### EJERCICIO 7 ##################
ejercicio_7 = df["Medal"].value_counts("%")
#print(ejercicio_7)
#f_Team = df[df["Team"]==]

########################################
######### EJERCICIO 8 ##################
ej8_c=df[df["Season"]=="Summer"]
minimo_verano= ej8_c.Year.min()
ejercicio_8= ej8_c[ej8_c["Year"]==minimo_verano]["NOC"].unique()
#print(minimo_verano)
print(ejercicio_8)
