import time
tiempo_Inicio = time.time()

numero = int(input('Ingrese la posición: '))

a1 = 0
a2 = 1
print(a1)
print(a2)

for i in range(numero-2):
    a3 = a1 + a2
    print(a3)
    a1 = a2
    a2 = a3

tiempo_Final = time.time()
tiempo = tiempo_Final-tiempo_Inicio
print(tiempo)