from functools import reduce

# def sayilariTopla(x,y):
#     return x+y

# print(reduce(sayilariTopla,range(1,100)))


# def sayilariCarp(x,y):
#     return x*y

# print(reduce(sayilariCarp,[1,2,3,4]))

# max fonksiyonu
print(max([22,-50,1000,25454474,654555454]))

def maksimum(x,y):
    if(x > y):
        return x
    else:
        return y

print(reduce(maksimum,[22,1000,10]))