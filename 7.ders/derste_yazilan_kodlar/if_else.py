# Koşullu Durumlar - if-else koşullu durumları
# Şimdiye kadar Pythondaki temel veritiplerini öğrendik ve gerekli temelleri aldık.
# Artık bundan sonra çok daha eğlenceli konular göreceğiz ve elle tutulur programlar 
# yazmaya başlayacağız. Bu konuda ilk olarak Python programlarının çalışma mantığını 
# göreceğiz ve daha sonrasında koşullu durumları anlamaya çalışacağız.

# Python Programlarının çalışma mantığı
# Python programları çalışmaya başladığı zaman kodlarımız yukardan 
# başlayarak teker teker çalıştırılır ve çalıştıracak kod kalmayınca 
# programımız sona erer. Şöyle bir örneği düşünelim;

# a = 2
# b = 3
# c = 4
# print(a+b+c)

# Yukarıdaki basit kodda program teker teker her bir satırı ve
# ifadeyi çalıştırır ve çalıştıracak kod kalmayınca program sona
# erer.Ancak Python'da her program bu kadar basit olmayabilir. 
# Çoğu zaman Python programlarımız belirli bloklardan oluşur ve
# bu bloklar her zaman çalışmak zorunda olmaz.Peki bu bloklar nasıl tanımlanır 
# ? Pythonda bir blok tanımlama işlemi Girintiler sayesinde olmaktadır. 
# Örnek olması açısından, Pythonda bloklar şu şekilde oluşabilir.

# indentation
# a = 2 # Blok 1 'e ait kod

# if (a == 2):
#     print(a) # Blok 2'ye ait kod
#     print("selcuk")
#     if (a > 3):
#         print("blok 3") # Blok 3'ye ait kod
#         print("selcuk") # Blok 3'ye ait kod
#     print("nova") # Blok 2'ye ait kod
# print("Merhaba") # Blok 1 ' ait  kod

# Dikkat ederseniz burada daha önce görmediğimiz bir şey yaptık ve if in 
# bulunduğu satırdan sonraki print işlemini bir tab kadar girintili yazdık. 
# Burada gördüğümüz gibi, girintiler(tab) Pythonda bir blok oluşturmak için 
# kullanılıyor ve her bloğunun çalıştırılması gerekmiyor. Mesela 
# yukarıda gördüğümüz kodda 2 print işlemi de çalıştı. Ancak kodumuzu 
# şu şekilde yazsaydık, ilk print işlemi çalışmayacaktı.

# a = 2 # Blok 1 'e ait kod

# if (a == 3):
#     print(a) # Blok 2'ye ait kod
# print("Merhaba") # Blok 1 ' ait kod

# Buradaki blok tanımlama işlemlerimiz bundan sonra sürekli karşımıza çıkacak. 
# Eğer henüz anlamadıysanız zamanla anladığınızı göreceksiniz.

# Koşullu Durumlar
# Artık Pythonda bizi bir ileri seviyeye taşıyacak koşullu durumları 
# öğrenmenin vakti geldi.

# Koşullu durumlar aslında günlük yaşamda sürekli karşılaştığımız 
# durumlardır. Örneğin havanın yağmurlu olma koşuluna göre şemsiyemizi 
# alırız veya uykumuzun gelme koşuluna göre uyuruz. 
# Aslında programlamada da birçok koşullu durumla karşılaşırız. 
# Örneğin , belli koşullara göre belli işlemleri yaparız , 
# belli koşullara göre yapmayız. İşte bunlar koşullu durumların 
# temeli oluşturur. İsterseniz koşullu durumları yazmaya if 
# blokları ile başlayalım.

# if Bloğu
# if bloğu programımızın içinde herhangi bir yerde belli bir 
# koşulu kontrol edecek isek kullanılan bloklardır.Yazımı şu şekildedir;
# if (kosul): 
#     # if bloğu - Koşul sağlanınca (True) çalışır. 
#     # Bu hizadaki her işlem bu if bloğuna ait.
#     # if bloğu - Girintiyle oluşturulur.
#     Yapılacak İşlemler

# if bloğu eğer koşul sağlanırsa anlamı taşır.
#  Eğer if kalıbındaki koşul sağlanırsa (True) 
#  if bloğu çalıştırılır, koşul sağlanmazsa (False) 
#  if bloğu çalıştırılmaz.

# Hemen bir örnek ile koşullu durumları anlamaya çalışalım.
    
# 18 yaş kontrolü
# yaş = int(input("Yaşınızı giriniz:"))

# if (yaş < 18):
#     # if bloğu -  Girinti ile sağlanıyor.
#     print("Bu mekana giremezsiniz.")
# if (yaş > 18):
#     print("bu mekana girebilirsiniz.")

# Negatif mi değil mi ?
# sayı = int(input("Sayıyı giriniz:"))

# if (sayı < 0):
#     print("Negatif Sayı")

# else Bloğu
# else blokları *if koşulu * sağlanmadığı zaman (False) 
# çalışan bloklardır. Kullanımı şu şekildedir;
# else:
#     # else bloğu - Yukarısındaki herhangi bir if bloğu 
#     # (veya ilerde göreceğimiz elif bloğu) çalışmadığı
#     # zaman çalışır. 
#     # else bloğu - Girintiyle oluşturulur.
#     Yapılacak İşlemler

# Dikkat ederseniz burada else koşulunun yanına herhangi bir 
# koşul yazmadık. Çünkü zaten else bloğunun çalışması 
# ondan önce gelen diğer koşulların sağlanmamasına bağlı 
# oluyor. İsterseniz, 18 yaş kontrolü örneğini else bloğunu
# dahil ederek tekrar yazalım.

age = int(input("Lütfen yaşınızı giriniz: "))

if (age < 18):
    print("Bu mekana giremezsiniz.")
else:
    print("mekana hoşgeldiniz.")

