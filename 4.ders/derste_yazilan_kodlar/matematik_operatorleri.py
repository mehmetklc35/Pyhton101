# Matematik Operatörleri
# Tekrardan hoşgeldiniz.

# Python'da ve diğer programlama dillerinde matematik operatörleri oldukça önemlidir. 
# Bu konumuzda, Pythondaki matematik operatörlerini öğreneceğiz.

# Toplama İşlemi (+)
# Python'da toplama işlemi şu şekilde yapılabilmektedir.

# a = 5
# b = 7
# print(a+b)

# x = 1.1
# y = 2.3
# print(x+y)

# Çıkarma İşlemi (-)
# Python'da çıkarma işlemi şu şekilde yapılabilmektedir.

# a = 30
# b = 35
# c = 40

# print(a-b-c)

# a = 3.4
# b = 2.1
# print(a-b)

# Çarpma İşlemi (*)
# Python'da çarpma işlemi şu şekilde yapılabilmektedir.

# a = 5
# b = 4
# print(a*b)

# i = 5.3
# j = 3.2
# print(i*j)

# Bölme İşlemi (/)
# Python'da bölme işlemi şu şekilde yapılabilmektedir.

# print(10/3)

# Peki bir sayının başka bir sayıya bölümünden çıkan bölüm sonucunu nasıl bulacağız ? 
# Bunun için de Python3'te şu şekilde bir operatör mevcut.

# Tamsayı Bölmesi (//)
# Bu operatör, bir sayının başka bir sayıya bölümünden ortaya çıkan bölüm sonucunu vermektedir.
# Örneklerimize bakalım.

# print(7//3)

# Kalanı Bulma (%)
# Bu operatör de , bir sayının başka bir sayıya bölümünden kalan sonucunu bulmamızı sağlar.

# print(11%3)

# a = 4
# if (a % 2 == 0):
#     print("sayımız çiftir.")
# else:
#     print("sayımız tektir")

# baslangic = int(input("baslangic degeri : "))
# bitis = int(input("bitis degeri : "))
# for i in range(baslangic,bitis):
#     if i % 2 == 0:
#         print(i)
# print(7/3)


# print(round(7/3, 2))

# Üs bulma (**)
# Bu operatör bir sayının üssünü bulmamızı sağlar. 
# Örnek olarak operatörün solundaki sayının sağdaki sayıya göre üssünü ekrana basar.

# print(10 ** 2)

# Peki bir sayının karekökünü nasıl bulacağız ? 
# Matematikten bildiğimiz gibi, bir sayının karekökü , o sayının 1/2 (0.5). üssüdür. 
# O zaman örneğimizle 64 sayısının karekökünü bulmaya çalışalım.

# print(4 ** 0.5)

# İşaret değiştirme (-)
# Programlarımızda bazen bir sayının işaretini değiştirmek isteyebiliriz.
# Bunun için de bu operatör işimize yarayabilir.
# a = -8
# print(a + 10)

# Operatörleri beraber kullanma ve İşlem sırası
# Bütün bu öğrendiğimiz şeyleri beraber nasıl kullanabiliriz? 
# Bunun için matematikteki işlem sırasını biliyorsak çok rahat edeceğiz, çünkü 
# Pythondaki işlem sırası matematiktekiyle birebir aynıdır. Nedir bu işlem sırası ? Kurallar şunlar ;

# 1. Parantez içi her zaman önce yapılır.
# 2. Çarpma ve Bölme her zaman Toplama ve Çıkarma işlemine göre önce yapılır.
# 3. İşlemler soldan sağa değerlendirilir.

# Ancak, buradaki işlemleri ezberlememize hiç gerek yok. 
# Kafamızın karıştığı yerler de işlemleri parantez içine almak, hayat kurtarır :) 
# Şimdi örneklere bakalım.

# print(8 + 4 * 3 / 2 - 18)

# print(8 + ((4 * 3) /2) - 18)