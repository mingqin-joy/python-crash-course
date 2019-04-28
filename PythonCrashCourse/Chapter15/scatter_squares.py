import matplotlib.pyplot as plt

# 自动计算数据
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.get_cmap("Blues"),
            edgecolors='none', s=40)
# 设置坐标轴，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=14)
plt.xlabel("value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
# 设置每个坐标轴的取值范围s
plt.axes([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('C:/Users/MingqinZhou/Desktop/squares_plot.png')
