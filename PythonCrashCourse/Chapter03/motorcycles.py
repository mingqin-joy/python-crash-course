motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('haha')
print(motorcycles)
bicycles = []
bicycles.append('honda')
bicycles.append("yamaha")
bicycles.append('suzuki')
print(bicycles)
bicycles.insert(0, 'ducati')
print(bicycles)
del bicycles[0]
print(bicycles)

print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + '.')


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# 动手试一试
guests = ['Chao Guan', 'Luping Gan', 'Mingqin Zhou', 'Yongwen Wang']
print(guests)
print("Please have a dinner with me : " + guests[0] + " and " + guests[1])
print("Oh, my God! " + guests[-1] + "couldn't come.")
del guests[-1]
print(guests)
guests.append("Da huang")
print(guests)
print("I have found a bigger desk, so we can call more people to come.")
guests.insert(0, 'Zhou an')
print(guests)

guests.insert(3, 'Song kun')
print(guests)
guests.append('Zhang fei')
print(guests)
print("We only could twe guests have a dinner, Sorry.")
first_guest_go = guests.pop()
print(guests)
second_guest_go = guests.pop()
print(guests)
third_guest_go = guests.pop()
print(guests)
four_guest_go = guests.pop()
print(guests)
five_guest_go = guests.pop()
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)
