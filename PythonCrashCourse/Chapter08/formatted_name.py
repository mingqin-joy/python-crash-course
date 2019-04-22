def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('Guan', 'Chao')
print(musician)
musician2 = get_formatted_name('Zhou', 'qin', 'ming')
print(musician2)
