from PIL import Image
import os




def resize_as_epic(img):
    old_size = img.size
    old_width = old_size[0]
    old_height = old_size[1]
    new_width = 1000
    new_height = (int)(old_height * 1000 / old_width)
    return img.resize((new_width, new_height), Image.ANTIALIAS)


def resize_as_thumbnail(img):
    return img.resize((140, 140), Image.ANTIALIAS)


def resize_as_author(img):
    return img.resize((140, 140), Image.ANTIALIAS)


files_names = os.listdir('./images')
for file_name in files_names:
    img = Image.open('images/' + file_name)
    if file_name[-8:-4] == 'epic':
        img = resize_as_epic(img)
    elif file_name[-13:-4] == 'thumbnail':
        img = resize_as_thumbnail(img)
    else:
        img = resize_as_author(img)
    img.save('results/' + file_name)