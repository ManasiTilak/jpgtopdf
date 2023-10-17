# import the modules
import os, os.path
from PIL import Image

# get the path/directory
folder_dir = r'C:\\Users\\Location\\'

# get number of elements in directory
num=0
for element in os.listdir(folder_dir):
    element_path=os.path.join(folder_dir, element)
    if os.path.isfile(element_path):
        num+=1
# print(num)

image_set = []
counter = 1


while(counter <= num):
    image = Image.open(r"C:\\Users\\Location\\" + str(counter) + ".jpg")
    image_mod = image.convert('RGB')
    image_set.append(image)
    counter += 1


image_set[0].save(r'C:\Users\Location\my_images2.pdf', save_all=True, append_images=image_set[1:])