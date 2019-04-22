message = input("Tell me something, and I will repeat it back to you: ")
print(message)
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\n what is your first name?"
name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you ?")
age = int(age)
age >= 18


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
#active = True
"""while message != 'quit':
    active = False
    message = input(prompt)
    if message != 'quit':
    print(message)
"""
while True:
    message = input(prompt)

    if message == 'quit':
        break
