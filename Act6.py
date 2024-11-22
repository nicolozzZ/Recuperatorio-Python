matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
def suma_diagonales(mat):
    num = 0
    num2 = 0
    for i in range (len(mat)):
        for j in range (len(mat[i])):
            if i == j: 
                num += mat[i][j] #num = mat[0][0] + mat[1][1] + mat[2][2] + mat[3][3]
            elif i + j + 1 == len(mat): 
                num2 += mat[i][j] #num2 = mat[3][0] + mat[2][1] + mat[1][2] + mat[0][3]
            
    return num, num2
    
print(suma_diagonales(matriz))
