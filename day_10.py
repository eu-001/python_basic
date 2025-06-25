import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img= Image.open('pngtree-tiger-roar-animal-wallpapers-picture-image_2903696.jpg').convert('L')
img_np= np.array(img)
inverted= 255 - img_np
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img_np, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Inverted Image')
plt.imshow(inverted, cmap='gray')
plt.show()