from PIL import Image

image = Image.open("image-result-white-pixels-to-transparent.png").convert('RGBA')
pixel_data = list(image.getdata())

for i, pixel in enumerate(pixel_data):
    (r, g, b, a) = pixel[:4]
    if a != 0:
        desired_r = 4
        desired_g = 77
        desired_b = 165
        pixel_data[i] = (desired_r, desired_g, desired_b, 255)

image.putdata(pixel_data)
image.save("image-result-transparent-to-color.png")
