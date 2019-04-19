# 使用函数range() 生成平方数值，先创建一个空的列表squares存储平方数值
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

square2 = []
for value in range(1, 11):
    square2.append(value ** 2)
print(square2)

min(square2)
max(square2)
sum(square2)

# 列表解析
square3 = [value ** 2 for value in range(1, 11)]
print(square3)

# 动手试一试
for value in range(1, 21):
    print(value)

lists = range(1, 1000001)
for value in lists:
    print(value)
min(lists)
max(lists)
sum(lists)

for value in range(1, 20, 2):
    print(value)

for value in range(3, 31, 3):
    print(value)

lifang = [value ** 3 for value in range(1, 11)]
print(lifang)
print(lifang[0: 4])
print(lifang[-3:])
second_lifang = lifang[:]
print(second_lifang)

second_lifang.append(111)
print(second_lifang)

lifang.append(100)
print(lifang)

# 动手试一试
lan = ['The', 'first', 'three', 'items', 'in', 'the', 'list', 'are']
print(lan[: 3])
print(lan[3:])
