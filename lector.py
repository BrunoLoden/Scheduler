
import pandas as pd
import SM_v1 as c


#-----------------------Esquema de Horario-----------------------------------
df_horario = pd.read_excel("Horario.xlsx","Hoja1", header=2 )
#print(df_horario)
#----------------------------------------------------------------------------

#--------------------------Diccionario para horas----------------------------
df_hora = pd.read_excel("Horario.xlsx","Horas")
list_hora = df_hora["Hora"].tolist()
list_per = df_hora["Periodo"].tolist()
zip_dem =zip(list_hora,list_per)
#--Diccionario---
Horas= dict(zip_dem)
#----------------------------------------------------------------------------

#---------------------------Separa cursoss----------------------------------
df_cursos = pd.read_excel("Horario.xlsx","Cursos")
for columna in df_cursos:
    print("===============Curso: ",columna,"=======================")
    lista = df_cursos[columna].tolist()
    print("-------",len(lista))
    l_clases = []
    l_clase = []    
    for i in range(0,len(lista)-8,7):
        print("-----------Iteracion - Clase",i/7,"--------------")
        l_clase.append(lista[i])
        l_clase.append(lista[i+1])
        l_clase.append(lista[i+2])
        l_clase.append(lista[i+3])
        l_clase.append(lista[i+4])
        l_clase.append(lista[i+5])
        l_clase.append(lista[i+6])
        print(l_clase)
        c = c.clase(lista[i],lista[i+1],lista[i+2],lista[i+3],lista[i+4],lista[i+5][0:2],lista[i+5][6:8],lista[i+6])
        l_clases.append(c)
        l_clase = []
        print("------------------------------------------------")
    

#print(clase)
print(l_clases)
#print(df_cursos)
