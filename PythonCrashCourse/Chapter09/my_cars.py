from PythonCrashCourse.Chapter09.car2 import Car
from PythonCrashCourse.Chapter09.electri_car3 import ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
