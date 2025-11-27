import os 

img_path = os.path.join(os.path.dirname(__file__), 'imgs', 'alex.jpg') 
print(img_path)


path = os.path.dirname(__file__)
path = os.path.dirname(path)
img_path2 = os.path.join(path, "imgs", "alex.jpg")

print(img_path2)