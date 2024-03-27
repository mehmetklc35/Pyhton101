# lambda_fonksiyon = lambda x: x % 2 == 0

# print(lambda_fonksiyon(1))

# filter(fonksiyon,iterasyon yapılabilen bir veritipi(liste vb.))
# liste = [0,1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x: x % 2 == 1,liste)))

# def ciftmi(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# liste = [0,1,2,3,4,5,6,7,8,9,10]
# print(list(filter(ciftmi,liste)))

def asalMi(x):
    i = 2
    if(x == 0):
        return False # Asal değil
    elif(x == 1):
        return False # Asal değil
    elif(x == 2):
        return True # Asal
    else:
        while(i < x):
            if x % i == 0:
                return False # Asal Değil
            i += 1
    return True # Asal

# liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
liste = range(0,1000)
print(list(filter(asalMi,liste)))