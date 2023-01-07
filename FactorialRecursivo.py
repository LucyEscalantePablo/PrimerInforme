import time
tiempo_Inicio = time.time()

numero = int(input('Ingrese el número: '))
def factorial(numero):
    if numero==0:
        return 1
    else:
        return numero*factorial(numero-1)
resultado = factorial(numero)   
print(f'el factorial de {numero}! es: {resultado}')
tiempo_Final = time.time()
tiempo = tiempo_Final - tiempo_Inicio
print(tiempo)