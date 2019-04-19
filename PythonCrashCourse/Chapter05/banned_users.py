banned_users = ['andrew', 'carolina', 'david']
user1 = 'carolina'
if user1 in banned_users:
    print(user1.upper())

user2 = 'marie'
if user2 not in banned_users:
    print(user2.title() + ", you can post a response if you wish.")
