import numpy as np

a=np.array ([1,2,3,4])
list1=[1,2,3,4]

a+=1
#list1+=1
'''
print (f"a:{a}")
print(f"list1:{list1}")


a=np.array([1,2,3])
b=np.zeros((2,3))
c=np.ones((3,3))
d=np.arange(0,10,2)
f=np.random.rand(2,3)
print(f"a:{a}")
print(f"b:{b}")
print(f"c:{c}")
print(f"d:{d}")
print(f"f:{f}")
'''

a=np.array([1,2,3])
b=np.array([10,20,30])
print(f"a+b:{a+b}")
print(f"a*b:{a*b}")


a=np.array([
    [1,2,3,],
    [4,5,6,]
])
print(a[0])
print(a[:,1])
#: = all

'''
import matplotlib.pyplot as plt
image = np.zeros((28,28))
print(image.shape)
plt.imshow(image,cmap="gray")
plt.title('28*28 black image')
plt.axis('off')
plt.show()

import matplotlib.pyplot as plt
color_img = np.zeros((100,100,3))
color_img[0:50,0:50]=[0.15,0.12,0.25]
color_img[50:100, 0:50]=[0.5,0, 0.9]
color_img[50:100,50:100][1,1,1]
print(color_img)
plt.imshow(color_img)
plt.title('100*100 color image')
plt.axis('off')
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plot a 3D surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()

a=np.array([1,2,3,4,5,6])
print(a.shape)

b=a.reshape(2,3)
print(b)
'''

a=np.array([[1,2],[3,4]])
r=a.ravel()
f=a.flatten()
print(r)
print(f)

#ravel flatten을 쓰면 다차원 행렬을 1차원으로 바꿔준다.








