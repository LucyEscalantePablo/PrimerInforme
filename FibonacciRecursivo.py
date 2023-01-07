import time
tiempo_Inicio = time.time()

def fibonacci(n):
    if n < 2:
        return n
    else: 
        return (fibonacci(n-1)+fibonacci(n-2))

tiempo_Final = time.time()
tiempo = tiempo_Final-tiempo_Inicio
print(tiempo)  