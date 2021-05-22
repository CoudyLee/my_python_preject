import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
fig,ax = plt.subplots()         #创建空白图表
ax.plot(squares)                #给表赋值

plt.show()                      #绘制图表
