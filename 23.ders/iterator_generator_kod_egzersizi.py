#generator carpım tablosu örnek

def carpimtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} : {}".format(i,j,i*j)

my_gen = carpimtablosu()
iterator = iter(my_gen)
print(next(iterator))

for i in carpimtablosu():
    print(i)
    
# peki generatorlar pyhtonda nerede kullanılır?
# aslında bizin daha önce öğrendiğimz range fonksiyonu
# pyhtonda generator tipinde yazılmış bir fonksiyondur.

for i in range(100):
    print(i)
    
# iterable ile kuvvet alma kod yazımı 

class Kuvvet3:
    def __init__(self,max = 0):
        self.max = max
        self.kuvvet = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.kuvvet <= self.max:
            sonuc = 3 ** self.kuvvet
            self.kuvvet +=1
            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration

kuvvet = Kuvvet3(6)

for i in kuvvet:
    print(i)

for j in kuvvet:
    print(j)
    
# generator code exercise

def fibonacci():
    a = 1
    b = 1
    yield a
    yield b
    
    while True:
        a,b = b,a+b
        yield b

for sayi in fibonacci():
    if sayi > 10000:
        break
    print(sayi)