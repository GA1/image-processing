from PIL import Image

image = Image.open("image-result-binarized.png").convert('RGBA')
pixel_data = list(image.getdata())

for i, pixel in enumerate(pixel_data):
    (r, g, b, a) = pixel[:4]
    if r == 255 and g == 255 and b == 255:
        pixel_data[i] = (255, 255, 255, 0)

image.putdata(pixel_data)
image.save("image-result-white-pixels-to-transparent.png")
