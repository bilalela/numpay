import numpy as np

skaler = np.array(5)
vektoal = np.array([1,2,3,4])
matrix = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
tansel = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])

print(matrix[2:3, 2,3])

print(skaler , "\n")
print(vektoal , "\n")
print(matrix  , "\n")
print(tansel , "\n")

print(vektoal.size)
print(matrix.size ,"\n")


# # *********************** matris kaçakaç olduğunu söyler *************
print(vektoal.shape)
print(tansel.shape)
print(matrix.shape ,"\n")


# *********** matris in boyutunu belirleme *************
print(vektoal.ndim)
print(matrix.ndim)
print(tansel.ndim ," \n")

print(matrix.dtype)
print(type(matrix))


matris = np.array([[1,2,3,"a"],[4,5,6,"b"],[7,8,9,"c"],[10,11,12,"d"]])

print(matris,"\n")

print(matris[2:3 , 3:4] ,"\n")

print(np.random.randint(1,5))
print(np.random.randint(1,5,(4,4)))  #burası elemanları 1 ile 5 arası ndan oluşan 4 e 4 bir matris üret


milyon = np.arange(100)
print(np.arange(5,50))


# ****************||||| ÖNEMLİ |||||| reshap() matris leri boyutlarını değiştirmek için kullanılır 
x = print(np.random.randint(0,2,(8,6)).reshape(4,12))

print( matrix[matrix==2].size)

# **************************************************************************************************************
# --------------------------------------------------------------------------------------------------------------

