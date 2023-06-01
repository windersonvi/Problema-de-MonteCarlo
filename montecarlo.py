import random as r

cont = 0
print ("Ingrese la cantidad de simulaciones a efectuar: ")
simulador = int(input())
for i in range (0,simulador):
    initial = [0,0]
    for h in range(0,10):
        varriaciones = r.randint(0,3) 

        if(varriaciones == 0):
            initial[0] += 1
        elif(varriaciones == 1):
            initial[0] += -1
        elif(varriaciones == 2):
            initial[1] += 1
        else:
            initial[1] += -1
        
    recorrido = sum([abs(x) for x in initial ])
    if(recorrido == 2):
        cont += 1

print(f"De {simulador} simulaciones la probalidad es de: ")
calculos = (cont/simulador)*100
print(calculos)