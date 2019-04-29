import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'C:/Users/MingqinZhou/Desktop/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lows, dates = [], []
    highs = []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            low = int(row[3])
            high = int(row[1])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("Daliy high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜的日期格式
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
