import matplotlib.pyplot as plt
# plt.scatter(2, 4, s=200)
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
