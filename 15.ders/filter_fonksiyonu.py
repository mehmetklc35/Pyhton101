# lambda_fonksiyon = lambda x: x % 2 == 0

# print(lambda_fonksiyon(2))

# def ciftmi(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# liste = [0,1,2,3,4,5,6,7,8,9,10]
# # print(list(filter(lambda x: x % 2 == 0,liste)))
# # print(list(filter(lambda x: x % 2 == 1,liste)))
# print(list(filter(ciftmi,liste)))

def asalMi(x):
    i = 2
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:
        while(i < x):
            if x % i == 0:
                return False
            i += 1
    return True

# liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
liste = range(0,100)
print(list(filter(asalMi,liste)))
    

