alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['color'] = 'yellow'
print(alien_0)
del alien_0['points']
print(alien_0)
del alien_0['color']
print(alien_0)

alien_0['x_position'] = 0
print(alien_0)
alien_0['y_position'] = 25
print(alien_0)
alien_0['speed'] = 'medium'
print(alien_0)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position:" + str(alien_0['x_position']))

del alien_0['speed']
print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 6}
alien_2 = {'color': 'red', 'points': 7}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens)

for alien in aliens[:5]:
    print(alien)

print("...")
print("Total number of aliens: " + str(len(aliens)))
