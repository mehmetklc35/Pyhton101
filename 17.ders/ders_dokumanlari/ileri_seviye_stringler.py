# upper() metodu stringin tüm karakterlerini büyük harfe çevirir.

# lower() metodu stringin tüm karakterlerini küçük harfe çevirir

# print("NoVa AcAdEMy".upper())
# print("NoVa AcAdEMy".lower())

# replace(x,y) : Stringteki x değerlerini y ile değiştirir.

# print("Bu derse katılan öğrencilerin python bilgisi iyi düzeyde".replace("e","o"))

# print("Nova Academy Nova Academy".replace("Nova","THY"))

# print("Bu derse, katılan öğrencilerin, python bilgisi iyi düzeyde".replace(",","-"))

# startswith(x) : String x ile başlıyorsa True, başlamıyorsa False değeri döndürür.

# endswith(x) : String x ile bitiyorsa True, bitmiyorsa False değeri döndürür.

# print("Ali ata bak.".startswith("Veli"))

# print("Ali ata bak.".endswith("bak."))

# split(a) : Verilen bir a değerine göre stringi 
# parçalara ayrılarak herbir parça listeye atılır.

# cumle = "Python Programlama Dili".split(" ")
# print(cumle)
# print(type(cumle))

# prog_dilleri = "Java-C#-Python-Javascript-Ruby-Django-Sql".split("-")
# print(prog_dilleri)

# prog_dilleri = "Java-C#-Python-Javascript-Ruby-Django-Sql".split("Javascript")
# print(prog_dilleri)

# strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.

# lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.

# rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.

# print("                   python programlama dili                ".strip(" "),"1",sep="")

# print("                   python programlama dili                ".lstrip(" "),"1")

# print("                   python programlama dili                ".rstrip(" "),"1")

# print("******------python programlama dili---******".strip("*"),"1",sep="")

# join()
# Listenin elemanlarını bir string değeriyle birleştirmemizi sağlar.

# liste = ["15","01","2024"]
# print("/".join(liste))

# liste = ["T","B","M","M"]
# yazi = ".".join(liste)
# print(yazi)

# count(x): Stringin içindeki x değerlerini sayar.

# count(x,index): Stringin içindeki x değerlerini 
# verilen index değerinden başlayarak saymaya başlar.

# print("gece olduğu zaman yıldızları görebilirsiniz. gece".count("görebilirsiniz"))

# print("gece olduğu zaman yıldızları görebilirsiniz. gece".count("gece",3))

# find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk 
# bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.

# rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk 
# bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.

print("araba".find("a"))

print("araba".rfind("a"))

print("araba".rfind("s"))

print("araba".find("x"))