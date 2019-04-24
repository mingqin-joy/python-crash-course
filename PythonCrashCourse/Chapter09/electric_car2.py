# Car()类：汽车作为父类
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas = 0

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def fill_gas_tank(self):
        print("This car  need " + str(self.gas) + " gas tank!")

    def update_gas(self, gass):
        self.gas += gass

# Battery类


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

# ElectricCar() 类:继承父类Car(), 又把Battery类实例之后作为一个属性。


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# 实例化ElectricCar()类
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
