def ciftMi(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
       
liste = [1,2,3,4,5,6,7,8,9,10]

liste2 = list(filter(ciftMi, liste))

from functools import reduce


print(reduce(lambda a,b: a+b, liste2))