import numpy as np

# skaler = np.array(5)
# vektoal = np.array([1,2,3,4])
# matrix = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# tansel = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])

# print(matrix[2:3, 2,3])

# print(skaler , "\n")
# print(vektoal , "\n")
# print(matrix  , "\n")
# print(tansel , "\n")

# print(vektoal.size)
# print(matrix.size ,"\n")


# # *********************** matris kaçakaç olduğunu söyler *************
# print(vektoal.shape)
# print(tansel.shape)
# print(matrix.shape ,"\n")


# *********** matris in boyutunu belirleme *************
# print(vektoal.ndim)
# print(matrix.ndim)
# print(tansel.ndim ," \n")

# print(matrix.dtype)
# print(type(matrix))


# matris = np.array([[1,2,3,"a"],[4,5,6,"b"],[7,8,9,"c"],[10,11,12,"d"]])

# print(matris,"\n")

# print(matris[2:3 , 3:4] ,"\n")

# print(np.random.randint(1,5))
# print(np.random.randint(1,5,(4,4)))  #burası elemanları 1 ile 5 arası ndan oluşan 4 e 4 bir matris üretir


# milyon = np.arange(100)
# print(np.arange(5,50))


# ****************||||| ÖNEMLİ |||||| reshap() matris leri boyutlarını değiştirmek için kullanılır 
# x = print(np.random.randint(0,2,(8,6)).reshape(4,12))

# print( matrix[matrix==2].size)

# **************************************************************************************************************
# --------------------------------------------------------------------------------------------------------------



# array1 = np.array ([[[1,2,3],[4,5,6]] , [[7,8,9],[10,11,12]]])
# print(array1.ndim)

# print(array1.reshape(6,2))

# örenek range ile oluşturduğumuz bir array yi istediğimiz boyuta çevirmemizi sağlar
# array2 = np.arange(30).reshape(5,6)
# print(array2)


# soru:  59 dahil toplam 60 sayi arasındaki tüm sayılardan oluşan bir array oluşturun , ardından bu arrayin shape ini değiştirerek
#  istediğiniz shaplerde 3 boyutlu bir array elde ediniz 

# array3 =np.arange(60).reshape(5,-1,6) # -1 dediğimiz boyutlardan bir tanesini kendisi ayarlar
# print(array3)

# çok boyutlu bir array yi tek boyuta dönüştürmek te reshap(-1) ile yapılır
# örenek 
# array4 = np.arange(30).reshape(6,5)
# array4= array4.reshape(-1)
# print(array4)

# bir array de gezinöek istiyorsak birden fazla for kullanmak tan sa nditer() metodu kullanmak çok rahatlık sağlar
# örenk
# array = np.arange(120).reshape(2,-1,5)

# for x in np.nditer(array):
#    print(x)


#  ************* Errey elemenlerı arasında dört işlem ***************


array1 = np.array([1,2,3,4,5,6,7])
array2 = np.array([8,9,10,11,12,13,14])

# print(array1+array2)
# print(array1-array2)
# print(array1*array2)
# print(array1//array2)

#  bir array yin bütün elemanlarını toplamaı, ortalaması ,varyansı ve standart sapması

# print(array1.sum())  #  bütün elemanları topla
# print(array2.mean()) #  bütün elemanları ortalamasını bul 
# print(array1.var())  # varyansı bulur
# print(array2.std())  # standart sapma yı bulur


# *****************numpay arraylerini birleştirme(bu işlem np.concatenate() ile yapılır) **********************
print(np.concatenate([array1,array2]))


#  NumPay Arraylarinde (index) Arama 
print(np.where(array1 == 5))  # yani 5 sayisi kaçınci indexte olduğunu sorgulamış luyoruz



