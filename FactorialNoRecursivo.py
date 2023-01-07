import time 
tiempo_Inicio = time.time()

x=1
n = int(input('Ingrese el dato que quieres saber el factorial:'))
for i in range(1,n+1):
    if n == 0:
        x = 1
    elif n>0:
        x = x*i
    
print(f'el factorial de {n}! es: {x}')

tiempo_Final = time.time()
tiempo = tiempo_Final-tiempo_Inicio
print(tiempo)