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

'''
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

