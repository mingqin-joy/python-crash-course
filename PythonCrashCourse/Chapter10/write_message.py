finename = 'C:/Users/MingqinZhou/Desktop/programming.txt'
with open(finename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
with open(finename, 'a') as file_object2:
    file_object2.write("I also love finding meaning in large datasets.\n")
    file_object2.write("I love creating apps that can run in a browser.\n")
