import random

lista=[]
lista2=[]

for i in range(1,3):
    lista.append(random.randint(1,10))
    a=input("Ingrese 10 números: ")
    #lista2.append(a)

lista2= a.split(",")
print(lista)
print(lista2)