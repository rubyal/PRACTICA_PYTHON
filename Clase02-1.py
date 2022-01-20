# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:30:20 2021

@author: ruby_
"""

a= 10
b= 25
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)



a= "mi nombre es"
b= " Ruby"
print (a+b)




print("c:\algun\nombre")
print(r"C:\algun\nombre")
print("""\
Uso: algo [OPTIONS]
 -h Muestra el mensaje de uso
 -H nombrehost Nombre del host al cual conectarse
""")
3*"un"+"iun"


lista=[1,2,4,5,6,8,10,36,99] ###primer elemento 0
a=3
if (a in lista):
    print("si esta en la lista")
else:
    print("no esta en la lista")
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
##print(lista[0,1,2,3,4,5,6])**

lista=[1,4,9,16,25]
lista+[36,37,89,24] ##concatenar listas (unir)

lista_m=[1,8,27,65,125]
4**3
lista_m[3]=64
lista_m


nombres=["o","a","b","c"]
print(nombres[0])
print(nombres[3])

numeros=[33,55,66,7,8,11]
numeros[4]=2
b=numeros[0]+numeros[1]
numeros
b


lista2=[1,2,3,85,90]
lista3=lista2+[92,60,12,77]
lista3[6]=10
lista4=lista2[3]+lista3[7]
lista3
lista4

85+12


matriz1=[1,2,3,4,5,6]
matriz2=[11,77,88,23,33]
matrizf=[matriz1,matriz2]



a,b=0,1
while b < 10: ##sentencia lo que haya dentro de ella se ejecute mientras sea verdadera
    b+=1	
    print(b) ##identado con tab

a,b=0,1 ##asignación multiple
while b < 10: ##mientras sea tan imprima
        print(b)
        a,b=b,a+b

x=int(input("ingrese un número entero: "))
if x < 0: 
    x=0
    print("negativo cambiado a 0")
elif x==0: ##elfif=else+if
    print("cero")
elif x==1:
    print("simple")
else:
    print("más")
    
    
dias=["lunes","martes","miercoles","jueves","viernes"]  ##index=[0,1,2,3,4]
for d in dias: 
    print(d, len(d))
    if (d == "lunes"): 
        print ("es lunes")
        
for i in range (5): ##range =[0,1,2,3,4]
    print(i)

list=["maria","luis","pedro","juan"]
for i in range (len(list)):
    print(i, list[i])
    
def fib(n): ##def definir una función *palabra reservada (se puede llamar en cualquier momento) """escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
         print(a, end=" ")
         a, b = b, a+b
    print()
    
fib(100)

##funciones lamba (retorna la)

##meses=["enero","febrero","marzo","abril"]


a= 100
b= 2
if a < b :
    print("a es menor que b")
elif a > b:
    print("b es mayor que a")


##pandas (datos) libreria 
##instalacion en la consola --conda install pandas-- pip install pandas--
    
##dos objetos:series y dataframes 
##diccionario 
import pandas as pd
data={
      "manzanas":[3,2,0,1],
      "naranjas":[0,3,7,2]
}

ventas=  pd.DataFrame(data) ##control i pd.DataFrame()



36/4*(3+2)*4+2
var="james bond"
print(var[2::-1])
def calculate (num1,num2=4):
    res=num1*num2
    print(res)
5*6

var="james"*2*3
print(var)
var1=1
var2=2
var3="3"
print(var+var2+var3)











