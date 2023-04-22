#exes 1
from functools import reduce

my_resume = {'name': 'Bakhtiyar',
            'surname': 'Sailauov',
            'age': 19,
            'profesional': 'soft Engiener',
            'city': 'Karaganda'}

def functional_def(objects):
    for item in objects:
        print(f'{item}: {objects[item]}')

def non_functional_def(objects):
    if objects['age']>=30:
        print(f'{objects["name"]}: {objects["age"]}')

functional_def(my_resume)
non_functional_def(my_resume)

#exes 2
def return_array(array, add_value):
    if type(array) == tuple:
        array_list = list(array)
        array_list.append(add_value)
        array_tuple = tuple(array_list)
        return f'type tuple:{array_tuple}'
    elif type(array) == list:
        array.append(add_value)
        return f'type list:{array}'
    elif type(array) == dict:
        array['new_objects'] = add_value
        return f'type dict:{array}'

array_values = (1,2,5,99)
print(return_array(array_values, 5))

#exes 3

#map
def find_the_cube(num):
    result_cube = num**3
    return result_cube

array = [1,3,22,77,88]
new_array = map(find_the_cube, array)
print(list(new_array))

#filter
def find_even(num):
    return num%2==0

new_array = filter(find_even, array)
print(list(new_array))

#reduce
def add_numbers(num1, num2):
    return num1+num2

result = reduce(add_numbers, array)
print(result)

#exes 4
def courier_company(street, *args):
    street_names = ['al-farabi', 'sain', 'tashentsky', 'dostyk']
    if street.lower() in street_names:
        if sum(args) <= 10000:
            result_payment = sum(args) + 500
            return result_payment
        else:
            return sum(args)
    else:
        result_payment = sum(args) + 1000
        return result_payment

result = courier_company('sain', 500,8500,1000,1500)
print(result)

#exes 5
def g(*args):
    return sum(*args)

def f(x):
    return x**2

def composition(f, g):
    def func(*args):
        return f(g(*args))
    return func

result = composition(f, g)([1, 5, 15])
print(result)
