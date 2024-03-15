from PIL import Image, ImageFilter

image = Image.open("back.jpg")
# image.show()
# image.save("back2.jpg")
# image.rotate(180).save("back3.jpg")
degistir = (960,600)
image.thumbnail(degistir)
image.save("back6.jpg")
image.filter(ImageFilter.GaussianBlur(3).save("back10.jpg"))