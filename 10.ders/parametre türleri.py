def toplama(a,b,c):
    print(a+b+c)
    
toplama(3,4,5)

def toplama(*Parametreler):
    toplam = 0
    print("*Parametreler:",Parametreler)
    for i in Parametreler:
        toplam += i
    return toplam

print(toplama(3,4,5,6,7,8,9))

    
