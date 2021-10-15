# --Type conversion-- ##
patient_name = input("what is the patient name?")
age = 2020 - int( input("what is the patient's birth year?") )
is_new = False
end_str = 'and he is a new patient' if is_new else 'is not a new patient '
result_str = patient_name + ' is ' + str(age) + ' years old ' + end_str
print(result_str)

num_one = input("First: ")
num_two = input("Second: ")
the_sum = float(num_one) + float(num_two)
print('Sum: ' + str(the_sum))

# --String-- ##
course = 'Python for Beginner'
print(course.upper())
print(course)
print(course.find('for'))
print(course.replace('for', '4'))
print('Beginner' in course)

# --Arithmetic Operators-- ##
print( 10 / 3 )
print( 10 // 3)
print (10 % 3)
print ( 10 ** 3)

temperature =19
if temperature > 30:
    print('It\'s a hot day')
    print('Drink a lot of water')
elif temperature > 20: #(20, 30]
    print("It's a nice day")
else:
    print("It's cold")
print('done')

weight = input('Weight: ')
unit = input('(K)g or (L)bs: ')
if unit.lower() == 'k':
    print('Weight in Lbs: ' + str( float(weight)/ 0.45 ) )
elif unit.lower() == 'l':
    print('Weight in Kg: ' + str( float(weight)* 0.45 ) )
else:
    print('Wrong input')

# --While Loop-- ##
i = 1
while i <= 10:
    print(i * '#?')
    i += 1

# -- Lists -- ##
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[1])
print(names[-2])
print(names[1:-1])
print(names[0:3])

numbers=[1, 2, 3, 4, 5, 6]
numbers.append(8)
print(numbers)
numbers.insert(3, -19)
print(numbers)
numbers.remove(5)
print(numbers)
print(-19 in numbers)
print(97 in numbers)
print(len(numbers))

# -- For Loops -- ##
new_numbers = [12, 13, 14, 15, 16]
for item in new_numbers:
    print(item)

# -- range() Function -- ##
my_list = range(10, 20, 2)
print(my_list)
for item in my_list:
    print(item)

# -- Tuples -- ##
my_tuple = (1, 34, 8, 9, 23, 77, 8)
print(my_tuple.count(8))


