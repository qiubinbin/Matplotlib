import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw = RandomWalk(5000)
	rw.fill_walk()  # 设置绘图窗口尺寸
	plt.figure(figsize=(10, 10))
	point_number = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values, c='red', linewidth=0.1)  # 设置点的轮廓，半径
	# 突出起始点
	plt.scatter(rw.x_values[0], rw.y_values[0], c='green', s=40, edgecolors='none')
	plt.scatter(rw.x_values[- 1], rw.y_values[- 1], c='green', s=40, edgecolors='none')
	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()
	keep_run = input("Y/N?")
	if keep_run == 'N':
		break