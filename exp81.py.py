from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("CAR.jpg")
img.show()
plt.imshow(img)
plt.show()

print(img.width)
print(img.height)

rotated = img.rotate(145)
plt.imshow(rotated)
plt.show()
rotated.save("rotated_img.jpg")

halfimg = img.resize((img.width // 2, img.height // 2))
plt.imshow(halfimg)
plt.show()
halfimg.save("Half_img.jpg")

resize = img.resize((50,70))
plt.imshow(resize)
plt.show()
resize.save("resized_img.jpg")

flipping = img.transpose(Image.FLIP_LEFT_RIGHT)
plt.imshow(flipping)
plt.show()
flipping.save("flipped_left_to_right.jpg")

flip = img.transpose(Image.FLIP_TOP_BOTTOM)
plt.imshow(flip)
plt.show()
flip.save("flipped_top_to_bottom.jpg")

area = (10, 50, 150, 200)
cropped = img.crop(area)
plt.imshow(cropped)
plt.show()
cropped.save("cropped_img.jpg")

grayscale = img.convert("L")
plt.imshow(grayscale)
plt.show()
grayscale.save("grayscale_img.jpg")

bw = img.convert("LA")
plt.imshow(bw)
plt.show()
bw.save("black_white.png")

blur = img.filter(Image Filter.GaussianBlur(radius = 5))
plt.imshow(blur)
plt.show()
blur.save("Blur_img.jpg")