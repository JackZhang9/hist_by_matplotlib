import matplotlib.pyplot as plt
import numpy as np
# print(plt.rcParams.keys())
plt.rcParams['font.sans-serif']=['SimHei']

'''直方图'''
x=np.random.randint(0,100,(400,))
plt.hist(x,bins=50,edgecolor='r')
plt.xlabel('分数')
plt.ylabel('人数')
plt.title('分数人数')
plt.show()








