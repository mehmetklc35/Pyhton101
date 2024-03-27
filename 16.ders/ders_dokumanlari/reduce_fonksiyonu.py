from functools import reduce

# def sayilariTopla(x,y):
#     return x+y

# print(reduce(sayilariTopla,range(1,1000)))

# [1,2,3,4,5]
# x+y
# ((((1+2)+3)+4)+5)

# def sayilariCarp(x,y):
#     return x*y

# #faktöriyel 4!
# print(reduce(sayilariCarp,[1,2,3,4]))

# # 10!
# print(reduce(sayilariCarp,range(1,11)))

# # max
# print(max([22,-50,1000,10,10]))

# max reduce
from functools import reduce

def maksimum(x,y):
    if(x > y):
        return x
    else:
        return y

print(reduce(maksimum,[22,-50,1000,10,10]))