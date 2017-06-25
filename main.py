from PIL import Image
import os


def resize_as_epic(img):
    old_size = img.size
    old_width = old_size[0]
    old_height = old_size[1]
    new_width = 800
    new_height = (int)(old_height * 800 / old_width)
    if old_width < new_width:
        return img
    else:
        return img.resize((new_width, new_height), Image.ANTIALIAS)


def resize_as_thumbnail(img):
    return img.resize((160, 160), Image.ANTIALIAS)


def resize_as_author(img):
    return img.resize((200, 200), Image.ANTIALIAS)


files_names = os.listdir('./images')
for file_name in files_names:
    img = Image.open('images/' + file_name)
    if 'epic' in file_name:
        img = resize_as_epic(img)
    elif 'thumbnail' in file_name:
        img = resize_as_thumbnail(img)
    else:
        img = resize_as_author(img)
    img.save('results/' + file_name.replace('_raw', ''))
