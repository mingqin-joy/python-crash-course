from PythonCrashCourse.Chapter15.die import Die
import pygal
die1 = Die()
die2 = Die(10)
results = []
for roll_num in range(5000):
    result = die1.roll() + die2.roll()
    results.append(result)
print(results)

# 分析结果
frenquencies = []
max_result = die1.num_sizes + die2.num_sizes
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frenquencies.append(frequency)
print(frenquencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Results"
hist.add('D6 + D10', frenquencies)
hist.render_to_file('die_visual.svg')
