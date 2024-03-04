# fonksiyonları Dönmek ve Argüman alorak göndermek

from numpy import argsort


def fonksiyon(islem_adi):
    
    def topla(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplama":
        return topla
    else:
        return carpma
    
deneme = fonksiyon("toplama")
print(type(deneme))
print(deneme)
print(deneme(1,2,3,4,5))

deneme2 = fonksiyon("carpma")
print(deneme2(1,2,3,4))

# Fonksiyonları Argüman olarak göndermek

def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def anafonksiyon(func1,func2,func3,func4,islem_adi):
    if islem_adi == "toplama":
        print(func1(*args))
    elif islem_adi == "cikarma":
        print(func2(*args))
    elif islem_adi == "carpma":
        print(func3(*args))
    elif islem_adi == "bolme":
        print(func4(*args))
    else:
        print("Geçersiz işlem.....")
        
anafonksiyon(toplama,cikarma,carpma,bolme,"cikarma",10,2)