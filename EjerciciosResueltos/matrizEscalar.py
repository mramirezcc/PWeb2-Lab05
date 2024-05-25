def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    print(m[i][j])
                    return False
            elif m[i][j] != d:
                print(m[i][j])
                return False
    return True

matriz = [[5, 0, 0], [0, 5, 0], [0, 0, 5]]
print("La matriz: ")
for sub in matriz:
    print(sub)
if(esEscalar(matriz)):
    print("Es escalar")
else:
    print("No es escalar")