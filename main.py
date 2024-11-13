# Student name
# Current date
# Practice: Positional & Keyword Arguments in Python


# POSITIONAL ARGUMENTS
# Start by writing the code to create the three functions outlined below
# You'll use only positional arguments in the first three functions
# Test your code and correct any errors

# Greet The User
# Write a function that takes two parameters -- first name and age
# Use an f-string to welcome the user by first name and to display his/her age
def user_info (first_name,age):
    print(f'Hello {first_name}, your age is {age}')
user_info('Alex', 17)
# Area of a Rectangle
# Write a function to calculate the area (in square feet) of a rectangle
# Your two parameters will be length and width
# The print statement in the function should display the length, width and area (in square feet) of your rectangle
def math_info (height,width):
    area = (height * width)
    print(f'The height is {height} and the width is {width} so our area would be {area:.2f}')
math_info(9,8)

# Sum of Numbers
# Write a function that finds the sum of three numbers
# Your three parameters will be num1, num2, and num3
# The print statement in the function should display the sum of the three numbers

def addition_info (num1,num2,num3):
    sum = num1 + num2 + num3
    print (f'The sum of {num1}, {num2}, and {num3} is {sum}')
addition_info(10,11,12)
# KEYWORD ARGUMENTS
# Create the three functions outlined below
# In these last three functions, you'll use only keyword arguments 
# Test your code and correct any errors

# Greet By Title
# Write a function that greets the user by title, first name and last name
# Examples of titles include: Mr., Ms., Mrs. and Dr.
# When calling your function, change the order of your keyword arguments so that they don't match the order of your function parameters
def greet_user (title,first_name,last_name):
    print(f'Hello, {title}{first_name} {last_name}')
greet_user(title = 'Mr.', last_name = 'Williams', first_name = 'Alexander')    
# Describe Your Pet
# Write a function that says what type of pet you have and what your pet's name is
# Your function parameters will be pet_type and pet_name
def pet_info(pet_type, pet_name):
    print(f'My pet is a {pet_type} and his name is {pet_name}')
pet_info(pet_type = 'dog', pet_name = 'Otto')
# Updated Function
# Choose any ONE of the first three functions from this project and rewrite it below using keyword arguments

def addition_info (num1,num2,num3):
    sum = num1 + num2 + num3
    print (f'The sum of {num1}, {num2}, and {num3} is {sum}')
addition_info(num1=10,num3=11,num2=12)