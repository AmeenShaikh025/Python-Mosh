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

# names = ['John','Bob','Mosh','Sarah','Marry']
# print(names)
# print(names[0])
# print(names[2])
# print(names[-1])
# print(names[-2])
#
# print(names[2:])#select range of items
# print(names[2:4])
#
# #original list
# print(names)
#
# names[0] = 'Jon'
# print(names)



#--------------------------------------------------------------------------------#

#PGRM: largest number in list (1:59:43)


# numbers = [50, 30, 55]
# largest = numbers[0]

#me

# if numbers[0] > numbers[1] and numbers[0] > numbers[2]:
#     largest = numbers[0]
# elif numbers[1] > numbers[2] and numbers[1] > numbers[0]:
#     largest = numbers[1]
# else:
#     largest = numbers[2]
# print(largest)

#mosh

# numbers = [50, 30, 55, 70]
# largest = numbers[0]
#
# for number in numbers:
#     if number > largest:
#         largest = number
# print(largest)



#--------------------------------------------------------------------------------#


#2D - List (used in data science extensively)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# matrix[0][1]
# print(matrix[0][1]);
#
# print()
# #nested loops
#
# for row in matrix:
#     for item in row:
#         print(item)





#--------------------------------------------------------------------------------#


#LIST METHODS

# numbers = [5, 2, 1, 7, 4, 5, 5]
# numbers.append(20)
# print(numbers)
#
# #---insert() - to insert item anywhere in list
#
# numbers.insert(0, 10)
# print(numbers)
#
# numbers.remove(5)
# print(numbers)
#
# #--- Clear the list
# # numbers.clear()
# print(numbers)
#
# #--- pop()- to remove last item in a list
# numbers.pop()
# print(numbers)
#
#
# #--- index() - to check for existance of an item
#
# print(numbers.index(7))
# #print(numbers.index(5)) #--- This will give an error
#
#
# #--- in() - to check for existance of an item
# print(50 in numbers) #---o/p: Error
#
# #--- count()- count number of occurance
# print(numbers.count(5))
#
# #--- sort() - to sort
# print(numbers.sort()) #--- o/p: none (Return value is none)
# numbers.sort()
# print(numbers) #---prints sorted lists
#
# numbers.reverse() #--- descending order
# print(numbers)
#
# #---copy()
# print()
# numbers2 = numbers.copy();
# numbers.append(20);
# print(numbers)
# print(numbers2)



#PGRM: remove duplicates in a list

# numbers = [10, 20, 30, 5, 5, 5]
# uniques = []
#
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)



#--------------------------------------------------------------------------------#


#TUPLES

#tuples are similar to list butthey are immutable.

#
# numbers = [1, 2, 3]
# number2 = (1,2,3) #Tuples
#
# number2[0] = 15 #Error
# print(number2[0])





#--------------------------------------------------------------------------------#


#UNPACKNG

# coordinates = (1 ,2, 3)
# # x = coordinates[0]
# # y = coordinates[1]
# # z = coordinates[2]
# #
# # above and below code similar
#
# x, y, z = coordinates
#
# print(x)
# print(y)
# print(z)
#
# print()
# coordinates2 = [1, 2, 6]
# x, y, z = coordinates2
# print(z)



#--------------------------------------------------------------------------------#


#DICTIONARIES

#   (KEY VALUE PAIR)
# Name: Ameen
# Email: ammen@123
# Ph: 234

# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
#
# print(customer["name"])
#
# #print(customer["birthDate"]) #error
# print(customer.get("birthDate")) # 'get()' will return none if key is not present
#
#
# #Optional Default value if key does not have a default value
#
# print(customer.get("birthDate","Jan 1 1980"))
#
# customer["name"] = "Jack Smith"
# customer["birthdate"] = "Jan 1 1980"
# print(customer["name"])
# print(customer["birthdate"])


#EXCERSICE (2:23:49)

#Phone: 123
#o/p: One Two Three

# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)




#--------------------------------------------------------------------------------#

#EMOJI CONVERTER


# message = input(">")
# words = message.split(' ') #splits the string when it finds a space
# #Ex: Good morning :)
#
# emojis = {
#     ":)": "\U0001F600",
#     ":D": "\U0001F603"
# }
#
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)


#--------------------------------------------------------------------------------#

#FUNCTIONS

# def greet_user():
#     print('Hi there')
#     print('Welcome aboard')
#
#
# print("Start")
# greet_user()
# print("Finish")

#--------------------------------------------------------------------------------#
#PARAMETERS

# def greet_user(first_name, last_name): #---> Parameter
#     print(f'Hi there {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# print("Start")
# greet_user("John","Smith") #---> Argument (POSITIONAL ARGUMENT)
# print("Finish")


#--------------------------------------------------------------------------------#

#KEYWORD ARGUMENTS

# def greet_user(first_name, last_name): #---> Parameter
#     print(f'Hi there {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# print("Start")
# #greet_user("John","Smith") #---> Argument (POSITIONAL ARGUMENT)
# greet_user(last_name="Smith",first_name="John") #---> Argument (KEYWORD ARGUMENT)
# print("Finish")


#[NOTE: For the most part use positional arguments.
#       But if you are dealing with functions with neumarical arguments use
#       keyword argument to increase the readabilty of the code.


#NOTE: KEYWORD Argument sholud come after POSITIONAL Arguments




#--------------------------------------------------------------------------------#

#RETURN STATEMENTS


# def square(number):
#     return number * number
#     #print( number * number)
#
#
# print(square(3))
#BY DEFAULT EVERY FUNCTION IN PTYTHON RETURNS "None"



#--------------------------------------------------------------------------------#

#CREATING A REUSABLE FUNCTION


# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "\U0001F600",
#         ":D": "\U0001F603"
#     }
#
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input(">")
# print(emoji_converter(message))


#--------------------------------------------------------------------------------#

#EXCEPTION


#Error: (after Running the py)
#exit code: 0 -> means success
#exit code: other than 0 -> program crashed

#TO HANDLE ERRORS: try except


# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be zero.')
# except ValueError:
#     print('Invalid value')


#--------------------------------------------------------------------------------#

#COMMENTS

#dsfdfdf

#print sky is blue (worng, REpetetive , unnecessary comment)
# print("SKy is blue")



#--------------------------------------------------------------------------------#


#CLASSES

#Note: for class name use(Pascal) naming convention, from Pascal langauge.
#ex: EmailClient, Point

#We use classes to define new types. These types can have methods() in body of the class
#and attributes that we can set anywhere in the program.


# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# #print(point2.x) #Error
# point2.x = 30
# print(point2.x)



#--------------------------------------------------------------------------------#


#CONSTRUCTOR

# class Point:
#     #CONSTRUCTOR
#     def __init__(self, x, y):#this method gets called when we create a new point object
#         self.x = x #Self is reference to current object
#         self.y = y
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
# point = Point(10, 20)
# print(point.x) #o/p: 10
#
# point.x = 11
# print(point.x) #o/p:11


#--------------------------------------------------------------------------------#


#Excercise (3:11:39)

# Person
#  -name
#  -talk()


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


p1 = Person('Ameen')
#print(p1.name)
p1.talk()

bob = Person("Bobby")
bob.talk()
