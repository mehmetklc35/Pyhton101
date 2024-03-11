import sys

sys.stderr.write("Burası bir hata mesajıdır\n")
sys.stderr.flush()
sys.stdout.write("Burası normal çıktımız\n")

import sys

def kok_bulma(a,b,c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("denklemin reel kökü yok")
    else:
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
        return (x1,x2)

if len(sys.argv) == 4:
    print("Kök bulma ", kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler giriniz")
    sys.stderr.flush()