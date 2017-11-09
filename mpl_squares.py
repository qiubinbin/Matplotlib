import matplotlib.pyplot as plt

x = [1.0, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(x, squares, 'g', linewidth=2)
plt.title('Square Number', fontsize=14)
# 设置坐标标签以及字体
plt.xlabel('Value', fontsize=14)
plt.ylabel('Squares', fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14, direction='out', color='g')
plt.show()
