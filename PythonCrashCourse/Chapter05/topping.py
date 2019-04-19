request_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in request_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in request_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in request_toppings:
    print("Ading extra cheese.")

# 动手试一试
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('green')
if 'green' not in alien_color:
    print('green is not the alien color!')

request_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for request_topping in request_toppings:
    if request_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + request_topping + ".")

print("\n Finished your pizza!")

request_toppings = []
if request_toppings:
    for request_topping in request_toppings:
        print("Adding " + request_topping + ".")
else:
    print("Are you sure you want a plain pizza?")

request_toppings = ['mushrooms', 'green peppers', 'extra cheese']
available_toppings = ['mushrooms', 'olivers', 'pepperoni', 'extra cheese']
for request_topping in request_toppings:
    if request_topping in available_toppings:
        print("Adding" + request_topping + ".")
    else:
        print("Sorry, we don't have " + request_topping + ".")
