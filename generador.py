import fpdf #pip3 intall fpdf
import random
from itertools import combinations_with_replacement

suma=0
while suma not in [11,17,20]:
    suma=int(input("Cuando tienen que sumar 11 o 17 o 20? "))
filas=0
while filas not in [4,5]:
    filas=int(input("Cuantas filas 4 o 5? "))
columnas=0
while columnas not in [1,2,3,4,5]:
    columnas=int(input("Cuantas columnas (de 1 a 5)? "))
paginas=0
while paginas<1:
    paginas=int(input("Cuantas páginas? "))

def generar_combinaciones(val,filas,total):
    if val!=[] and len(val[0])==filas:
        return list(filter(lambda x: sum(x) == total, val))
    newval=[]
    for num in range(0,10):
        if val==[]:
            newval.append([num])
        else:
            for cad in val:
                newval.append(cad+[num])
    return generar_combinaciones(newval,filas,total)

# Generar las combinaciones posibles
valores=generar_combinaciones([],filas-1,suma)

minmax={11:[0,7],17:[2,9],20:[0,7]} # minimos y maximos del numero aleatorio
tamfuente={4:145,5:135} # tamaño de la fuente
# calculamos las posiciones de las columnas dentro de la hojas
pdf = fpdf.FPDF(orientation='L') #pdf format
pdf.add_font('Franklin', '', r"Franklin Gothic Heavy Regular.ttf", uni=True)
pdf.set_font("Franklin", size=tamfuente[filas]) # font and textsize
anchohoja=pdf.w-10 # descuento 10 de margen por cada lado
altohoja=pdf.h-20 # descuento 10 de margen por cada lado

poscol=[10]
while (len(poscol)<columnas):
    poscol.append(poscol[-1]+anchohoja/columnas)

# calculamos las posiciones de las filas dentro de la hojas
posfila=[20]
while (len(posfila)<filas):
    posfila.append(posfila[-1]+altohoja/filas)



for a in range(0,paginas):
    pdf.add_page() #create new page
    for columna in range(0,columnas):
        numeros=random.choice(valores).copy()
        numeros.insert(filas-2,random.randint(minmax[suma][0],minmax[suma][1]))
        for fila in range(0,filas):
            pdf.set_xy(poscol[columna], posfila[fila])
            pdf.cell(anchohoja/columnas, 17, txt=str(numeros[fila]), ln=0, align="C",border=0)
archivo="Lightning_Addition_suma{}_{}x{}_{}paginas.pdf".format(suma,columnas,filas,paginas)
pdf.output(archivo)
print("Generado archivo:",archivo)