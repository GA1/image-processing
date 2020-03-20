from PIL import Image

img = Image.open("image-input.png")
gray = img.convert('L')
bw = gray.point(lambda x: 255 if x < 178 else 0, '1')
bw.save("image-result-binarized.png")
