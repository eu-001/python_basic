import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('pngtree-tiger-roar-animal-wallpapers-picture-image_2903696.jpg')  # 컬러로 열기
img_np = np.array(img)
# 좌우반전: 열(가로축) 순서를 뒤집는다 (컬러 이미지)
flipped = img_np
if img_np.ndim == 2:
    # 흑백일 때: 두 개의 차원만 있으니까 이렇게
    flipped = img_np[:, ::-1]
else:
    # 컬러일 때: 세 번째 축(RGB)까지 고려
    flipped = img_np[:, ::-1, :]

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img_np)
plt.subplot(1, 2, 2)
plt.title('Flipped Image')
plt.imshow(flipped)
plt.show()

