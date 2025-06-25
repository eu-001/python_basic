import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#이미지 열기
img = Image.open('pngtree-tiger-roar-animal-wallpapers-picture-image_2903696.jpg').convert('RGB')
img_np = np.array(img)
#밝기 증가 RGB 채널에 50을 더함
brighter = img_np.astype(np.int16) + 50  # Use int16 to prevent overflow
brighter = np.clip(brighter, 0, 255).astype(np.uint8)

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img_np)

plt.subplot(1, 2, 2)
plt.title("Brighter")
plt.imshow(brighter)
plt.show()