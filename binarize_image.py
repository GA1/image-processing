# from PIL import Image
#
# img = Image.open("image.png")
# gray = img.convert('L')
# bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
# bw.save("tiengos-result.png")
#
#
# 0.21 R + 0.72 G + 0.07 B.

from PIL import Image

image = Image.open("image-input.png").convert('RGBA')
pixel_data = list(image.getdata())

for i, pixel in enumerate(pixel_data):
    (r, g, b, a) = pixel[:4]
    if a > 10:
        pixel_data[i] = (0, 0, 0, 255)

image.putdata(pixel_data)
# image = image.resize((500, 500), Image.ANTIALIAS)
image.save("image-output.png")
