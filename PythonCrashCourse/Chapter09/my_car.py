from PythonCrashCourse.Chapter09.car import ElectricCar  # 导入模块内的类
import PythonCrashCourse.Chapter09.car as cars  # 导入整个模块
my_new_car = cars.Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# my_new_car.odemeter_reading = 23
# my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
