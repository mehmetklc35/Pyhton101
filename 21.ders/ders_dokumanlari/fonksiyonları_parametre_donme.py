# Fonksiyonları Dönmek ve Argüman Olarak Göndermek
# Bu konuda fonksiyonları return ile başka bir fonksiyondan dönmeyi ve 
# diğer fonksiyonlara parametre olarak göndermeyi öğreneceğiz.

# Fonksiyonları return ile Dönmek
# Bir fonksiyon aynı zamanda bir obje olduğu için, bu 
# fonksiyonu başka bir fonksiyondan return ile döndürebiliriz.

def fonksiyon(islem_adi):

    def topla(*args):
        toplam = 0
        for i in args:
            toplam += i
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

# deneme = fonksiyon("toplama")
# print(type(deneme))
# print(deneme)
# print(deneme(1,2,3,4,5))

# deneme2 = fonksiyon("carpma")
# print(deneme2(1,2,3,4,5))

# Fonksiyonları Argüman Olarak Göndermek
    
def toplama(*args):
    toplam = 0
    for i in args:
        toplam += i
    return toplam

def cikarma(*args):
    return args[0] - args[1]

def carpma(*args):
    carpim = 1
    for i in args:
        carpim *= i
    return carpim

def bolme(*args):
    return args[0] / args[1]

def anafonksiyon(func1,func2,func3,func4,islem_adi,*args):
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
        
anafonksiyon(toplama,cikarma,carpma,bolme,"bolme",10,5)