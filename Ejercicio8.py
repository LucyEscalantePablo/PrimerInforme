'''
potencia = 1
for i in range(1,exponente+1):
    potencia = potencia*base

print(potencia)
'''
base = int(input('base: '))
exponente = int(input('esponente: '))

def potencial (base, exponente):
    if exponente == 0:
        return 1
    else:
        return base* potencial(base, exponente-1)

resul = potencial(base,exponente)
print(resul)