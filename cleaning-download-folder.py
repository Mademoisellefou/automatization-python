from importlib.resources import contents
import os
folder_location = ""
os.chdir(folder_location)
list_of_files =os.listdir()

# Selecting All Images
images = [content for content in list_of_files if content.endswith('.png','.jpg','.jpeg')]

for index, image in enumerate(images):
    os.rename(image,f'{index}.png')
