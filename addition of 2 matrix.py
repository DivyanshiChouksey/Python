# addition of 2 matrix
mat1 =[[1,2],[3,4]]
mat2= [[9,8],[7,5]]
mat3= [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            mat3[i][j]+=(mat1[i][k]*mat2[k][j])
print(mat3)
