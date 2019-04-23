def greet_users(names):
    for name in names:
        message = "Hello, " + name.title()
        print(message)


usernames = ['Zhoumingqin', 'Guanchao', 'Ganluping']
greet_users(usernames)
