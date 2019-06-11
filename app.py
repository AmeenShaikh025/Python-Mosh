# print('Ameen')
# print('0----')
# print(' ||||')
# print('*' * 10)

#Variables

# price = 10
# print(price)
# price = 20
# print(price)
# rating = 4.9
# name = 'Ameen'
# is_published = False
# is_publish = True
#
# pat_name = 'John Smith'
# age = 20
# is_new_patient = True

#Input

# name = input('What is your name? ')
# print('Hi ' + name)
#
# person_name = input('What is your name? ')
# fav_color = input('what is your favorite color ? ');
# print(person_name +' likes '+ fav_color)

#Error(String)
#int()
#float()
#bool()

#conversion

# birth_year = input('Birth Year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# weight_pounds = input('Enter your weight in pounds: ')
# weight_kilogram = float(weight_pounds) * .45
# print(weight_kilogram)

#--------------------------------------------------------------------------------#

#strings

# course = "Python's course for Biginners"
# print(course)

# email = '''
#     Hi John,
#
#     Here is our first email to you
#
#     Thank you
#     The support team
# '''
# print(email)

# course = "Python for Biginners"
# print(course[0]) #p
# print(course[-1]) #s
# print(course[-2]) #r
#
# print(course[0:3]) #Pyt
#
# print(course[0:]) #Python for Biginners ( DEFAULT END INDEX IS -1)
# print(course[1:]) #ython for Biginners
#
# print(course[:5]) #Pytho   ( DEFAULT START INDEX IS 0 )
# print(course[:]) #Python for Biginners
#
# another = course[:]
# print(another)
#
# name = 'Jennifer'
#
# print(name[1:-1]) #ennife

#--------------------------------------------------------------------------------#


#Formatted strings

# first = 'John'
# last = 'Smith'
# # John [smith] is a coder
#
# message = first + '[ ' + last + ' ] is a coder'
# print(message)
#
# msg = f'{first} [{last}] is a coder'
# print(msg)


#--------------------------------------------------------------------------------#

#String Methods

#FUNCTIONS

# course = 'Python for Beginners'
# print(len(course)) #len() is a built in function(General purpouse fun)

#fun specific to strings - METHODS

# print(course.upper()) #o/p: PYTHON FOR BEGINNERS
# print(course) #o/p: Python for Beginners
# print(course.lower())
#
#
# print(course.find('P'))
# print(course.find('o'))# find()- is case sensitive
# print(course.find('O')) #o/p: -1 (not found)
#
# print(course.find('Beginners')) #o/p: 11
#
# print(course.replace('Beginners','Absolute Beginners')) #o/p: Python for Absolute Beginners
# print(course.replace('beginners','Absolute Beginners')) #o/p: will be 'Python for Beginners'
# print(course.replace('P','J'))
#
# print('Python' in course)
# print('python' in course)

# len(), upper(), lower(), title(), find(), replace(), '..' in course

#--------------------------------------------------------------------------------#

#Airthematics operator

# print(10+3)
# print(10-3)
# print(10*3)
#
# # 2- DIVISON OPERATORS
# print(10/3) #FLOATING POINT OUTPUT
# print(10 // 3) # INTEGER VALUE
#
# print(10%3)
#
# #exponent(power)
# print(10**3)
#
#
# #Augmented assignment operator
#
# x = 10
# x += 3 #OR (x = x + 3)
# print(x)


#--------------------------------------------------------------------------------#

#Operator precedence

#x = 10 + 3 * 2  # o/p: 16
#x = 10 + 3 * 2 ** 2  # o/p: 22

# x = (10 + 3) * 2 ** 2  # o/p: 52
# print(x)

# ORDER
# Parenthesis
#exponentiation 2 ** 3
#multiplication or division
#addition or substraction




#--------------------------------------------------------------------------------#

#MATH FUNCTIONS

#IMPORT MATH MODULE TO DO COMPLEX MATHEMATICAL OPERATIONS

# import math
#
# x = 2.9
# y = -2.9
#
# print(math.ceil(2.9))
# print(math.floor(2.9))

# Python3 math module is different from python2 math module

# print(round(x))
# print(abs(y))


#--------------------------------------------------------------------------------#

# IF STATEMENTS

#(Shift + tab) - To remove indentation
# elif =-> else if

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("wear warm clothes")
# else:
#     print("It's a lovely day")
#
# print("Enjoy your day")


# Example (1:05:04)

# price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = .1 * price
# else:
#     down_payment = .2 * price
# print(f"Down Payment: ${down_payment}")



#--------------------------------------------------------------------------------#


#LOGICAL OPERATORS (OR , AND, NOT)

# has_high_income = False
# has_good_credit = True
#
# if has_high_income and has_good_credit:
#     print('Eligable for loan')
#
# if has_high_income or has_good_credit:
#     print('Eligable for anything')
#
# has_criminal_record = False
#
# if has_good_credit and not has_criminal_record:
#     print('Eligable')



#--------------------------------------------------------------------------------#


#Comparison Operator(> , < ,==, <=, >=, !=)



# temprature = 30
#
# if temprature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

#Exaple (1:14:36)

#name = "Ameen"
# name = input("Enter your name: ")
#
# name_char_count = len(name)
#
# if name_char_count < 3:
#     print('Name must be atleast 3 characters long')
# elif name_char_count > 50:
#     print('Name can be maximum 50 characters long')
# else:
#     print('name looks good')






#--------------------------------------------------------------------------------#


#Project: Weight Converter

# weight = input('Weight: ')
# unit = input('(L)bs or (K)g: ')
#
# in_kg = float(weight) * 2
# in_lbs = float(weight) * .45
#
# # if unit == 'l' or unit == 'L':
# # (OR)
# if unit.upper() == 'L':
#     print(f'You are {in_lbs} kilos')
#
# elif unit == 'k' or unit == 'K':
#     print(f'You are {in_kg} pounds')



#--------------------------------------------------------------------------------#


#WHILE LOOPS

# i = 1
# while i <=3:
#     #print(i)
#     print('*' * i) #When you multiply string by number: you'll get multiple strings Ex: **, **** etc..
#     i = i + 1
# print("Done")


#--------------------------------------------------------------------------------#

#Guessing Game


# guess = int(input('Guess: '))
# counter = 1
#
# while guess == 9:
#     print('You Win!!!')
#
#     counter = counter + 1
#     if counter == 3:

#----Mosh's Code-----

# secret_number = 9
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Win!!!')
#         break
# else:
#     print("Sorry you've failed!") #This statement will execute if the guess_count fails


#--------------------------------------------------------------------------------#

#IMPORTANT

#CAR GAME

#---Ameen Code---
# value_entered = input()
#
# if value_entered.upper() == 'HELP':
#     print('start - to start the car')
#     print('stop - to stop the car')
#     print('quit - to quit the car')
#     car_option = input()
#     if car_option.upper() == 'START':
#         print('Car started... ready to go!')
#     elif car_option.upper() == 'STOP':
#         print('Car stopped')
#     elif car_option.upper() == 'QUIT':
#         print()



#---Mosh's code---

# command = ""
# start_cont = 1
#
# while True:
#     command = input("> ").lower()
#     if command == "start":
#
#         if start_cont == 1:
#             print('Car started... ready to go!')
#             start_cont += 1 #WE CAN USE BOOLEAN VAULES INSTEAD OF COUNTER - TO CHECK IF CAR HAS STARTED
#         else:
#             print("Car is already started")
#     elif command == 'stop':
#         if start_cont == 2:  #WE CAN USE BOOLEAN VAULES INSTEAD OF COUNTER - TO CHECK IF CAR HAS STOPPED
#             print('Car stopped')
#             start_cont +=1
#         else:
#             print('Car is already stopped')
#     elif command == 'help':
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit the car
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry I dont't understand that!")




#--------------------------------------------------------------------------------#


#FOR LOOPS


# for item in 'Python':
#     print(item)
#
# for item in ['Mosh','Ameen','Aman']:
#     print(item)
#
# for item in [1,2,3,4]:
#     print(item)

#---IN PYTHON TO SPECIFY RANGE VALUES WE HAVE "RANGE fUNCTION" - FOR LARGE LIST OF NUMBERS


# for item in range(10):
#     print(item) #10 - is not included

# for item in range(5, 10): #5 to 9 numbers
#     print(item)

#--- step - for range()

# for item in range(5, 10, 2): # 2 - step for numbers i.e, 5,7,9
#     print(item)

#--------------------------------------------------------------------------------#

#FOR LOOP - EXCERCISE

#1:45:30

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(total)


#--------------------------------------------------------------------------------#


#NESTED LOOPS

#using nested loops we can generate list of coordinates
#Ex: (x,y) => (0,1) etc..

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')
#
#
# #challenge (1:51:34) PRINT - F
#
# numbers = [5, 2, 5, 2, 2]
# count = len(numbers)
#
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)
#
# # print -  L
#
# numbers = [2, 2, 5]
# count = len(numbers)
#
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)


#--------------------------------------------------------------------------------#

#LISTS








