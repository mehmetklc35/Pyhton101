# Print Fonksiyonu ve Formatlama
# Bu bölümde ekrana veri tiplerini yazdırmak için kullandığımız print() 
# fonksiyonunu ve formatlama yöntemlerini öğreneceğiz.

# Print() Fonksiyonu
# Kodlarımızı dosyalara yazdığımızda, eğer ekrana bir değer 
# bastırmak istersek print fonksiyonunu kullanırız. 
# Kullanımı oldukça basittir ve değişik özelliklere sahiptir. Örneklerimize bakalım.

# print(35)
# print(3.154)

# a = 18
# b = 24
# print(a+b)

# a = "18"
# b = "24"
# print(a+b)

# print("Selcuk Akarın'ın Dersi")


# Buradaki işlemlerde gördüğümüz gibi biz print fonksiyonunun içine bastırmak 
# istediğimiz değeri veriyoruz ve bu fonksiyon da ekrana değerimizi bastırıyor. 
# Peki aynı satırda birkaç değer bastırmak istersek ne yapıyoruz?
# Bunun için değerlerimizin arasına , karakterini atıyoruz.

# print("Matematik : ",85," Türkçe : ",70)

# print("Ali ",8,9.1657,True)

# Stringlerdeki Özel Karakterler
# Pythonda stringlerde kullanılan özel karakterler mevcuttur ve 
# kullanıldıkları yerler de işlerimizi kolaylaştırır. 
# En çok kullanılan 2 tanesi şunlardır;

# \n karakteri
# Eğer print() fonksiyonu stringlerde böyle bir karakterle 
# karşılaşırsa alt satırdan ekrana yazdırma işlemine devam eder. 
# Hemen örneklerimize bakalım.

# print("Merhaba,\n\nBu dilekçeyi Müdürlüğünüze yazıyorum.\nBen Selçuk Akarın")

# \t karakteri  ***** açıklanacak
# Eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa bir 
# tab boşluk bırakarak ekrana yazdırma işlemine devam eder. Hemen örneklerimize bakalım.

# print("Ocak\tMart\tŞubat")

# type() fonksiyonu
# print() fonksiyonundan bahsetmişken type() fonksiyonunu öğrenmekte fayda var. ,
# type() fonksiyonu içine gönderilen değerin hangi veri tipinden olduğunu söyler.

# print(type(8))

# print(type("sınıf"))

# print(type(True))

# Print() Fonksiyonunun Özellikleri
# Ekrana yazdırma işlemlerimiz sırasında print() fonksiyonunun 
# faydalı özelliklerini kullanırsak yazdığımız kodu daha verimli kılabiliriz.
# Bunun için burada 2 tane özellikten bahsedeceğiz.

# sep parametresi
# print() fonksiyonunda kullanılabilen sep parametresi yazdırdığımız 
# değerlerin arasına istediğimiz karakterlerin yerleştirilmesini sağlar. 
# Eğer bu parametreyi kullanmazsak değerlerin arasına varsayılan olarak boşluk
# yerleştirildiğini biliyoruz.Örneklere bakalım.

# print("Selcuk","Hoca")

# print("Selcuk","Hoca", sep=" ")

# print("Selcuk","Hoca","Ders","İşliyor", sep=".-.")

# print("15","12","2023", sep="/")

# Yıldızlı Parametreler
# Eğer bir stringin başına * işareti koyup, print fonksiyonuna 
# gönderirsek bu string karakterlerine ayrılacak ve her bir karakter 
# ayrı birer string olarak davranılarak ekrana basılacaktır.

# print(*"NovaAcademy")


# print(*"NovaAcademy", sep="*")

# Formatlama
# Programlama yaparken bazı yerlerde bir stringin içinde daha önceden 
# tanımlı string,float, int vs. değerleri yerleştirmek isteyebiliriz. 
# Böyle durumlar için Pythonda format() fonksiyonu bulunmaktadır. 
# Örneğin, programımızda 3 tane tamsayı değerimiz var ve biz bunları 
# bir string içinde ekrana basmak istiyoruz. Bunun için format() 
# fonksiyonunu kullanabiliriz. format() fonksiyonunun çok fazla özelliği 
# olduğu için, ben burada sadece en çok kullandığımız özelliğini göstereceğim.

# string = "{}.{}.{}.{}.".format("T","B","M","M")

# print(string)

# a = 5
# b = 10
# print("{} + {} = {} dir. Sonucumuz {}'dir.".format(a,b,a+b,a+b))

# a = 5
# b = 10
# print("{2} + {1} = {0} dir. Sonucumuz {3}'dir.".format(a+b,b,a,a+b))

# print("{:.2f} - {:.1f} - {:.4f}".format(3.152,184.15,54554.65465465))