
from filecmp import clear_cache
import pandas as pd
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

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#Clase: Horario de una lcase (3 horas a los max)
class clase:
    def __init__(self,cod,nom,seccion,tipo,dia,hora_i,hora_f,profesor):
        self.cod = cod
        self.nom = nom
        self.sec = seccion
        self.tip = tipo
        self.dia = dia
        self.hoi = hora_i
        self.hof = hora_f
        self.prf = profesor

    def __str__(self):
        t = str(self.cod)+"-"+str(self.sec)+" "+str(self.prf)  
        return t
        
  #c1 = clase("BIC01","INTRODUCCIÓN A LA COMPUTACIÓN", "M","T","LU","14.0","16.0","ROJAS")

#Curso: Conjunto de horario de clase
class curso:
    def __init__(self,cls1,cls2,cls3,cls4):
        self.cls1 = cls1
        self.cls2 = cls2
        self.cls3 = cls3
        self.cls4 = cls4

    def editar(self):
        print("Hora de inicio: ",self.cls1.hoi)
        print("Hora de fin: ",self.cls1.hof)
        print("----------------")
        print("Hubibcacion inicio: ",Horas[float(self.cls1.hoi)])
        print("Hubicacion fin: ",Horas[float(self.cls1.hof)])
        print("----------------")
        df_horario.loc[ Horas[float(self.cls1.hoi)-0.5] :Horas[float(self.cls1.hof)], str(self.cls1.dia)] = self.cls1
        df_horario.loc[ Horas[float(self.cls2.hoi)-0.5] :Horas[float(self.cls2.hof)], str(self.cls2.dia)] = self.cls2
        df_horario.loc[ Horas[float(self.cls3.hoi)-0.5] :Horas[float(self.cls3.hof)], str(self.cls3.dia)] = self.cls3
        df_horario.loc[ Horas[float(self.cls4.hoi)-0.5] :Horas[float(self.cls4.hof)], str(self.cls4.dia)] = self.cls4



#print(c1)

# cur1 = curso(c1,c1,c1,c1)
# cur1.editar()


#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

#---------------------------Separa cursos----------------------------------
df_cursos = pd.read_excel("Horario.xlsx","Cursos")
for columna in df_cursos:
    print("===============Curso: ",columna,"=======================")
    lista = df_cursos[columna].tolist()
    print("-------",len(lista))
    l_clases = []
    l_clase = []    
    for i in range(0,len(lista)-8,7):
        print("-----------Iteracion - Clase",i/7,"--------------")
        nom = lista[i+6][0:lista[i+6].find(" ")+1]
        c = clase(lista[i],lista[i+1],lista[i+2],lista[i+3],lista[i+4],lista[i+5][0:2],lista[i+5][6:8],nom)
        print(c)
        l_clases.append(c)
        print("------------------------------------------------")
        print(c.cod)
        print(c.sec)
        print(c.tip)
        print(c.dia)
        print(c.hoi)
        print(c.hof)
        print(c.prf)
        print("------------------------------------------------")

print("-----------------")
#print(clase)
print(type(l_clases))
#print(df_cursos)
print(len(l_clases))
print("-----------------")

cur1 = curso(l_clases[0],l_clases[1],l_clases[2],l_clases[3])
cur1.editar()
print(df_horario)