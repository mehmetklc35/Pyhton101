# İç içe Fonksiyonlar ve Fonksiyon Parametreleri
# Bu bölümle birlikte decorator fonksiyonların mantığını anlamaya çalışacağız. 
# Decoratorları daha iyi anlamak için fonksiyonlara biraz daha derinlemesine 
# bakmaya çalışalım.

# *args ve **kwargs
# Fonksiyonlara argüman göndermenin esnek bir şekilde yapıldığını biliyoruz. 
# İsterseniz ilk olarak yıldızlı argümanları hatırlamaya çalışalım.

# def fonksiyon(*args): # istediğimiz sayıda argüman gönderebiliriz.
#     print(args)
#     for i in args:
#         print(i)

# # # function call
# fonksiyon(1,2,3)

# def fonksiyon(teacher,instutition,*args): # istediğimiz sayıda argüman gönderebiliriz.
#     toplam = 0
#     print(f"Öğretmen {teacher}, Kurum: {instutition}")
#     for i in args:
#         toplam += i
#     print("not ortalması: ",toplam/12)

# fonksiyon("Selcuk","NovaAcademy",40,80,90,100,110,120,200,10,1,2,3,4)

# def fonksiyon(teacher,instutition,**kwargs):
#     print(f"Dersin öğretmeni {teacher} dır. Dersin verildiği kurumu {instutition} dır.")
#     print(kwargs)

# fonksiyon("Bill Gates","Nova Academy",isim="Selcuk",soyisim="Akarın",numara=1375,memleket="istanbul")


# def fonksiyon(teacher,instutition,*students,**kwargs):
#     print(f"Dersin öğretmeni {teacher} dır. Dersin verildiği kurumu {instutition} dır.")
#     print("Öğrenci listesi")
#     for i in students:
#         print(f"Ogrenci Adı {i}")
#     # print(type(kwargs))
#     for key,value in kwargs.items():
#         print(f"{key} - {value}")

# fonksiyon("Bill Gates","Nova Academy","Hülya","Ahmed","Mehmet",dersin_kodu=1375,ders_saati=4,ders_location="istanbul")


# İç içe fonksiyonlar
# Pythonda fonksiyonlar da birer obje oldukları için hem bir tane 
# değişkene atanabilirler, hem de başka bir fonksiyonun içinde 
# tanımlanabilirler. Şimdi bunlara bakmaya başlayalım.

# def selamla(isim):
#     print("Selam",isim)

# selamla("Selcuk")

# merhaba = selamla
# # print(merhaba)
# # print(selamla)
# merhaba("Hulya")
# del selamla
# merhaba("Ali")
# selamla("MEHMET")

# iç içe fonksiyon
# def fonksiyon():
#     def fonksiyon2():
#         print("Küçük fonksiyondan Selam")
#     print("Büyük fonksiyondan selam")
#     fonksiyon2()

# fonksiyon()

# def fonksiyon(*args):
#     def topla(args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam
#     print(topla(args))

# fonksiyon(1,2,3,4,5)
        