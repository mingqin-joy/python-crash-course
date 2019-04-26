from PythonCrashCourse.Chapter11.name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\n Please give me a first name:")
    if first == 'q':
        break
    last = input("Please give a last name: ")
    if last == 'q':
        break
    format = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + format + ".")
