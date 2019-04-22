responses = {}
active = True
while active:
    name = input("\n What is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes / no)")
    if repeat == 'no':
        active = False
print("\n---Result---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
