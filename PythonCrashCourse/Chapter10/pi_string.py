filename = 'C:/Users/MingqinZhou/Desktop/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

filename2 = 'C:/Users/MingqinZhou/Desktop/pi_million_digits.txt'
with open(filename2) as file_object2:
    lines2 = file_object2.readlines()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string2:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")

pi_string2 = ''
for line in lines2:
    pi_string2 += line.strip()

print(pi_string2[:52] + "...")
print(len(pi_string2))
