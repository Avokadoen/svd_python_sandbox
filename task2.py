#
# Singular value tutorial
#
import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image
import os 


#
# Load images from files
#
images = []
for filename in os.listdir('numberimage'):
    img = Image.open('numberimage/'+filename).convert('L');
    if img is not None:
        images.append(img)


#
# Division of data set into two parts
#
trainrange = 30

flattraindata = np.array([images[i+55*j].getdata() for i in range(0,trainrange) for j in range(0,10)], dtype=float)
flattestdata = np.array([images[i+55*j].getdata() for i in range(trainrange,55) for j in range(0,10)], dtype=float)


#
# index % 10 is the digit 
#
index = 45
ex = flattestdata[index].reshape(30,30)
plt.imshow(ex)
