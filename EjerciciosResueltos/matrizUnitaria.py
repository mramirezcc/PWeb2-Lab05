from matrizEscalar import esEscalar
def esUnitaria(m):
    return esEscalar(m) and m[0][0] == 1

matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
for sub in matriz:
    print(sub)
if(esUnitaria(matriz)):
    print("La matriz es unitaria")
else:
    print("La matriz no es unitaria")
