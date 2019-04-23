def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user('Guanchao')


def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name


while True:
    print("\n Please enter your name:")
    print("Enter 'q' at any time to quit.")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    if ((first_name == 'q') or (last_name == 'q')):
        break
    else:
        format_name = get_formatted_name(first_name, last_name)
        print("\n Hello, " + format_name + "!")
