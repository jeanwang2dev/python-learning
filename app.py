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

