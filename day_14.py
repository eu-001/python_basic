#matplot - png로 그래프 보여주기. 실시간 x

"""
 import matplotlib.pyplot as plt
 import numpy as np

 xpoints = np.array([0, 6])
 ypoints = np.array([0, 250])

 plt.plot(xpoints, ypoints)
 plt.show()
"""
#수학으로 그래프 해석하면 (0,0)(6,250) 걍 기하하는 건디
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
xpoints = np.array([0.3, 0.7, 2.1, 2.2])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(ypoints, marker = 'o')
plt.plot(xpoints, linestyle = 'dotted')
plt.title("egea meu hanueon guim", loc="right")
plt.ylabel("omg",fontdict=font1)
plt.xlabel("what",fontdict=font2)
plt.show()
"""
