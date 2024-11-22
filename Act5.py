matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def suma_filas(mat):
    matFin = []
    for i in range (len(mat)):
        for j in range (len(mat[i])):
            num = mat[i][0] + mat[i][1] + mat[i][2]
        matFin.append(num)
    return matFin
            
            
def suma_columnas(mat):
    matFin = []
    for i in range (len(mat)):
        for j in range (len(mat[i])):
            num = mat[0][i] + mat[1][i] + mat[2][i]
        matFin.append(num)
    return matFin        
            
def transpuesta(mat):
    matFin = []
    for i in range (len(mat)):
        for j in range (len(mat[i])):
            matFin.append([mat[0][j],mat[1][j],mat[2][j]])

        return matFin
            
print(suma_filas(matriz))
print(suma_columnas(matriz))
print(transpuesta(matriz))
