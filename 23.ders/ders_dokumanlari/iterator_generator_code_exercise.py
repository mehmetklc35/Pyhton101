# generator carpim tablosu ornek

# generator
# def carpimtablosu(sayi):
#     for i in range(1,sayi):
#         for j in range(1,sayi):
#             yield "{} x {} = {}".format(i,j,i*j)

# # my_gen = carpimtablosu()
# # iterator = iter(my_gen)
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# for i in carpimtablosu(11):
#     print(i)

# # Peki generatorlar Pythonda nerede kullanılıyor ? 
# # Aslında bizim daha önce öğrendiğimiz range fonksiyonu 
# # Pythonda generator tipinde yazılmış bir fonksiyondur.
    
# for i in range(100):
#     print(i)

# İşte generatorların genel mantığı bu şekilde. 
# Anlamadığınız bir yer olursa lütfen çekinmeden sorun. 
# Bir sonraki derste görüşmek üzere.

# class Kuvvet3:
#     def __init__(self,max = 0):
#         self.max = max
#         self.kuvvet = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.kuvvet <= self.max:
#             sonuc = 3 ** self.kuvvet
#             self.kuvvet += 1
#             return sonuc
#         else:
#             self.kuvvet = 0
#             raise StopIteration
        
# kuvvet = Kuvvet3(6)
# # my_iterator = iter(kuvvet)
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))

# for i in kuvvet:
#     print(i)

# # for j in kuvvet:
# #     print(j)

# generator code exercise
def fibonacci():
    # 1 1 2 3 5 8
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