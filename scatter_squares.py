import matplotlib.pyplot as plt

x = range(6)
y = [0, 1, 4, 9, 16, 25]
plt.scatter(x, y, s=100, color='r')
plt.title('Square Number', fontsize=14)
plt.xlabel('Value', fontsize=14,color='r')
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.show()
