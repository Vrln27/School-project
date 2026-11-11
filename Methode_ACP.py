'''
projet ACP.  
'''
import numpy as np 
import matplotlib.pyplot as plt 
import os
from sklearn.decomposition import PCA
from PIL import Image


# import d'une image 

img = input(Image.open("cardigan_ex.jpeg"))

# Conversion en matrice 
matrice_a = np.array(img)/255

plt.imshow()
plt.axis("off")
plt.show