# Generatorların Oluşturulması ve Kullanılması

def kareleri_al():
    sonuc = []
    for i in range(1,6):
        sonuc.append(i**2)
    return sonuc

print(kareleri_al())

# Generator fonksiyon
def kareleri_al2():
    for i in range(1,6):
        yield i**2 

generator = kareleri_al2()
print(generator)

#list comprehensionları generatorlara çevirme

liste = [i**3 for i in range(5)]
print(liste)

generator = (i**3 for i in range(5))
iterator = iter(generator)
print(next(iterator))

    