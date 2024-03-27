from PIL import Image,ImageFilter


image = Image.open("kuş.jpg")
# resmi gösterir
image.show()
# resmi kaydeder
image.save("kuş2.jpg")
# 180 derece döner
image.rotate(180).save("kuş3.jpg")
# 90 derece döner
image.rotate(90).save("kuş4.jpg")
# resmin siyah beyaz halini verir.
image.convert(mode = "L").save("kuş5.jpg")
# boyutları değiştirir
degistir = (960,600)
image.thumbnail(degistir)
image.save("kuş6.jpg")
# blurlanır. 5 -8 -10 değerleri ne kadar yüksekse o kadar blur olur
image.filter(ImageFilter.GaussianBlur(10)).save("kuş8.jpg")

kırpılacak_alan = (340,0,950,600)

image2 = Image.open("atatürk.jpg")
image2.crop(kırpılacak_alan).save("kuş9.jpg")



# image.show()

# image1.save("kuş2.jpg")

# image1.rotate(180).save("kuş2.jpg")

# image1.convert(mode = 'L').save("kuş2.jpg")

# image1.thumbnail((300,300))

# image1.filter(ImageFilter.GaussianBlur(10)).save("kuş4.jpg")




#kırpılacak_alan = (270,0,970,580)
#image1.crop(kırpılacak_alan).save("deneme.jpg")
