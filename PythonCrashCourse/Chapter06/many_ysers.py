users = {
    'GC': {
        'Xing': 'Guan',
        'Ming': 'Chao',
        'location': 'Yangzhou',
    },

    'ZMQ': {
        'Xing': 'Zhou',
        'Ming': 'Mingqin',
        'location': 'Chongqing',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    Xingming = user_info['Xing'] + " " + user_info['Ming']
    location = user_info['location']
    print("\tXing: " + Xingming)
    print("\tfrom: " + location)
