from PIL import Image

img = Image.open("image-input.png")
gray = img.convert('L')
bw = gray.point(lambda x: 0 if x < 178 else 255, '1')
bw.save("image-result-binarized.png")
