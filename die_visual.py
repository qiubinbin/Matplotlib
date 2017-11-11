import pygal
from die import Die

# 创建一个骰子对象
die6_1 = Die()
die10_1 = Die(10)
# 掷骰子，存结果
result = []
for roll_num in range(10000):
	result_temp = die6_1.roll() + die10_1.roll()
	result.append(result_temp)
# print(results)
# 分析结果
max_result = die6_1.num_sides + die10_1.num_sides
frequencies = []
for value in range(2, max_result + 1):
	frequency = result.count(value)
	frequencies.append(frequency)
print(frequencies)
# 可视化结果
hist = pygal.Bar()
hist.title = "Result of rolling one D6+D10 10000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add('D6+D10', frequencies)
hist.render_to_file('die_visual.svg')
