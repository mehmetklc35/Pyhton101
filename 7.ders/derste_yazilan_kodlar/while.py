# While Döngüleri
# Bu bölümde while döngülerinin yapısını ve nasıl 
# kullanılacağını öğrenmeye çalışacağız.

# while döngüleri belli bir koşul sağlandığı 
# sürece bloğundaki işlemleri gerçekleştirmeye devam eder.
# while döngülerinin sona ermesi için koşul durumunun bir
#  süre sonra False olması gereklidir.Yapısı şu şekildedir;

# while (koşul):
#     İşlem1
#     İşlem2
#     İşlem3
#       //
#       //
    
# while döngülerini daha iyi anlamak için örneklerimize bakalım.
    
# i = 0

# while (i<10):
#    print(f"i nin değeri = {i} 'dir ")
#    i +=1

# i = 0

# while(i < 20):
#     print(f"i nin değeri = {i} 'dir ")
#     i += 2

# i = 0

# while(i<5):
#     print("Python öğreniyorum.")
#     i += 1

# liste = [1,2,3,4,5,6]
# a=0
# while(a<len(liste)):
#     print(f"Indeks: {a}, Eleman: {liste[a]}")
#     a += 1

# Sonsuz Döngü Olayları
# while döngüsü kullanırken biraz dikkatli olmamızda fayda var. 
# Çünkü, while döngü koşulunun bir süre sonra False olması 
# gerekecek ki döngümüz sonlanabilsin. Ancak eğer biz while 
# döngülerinde bu durumu unutursak , döngümüz sonsuza kadar 
# çalışacaktır. Biz buna sonsuz döngü olayı diyoruz. Örneğimize bakalım

# i = 0
# while(i<10):
#     print(i)