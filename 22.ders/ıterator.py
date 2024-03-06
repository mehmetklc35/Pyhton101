# liste = [1,2,3,4,5]
# for i in liste:
#     print(i)

liste = [1,2,3,4,5]
iterator = iter(liste)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
# Kendi iterable objelerimizi oluşturmak

class Kumanda:
    def __init__(self,kanal_listesi):
        self.kanal_listesi =kanal_listesi # kanal listemiz
        self.index = -1 # indeksimiz
    
    def __iter__(self):
        return self #iterator oluşturduğumuz (iter fonksiyonu çağrıldığında)
    
    def __next__(self):
        self.index += 1
        if self.index < len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration
kumanda = Kumanda(["atv","kanal-d","tv-8","star","now"])

iterator = iter(kumanda ) #objemiz iterable olduğu için iterator oluşturabiliriz.
print(next(iterator))
