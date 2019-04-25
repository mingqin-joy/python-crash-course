import json
numbers = [2, 3, 4, 5, 7, 13]
filename = './numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj1:
    num = json.load(f_obj1)
print(num)
