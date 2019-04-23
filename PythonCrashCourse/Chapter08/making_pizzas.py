#from PythonCrashCourse.Chapter08.formatted_name import get_formatted_name, get_formatted_name2
from PythonCrashCourse.Chapter08.formatted_name import *
# import PythonCrashCourse.Chapter08.formatted_name
import PythonCrashCourse.Chapter08.pizza as mp
mp.make_pizza(12, 'pepperoni')
mp.make_pizza(16, 'mushrooms', 'Agreen peppers', 'extra cheese')

musician = get_formatted_name('Guan', 'Chao')
print(musician)
musician2 = get_formatted_name2('Zhou', 'qin', 'ming')
print(musician2)

'''
PythonCrashCourse.Chapter08.formatted_name.get_formatted_name()
PythonCrashCourse.Chapter08.formatted_name.get_formatted_name2()
'''
