from PIL import Image, ImageFilter
import PIL
import os

image = Image.open("kuş.jpg")
# image.show()
# image.save("kuş2.jpg")
# image.rotate(180).save("kuş3.jpg")
# image.rotate(90).save("kuş4.jpg")
# image.convert(mode="L").save("kuş5.jpg")
# degistir = (960,600)
# image.thumbnail(degistir)
# image.save("kuş9.jpg", "JPEG")

# small_img = image.resize(degistir, PIL.Image.Resampling.LANCZOS)  
# print(small_img.size)
# small_img.save("kuş8.jpg")
# image.save("kuş7.jpg")

# from PIL import Imageimport 
# glob, ossize = 128, 128
# for infile in glob.glob("*.jpg"):
#     file, ext = os.path.splitext(infile)
#     with Image.open(infile) as im:
#         im.thumbnail(size)
#         im.save(file + ".thumbnail", "JPEG")

# image.filter(ImageFilter.GaussianBlur(30)).save("kuş12.jpg")

kirpilacak_alan = (302,0,963,569)
image2 = Image.open("atatürk.jpg")
image2.crop(kirpilacak_alan).save("ataturk1.jpg")