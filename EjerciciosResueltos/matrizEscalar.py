def esEscalar(m):
    try:
        d = m[0][0]
        for i in range(len(m)):
            for j in range(len(m)):
                if i != j:
                    if m[i][j] != 0:
                        print("Elemento incongruente: " + str(m[i][j]))
                        return False
                elif m[i][j] != d:
                    print("Elemento incongruente:" + str(m[i][j]))
                    return False
    except IndexError:
        print("Las dimensiones de la matriz no son correctas")
        return False
    return True

matriz = [[5, 0, 0], [0, 5], [0, 0, 5]]
for sub in matriz:
    print(sub)
if(esEscalar(matriz)):
    print("La matriz es escalar")
else:
    print("La matriz no es escalar")