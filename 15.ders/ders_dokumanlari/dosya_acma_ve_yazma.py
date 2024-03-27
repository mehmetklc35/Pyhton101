# w kipi

# open("bilgiler.txt","w")

# file = open("bilgiler.txt","w")

# file = open("C:/Users/selcuk/Desktop/PythonEgitim/15.ders/baska_dosya.txt","w")

# file = open("bilgiler.txt","w", encoding="utf-8")

# file.write("Nova Academy ığü 1111")

# file.close()

# a kipi - append

file = open("bilgiler.txt","a",encoding="utf-8")

file.write("\n\nÖğrenci liste")
file.write("\n************")
file.write("\nMehmet Bey")
file.write("\Hülya Hanım")

file.close()
