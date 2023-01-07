import random

def desordenar():
    L=[1,2,3,4,5]
    for i in range(len(L)):
        indiceAzar = random.randint(0, len(L)-1)
        L[i], L[indiceAzar] = L[indiceAzar], L[i]
    print(L)
    
desordenar()
