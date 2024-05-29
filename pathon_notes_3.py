# 3. Nested Loops--
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop".

# Example1--
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()
# Example2--
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x, y)
#
# Example3--
# for i in range(1, 7):
#     for j in range(i):
#         print(i, end=' ')

# Example4--
# for i in range(1, 7):
#     for j in range(i):
#         print(i,end= " ")
#     print("")

# Control Statements in Python--
# Break statement
# Continue statement
# Pass statement

# # Break statement
# In Python, the break statement is employed to end or remove the control from the loop that contains
# the statement. It is used to end nested loops (a loop inside another loop), which are shared with both
# types of Python loops. The inner loop is completed, and control is transferred to the following statement
# of the outside loop.
# It is used with both the while and the for loops, especially with nested loops (loop within a loop)
# to quit the loop. It terminates the inner loop and control shifts to the statement in the outer loop.
# Example1--
# char = "python"
# for i in char:
#     if (char == 'h'):
#         break
#     print('Current character: ', char)

#
# Example2--(from my side)

# age=32
# while age>18:
#     break
# print('You can vote')

#
# age=int(input("please inter your age="))
# while True:
#     if age>18:
#         print("you are eligible for vote")
#         break
#     else:
#         print("you are not eligible for vote")
#         break

# Continue statement--
# When a program encounters a continue statement in Python, it skips the execution of the current iteration
# when the condition is met and lets the loop continue to move to the next iteration. It is used to
# continue running the program even after the program encounters a break during execution.
# Example1--
#
# for char in 'Python':
#     if (char == 'h'):continue
#     print('Current character: ', char)

# Example2--
# for letter in 'Credence  Automation':
#     if letter == ' ':continue
#     print ('Letters: ', letter)

# Example3--
# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':continue
#     print('Current Letter :', letter)

# Pass statement--
# The pass statement is a null operator and is used when the programmer wants to do nothing when the
# condition is satisfied. This control statement in Python does not terminate or skip the execution, it simply
# passes to the next iteration.A loop cannot be left empty otherwise the interpreter will throw an error and
# to avoid this, a programmer can use the pass statement.A coder can put the pass statement to prevent the
# interpreter from throwing an error when a loop or a code block is left empty.

# Example1--
# for char in 'Python':
#     if (char == 'h'):pass
#     print('Current character: ', char)


# Pattern Printinng examples using for loop--
# rows = 5
# for i in range(1, rows):
#     # nested loop for each column
#     for j in range(1, i + 1):
#         print(j, end=' ')
#         # new line after each row
#     print(" ")

# rows = 5
# for i in range(0, rows):
#     # nested loop for each column
#     for j in range(0, i + 1):
#         # print star
#         print("*", end=' ')
#         # new line after each row
#     print(" ")
# ------------------------------Might be reffer yusuf sir's Notes(From page no.-234) along with bellow notes----------------------------------------------------------------------------------------
# Python Functions
# Python Functionsis a block of statements that return the specific task.The idea is to put some commonly
# or repeatedly done tasks together and make a function so that instead of writing the same code again and
# again for different inputs, we can do the function calls to reuse code contained in it over and over again.
#
# Benefits -
# Code Reusability
# Code Readability
# There are two types of function in Python programming:--
# •Standard library functions-These are built-in functions in Python that are available to use.
# Example--
# •print()-prints the string inside the quotation marks
# •len()-returns the length
# •User-defined functions-We can create our own functions based on our requirements
#
# The syntax to declare a function is:
# def function_name(arguments):
#     functionbody
#     return
# Here,•def-keyword used to declare a function
# •function_name-any name given to the function
# •arguments-any value passed to function
# •return(optional) -returns value from a function
#
# Example: Python Function
# def greet():
#     print('HelloWorld!')
# #callthefunction
# greet()
# print('Outsidefunction')
# Output
# HelloWorld!
# Outsidefunction

# Function Arguments/Parameters--
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments
# as you want, just separate them with a comma.

# Example1--
# def my_function(fname):
#     print(fname)
# my_function("Yusuf")
#
# Example2--
# def my_function(fname,lname):
#     print(fname," ", lname)
# my_function("Yusuf","Tamboli")
#
# From a function's perspective:--
# An argument is the value that is sent to the function when it is called.
# A parameter is the variable listed inside the parentheses in the function definition.

# Passing a List as an Argument--
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# Example--
# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ["apple","banana","cherry"]
# my_function(fruits)

# return Statement--
# We write a return statement in a function to leave a function and give the calculated value when a defined
# function is called.To let a function return a value, use the return statement:
# Example1--
# def arithmatic(a,b):
#     c=a+b
#     d=a-b
#     e=a*b
#     f=a/b
#     return c,d,e,f
# print(arithmatic(20,10))

# Example2--
# def arithmatic(a,b):
#     c=a+b
#     d=a-b
#     e=a*b
#     f=a/b
#     return c,d,e,f
# result= (arithmatic(20,10))
# print(result)

# Example3--
# def my_function(x):
#     return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# Recursive Function--
# A recursive function is a function that repeats its behavior until a specified condition is met.
# In Python, we know that afunctioncan call other functions. It is even possible for the function to call
# itself.These types of construct are termed as recursive functions.
# Example1--
# def greet():
#     print("Hello")
#     greet()
# greet()

# Example2--
# def count(num):
#     if (num<=0):
#         print("Stop")
#     else:
#         print(num)
#         count(num-1)
# count(5)
#
# Fibonacci Sequence--
# It is a most famous mathematical problem and sometime also asked in interview at entry level jobs.
# In this sequence, each number in the sequence is the sum of the two numbers that precede it.
# The series will be 0, 1, 1, 2, 3, 5, 8,....so on.Suppose  we  want 6thelement of Fibonacci series,
# the preceding two elements will be 5 and 4 -
# 1.fib(6)=fib(5)+fib(4)=>5+3=8
# 2.fib(5)=fib(4)+fib(3)=>2+3=5
# 3.fib(4)=fib(3)+fib(2)=>2+1=3
# 4.fib(3)=fib(2)+fib(1)=>1+1=2
# 5.fib(2)=fib(1)+fib(0)=>1+0=1
# 6.fib(1)=fib(0)+fib(1)=>0+1=1
# 7.fib(0)=0
# The sequence Fn is defined by the recurrence relation as below.
# 1.Fn=Fn-1+Fn-2
# With the seed values -
# 1.F0=0 and F1=1

# Python Variable Scope--
# PythonGlobalvariablesare those which are not defined inside any function and have a global scope whereas
# Pythonlocalvariablesare those which are defined inside a function and their scope is limited to that
# function only. In other words, we can say that local variables

# message='Hello'
# def greet():
#     print('Local',message)
# greet()
# print('Global',message)

# This means that a global variable can be accessed inside or outside of the function.

# let's try to access a global variable from the inside of a function,--
# c=1
# def add():
#     print(c)
# add()
# if we try to modify the global variable from inside a function it shows error--
# c=1
# def add():
#     c = c+1
#     print(c)
# add()
#
# This is because we can only access the global variable but cannot modify it from inside the function.
# The solution for this is to use the global keyword.

# c = 1
# def add():
#     global c
#     c = c + 1
#     print(c)
# add()

# Global in Nested Functions In Python, we can also use the global keyword in a nested function. For example,
# def outer_function():
#     num=20
#     def inner_function():
#         global num
#         num=25
#     print("Before calling inner_function():",num)
#     inner_function()
#     print("Aftercallinginner_function():",num)
# outer_function()
# print("Outsidebothfunction:",num)
# Python Module--
# A Python module is a file containing Python definitions and statements. A module can define functions, classes,
# and variables. A module can also include runnable code. Grouping related code into a module makes the code
# easier to understand and use. It also makes the code logically organized.
# Create a simple Python module Let’s create a simple Module1.py in which we define 4 functions, add,
# sub,muland
# div.def
#     add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a/b)
# Import Module in Python We can import the functions, and classes defined in a module to another module using
# the import statement in some other Python source file.When the interpreter encounters an import statement, it
# imports the module if the module is present in the search path. A search path is a list of directories that
# the interpreter searches for importing a module. For example, to import the module Module1.py, we need to put
# the following command at the top of the script.
# Syntax of Python Import-
# import Module1
# Note:This does not import the functions or classes directly instead imports the module only. To access the
# functions inside the module the dot(.) operator is used.
# import Module1
# Module1.add(20,10)
# Module1.sub(20,10)
# Module1.mul(20,10)
# Module1.div(20,10)

# The from-import Statement in Python
# Python’s from statement  lets  you  import  specific  attributes  from  a  module  without importing the
# module as a whole.Importing specific attributes from the module Here, we are importing specific add and
# dev attributes from the math module.
# from Module1 import add,div
# add(20,10)
# div(20,10

# Import all Names --
# The  *  symbol  used  with  the  from  import  statement  is  used  to  import  all  the names from a
# module to a current namespace.
# Syntax:--
# from Module1 import *

# Python Packages--
# APythonmodulemay contain several classes, functions, variables, etc. whereas a Python package can contains
# several module. In simpler terms a package is folder that contains various modules as files.
# Understanding __init__.py--
# __init__.py helps the Python interpreter to recognise the folder as package. It also specifies the resources
# to be imported from the modules. If the __init__.py is empty this means that all the functions of the modules
# will be imported. We can also specify the functions from each module to be made available.
# Creating Package--
# Let’s create a package named demopack1 that will contain two modules mod1 and mod2. To create this module
# follow the below steps –•Create a folder named demopack1.•Inside this folder create an empty Python file
# i.e. __init__.py•Then create two modules mod1 and mod2 in this folder.
# The hierarchy of the our package looks like this --
# __init__.py
# Mod1.py
# def gfg():
#     print("Welcome to GFG")
# Mod2.py
# def sum(a, b):
#     print( a+b)
# Import Modules from a Package--
# We can import these modules using the from...import statement and the dot(.) operator.Syntax:import
# package_name.module_nameExample: Import Module from packageWe will import the modules from the above
# created package and will use the functions inside those modules.
# from demopack1 import mod1
# from demopack1 import mod2
# mod1.gfg()
# mod2.sum(20,10)

# When a Python program meets an error, it stops the execution of the rest of the program. An  error  in
# Python  might  be  either  a syntax error of  an  expression  or  a  Python exception.
#
# What is an Exception?--
# An exception in Python is an incident that happens while executing a program commands  to  be  disrupted.
# When a Python code comes across a condition it can not handle, it raises an exception. An object in Python
# that describes an error is called an exception.When  a  Python  code  throws  an  exception,  it  has
# two  options:  handle  the  exception immediately or stop and quit.
# SyntaxError:--
# As the name suggests this error is caused by the wrong syntax in the code. It leads to the termination of
# the program.
# # SyntaxError Example--
# string="PythonExceptions"
# for s in string:
#     if (s != "o":
#         print(s)
# Output:--
#     if (s != o:
#             ^
# SyntaxError: invalid syntax
# The arrow in the output shows where the interpreter encountered a syntactic error. There was one unclosed
# bracket in this case. Close it and rerun the program.
# NameError Example--
# string = "Python Exceptions"
# for s in string1:
#     if ('s' != 'o'):
#         print(s)
# Output--# NameError: name 'string1' is not defined. Did you mean: 'string'?
# We  encountered  an  exception  error  after  executing  this  code.  When  syntactically  valid Python code
# produces an error, this is the kind of error that arises. The output's last line specified  the  name  of
# the  exception  error  code  encountered. Instead  of  displaying  just "exception  error",  Python  displays
# information  about  the  sort  of  exception  error  that occurred. It was a NameError in this situation.
# Different types of exceptions in python:--
# •SyntaxError:-This exception is raised when the interpreter encounters a syntax error in the code, such as a
#               misspelled keyword, a missing colon, or an unbalanced parenthesis.
# •TypeError:-  This exception is raised when an operation or function is applied to an object of the wrong type,
#               such as adding a string to an integer.
# •NameError:-  This exception is raised when a variable or function name is not found in the current scope.
# •IndexError:- This exception is raised when an index is out of range for a list, tuple,
#               or other sequence types.
# •KeyError:-   This exception is raised when a key is not found in a dictionary.
# •ValueError:- This exception is raised when a function or method is called with an invalid argument or
#               input, such as trying to convert a string to an integer when the string does not represent
#               a valid integer.
# •AttributeError:- This exception is raised when an attribute or method is not found on an object, such
#                 as trying to access a non-existent attribute of a class instance.
# •IOError:-   This exception is raised when an I/O operation, such as reading or writing a file, fails due
#               to an input/output error.
# •ZeroDivisionError:- This exception is raised when an attempt is made to divide a number by zero.
# •ImportError:- This exception is raised when an import statement fails to find or load a module.
# These are just a few examples of the many types of exceptions that can occur in Python. It’s important to
# handle exceptions properly in your code using try-except blocks or other error-handling techniques,
# in order to gracefully handle errors and prevent the program from crashing.
# * Exception Handling in Python
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try-and except blocks.
# try :
#     # statements in try block
# except :
#     # executed when error in try block
# You can specify the type of exception after the except keyword. The subsequent block will be executed only
# if the specified exception occurs. There may be multiple except clauses  with  different  exception  types
# in  a  single  try  block.  If  the  type  of  exception doesn't match any of the except blocks, it will
# remain unhandled and the program will terminate.
# Example1)--
# try:
#     a = 5
#     b = '0'
#     print(a / b)
# except:
#     print('Some error occurred.')
# print("Out of try except blocks.")
# Output-
# Some error occurred.
# Out of try except blocks.

# # Example2)--
# x = 5
# y = "hello"
# try:
#     z = x + y
# except TypeError:
#     print("Error: cannot add an int and a str")
# # OutputError:- cannot add an int and a str

# # Example3)--
# try:
#     even_numbers = [2,4,6,8]
#     print(even_numbers[5])
# except ZeroDivisionError:
#     print("Denominator cannot be 0.")
# except IndexError:
#     print("Index Out of Bound.")
# Output: Index Out of Bound

# Example4)--
# try:
#     a=5
#     b='0'
#     print(a+b)
# except TypeError:
#     print('Unsupported operation')
# print("Out of try except blocks")
# Output-
# Unsupported operation
# Out of try except blocks
# Example5)--
# try:
#     a=5
#     b=0
#     print(a/b)
# except TypeError:print('Unsupported operation')
# except ZeroDivisionError:print('Division by zero not allowed')
# print('Out of try except blocks')
# Output--
# Division by zero not allowed
# Out of try except blocks
# However, if variable b is set to '0', TypeError will be encountered and processed by corresponding except block.

# def AbyB(a , b):
#     try:
#         c = ((a+b) / (a-b))
#     except ZeroDivisionError:
#         print ("a/b result in 0")
#     else:print (c)
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)
# else and finally--
# In  Python,  keywords else and finally can  also  be  used  along  with  the  try  and  except clauses.
# While the except block is executed if the exception occurs inside the try block, the else block gets
# processed if the try block is found to be exception free.
# Syntax:
# try:
#     # statements in try block
# except:
#     # executed when error in try block
# else:
#     # executed if try block is error-free
# finally:
#     # executed irrespective of exception occured or not

# Example: try, except, else, finally blocks(try to use diffrant input like 4/0 or 4/2 or4/'rtp' and so on---
# try:
#     print('try block')
#     x=int(input('Enter a number: '))
#     y=int(input('Enter another number: '))
#     z=x/y
# except ZeroDivisionError:
#     print("except ZeroDivisionError block")
#     print("Division by 0 not accepted")
# else:
#     print("else block")
#     print("Division = ",z)
# finally:
#     print("finally block")
#     x=0
#     y=0
# print("Out of try, except, else and finally blocks.")

# Raise an Exception--
# Python also provides theraisekeyword to be used in the context of exception handling. It  causes  an
# exception  to  be  generated  explicitly.If a condition does not meet our criteria but is correct according
# to the Python interpreter, we can intentionally raise an exception using the raise keyword.
# how to raise an exception in Python --
# Example1)--
# num=[3,4,5,7]
# if len(num)>3:
#     raise Exception(f'Length of the given list must be less than or equal to 3 but is {len(num)}')

# Example2)--
# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# Example3)--
# try:
#     x=int(input('Enter a number upto 100: '))
#     if x >100:
#         raise ValueError(x)
# except ValueError:
#     print(x,"is out of allowed range")
# else:
#     print(x,"is within the allowed range")
#
# Advantages of Exception Handling:--
# •Improved programre liability:- By handling exceptions properly, you can prevent your program from crashing or
#                                 producing incorrect results due to unexpected errors or input.
# •Simplified error handling:-   Exception handling allows you to separate error handling code from the main
#                                program logic, making it easier to read and maintain your code.
# •Cleaner code:-   With exception handling, you can avoid using complex conditional statements to check for
#                   errors, leading to cleaner and more readable code.
# Disadvantages of Exception Handling:--
# •Performance overhead:-Exception handling can be slower than using conditional statements to check for
#                        errors, as the interpreter has to perform additional work to catch and handle the
#                        exception.
# •Increased code complexity:- Exception handling can make your code more complex, especially if you have to
#                             handle multiple types of exceptions or implement complex error handling logic.
# Python File Handling--
# Sometimes,  it  is  not  enough  to  only  display  the  data  on  the  console.  The  data  to  be
# displayed may be very large, and only a limited amount of data can be displayed on the console  since
# the  memory  is  volatile,  it  is  impossible  to  recover  the  programmatically generated data again
# and again.The file handling plays an important role when the data needs to be stored permanently into the
# file.We can access the stored information (non-volatile) after the program termination.
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////////
# f = open("hop.txt","w")
# f.write(" see you agian")
# f.close()
# f = open("hop.txt",'r')
# print(f.read())

# f = open("hlopt.txt","x")
# import os
# os.remove("hlopt.txt")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\///////////////////////////////////////////////////////////////
# The key function for working with files in Python is theopen()function.Theopen()function takes two
# parameters; filename, andmode.There are four different methods (modes) for opening a file:
# "r"-Read -Default value. Opens a file for reading, error if the file does not exist
# "a"-Append -Opens a file for appending, creates the file if it does not exist
# "w"-Write -Opens a file for writing, creates the file if it does not exist
# "x"-Create -Creates the specified file, returns an error if the file exists

# To open the file, use the built-inopen()function.
# The open()function returns a file object, which has aread()method for reading the content of the file:
# Example--
# f =open("hop.txt.txt","r")
# print(f.read())
# f the file is located in a different location, you will have to specify the file path, like this:
# Example --
# Open a file on a different location:-
# f =open("C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Stanalone\\hop.txt","r")
# print(f.read())
# Read Only Parts of the File By default the read()method returns the whole text, but you can also specify how
# many characters you want to return:
# Example--
# Return the 5 first characters of the file:
# f =open("hop.txt","r")
# print(f.read(5))
# Read LinesYou can return one line by using the readline()method:
# Example-Read one line of the file:
# f =open("hop.txt","r")
# print(f.readline())
# By calling readline()two times, you can read the two first lines:
# Example--
# Read two lines of the file:
# f =open("hop.txt","r")
# print(f.readline())
# print(f.readline())
# By looping through the lines of the file, you can read the whole file, line by line:
# Example--Loop through the file line by line:
# f =open("hop.txt","r")
# for x in f:print(x)
# Close Files--
# It is a good practice to always close the file when you are done with it.
# Example--Close the file when you are finish with it:
# f =open("hop.txt","r")
# print(f.readline())
# f.close()
# Write to an Existing File-
# To write to an existing file, you must add a parameter to theopen()function:
# "a"-Append -will append to the end of the file
# "w"-Write -will overwrite any existing content
# Example--Open the file "demofile2.txt" and append content to the file:
# f =open("hop.txt","a")
# f.write("Now the file has more content!")
# f.close()
# open and read the file after the appending:
# f =open("hop.txt","r")
# print(f.read())

# Open the file "demofile3.txt" and overwrite the content:
# Example--
# f =open("hop.txt","w")
# f.write("Woops! I have deleted the content!")
# f.close()
# open and read the file after the overwriting:
# f =open("hop.txt","r")
# print(f.read())
# Create a New File--
# To create a new file in Python, use the open()method, with one of the following parameters:
# "x"-Create -will create a file, returns an error if the file exist
# "a"-Append -will create a file if the specified file does not exist
# "w"-Write -will create a file if the specified file does not exist
# Example--Create a file called "newjet.txt":
# f =open("newjet.txt","x")
# # Result: a new empty file is created!
# Delete a File--
# To delete a file, you must import the OS module, and run it's os.remove()function:
# Example--
# Remove the file "newjet.txt":
# import os
# os.remove("newjet.txt")
# Renaming the file--
# import os
# os.rename("hop.txt", "file4.txt")
# The with statement--
# The advantage of using with statement is that it provides the guarantee to close the file.
# so It is always suggestible to use thewithstatement in the case of files because, if the break, return,
# or exception occurs in the nested block of code then it automatically closes the file, we don't need to
# write the close()function. It doesn't let the file to corrupt
# Example--
# with open("fo.txt",'w') as f:
#     content = f.write("Yusuf");
#     f.close()
# with open("fo.txt",'a') as f:
#     f.write("Tushar")
#     f.close()
# with open("fo.txt",'r') as f:
#     print(f.read())

# Handling Python FileNotFoundError;-
# If you have received the error “FileNotFoundError: [WinError 2] The system cannot find the file specified”,
# it means that there is no file present at the path you specified.
# Solution –Python FileNotFoundErrorThere are two ways in which you can handle FileNotFoundError.
# •Use try-except and handle FileNotFoundError
# •Check if file is present, and proceed with the file operation accordingly.
# First Way--
# import os
# try:
#     os.remove('fo.txt')
#     print('The file is removed.')
# except FileNotFoundError:
#     print('The file is not present.')

# Second Way--
# import os
# if os.path.exists("fo.txt"):
#     os.remove("fo.txt")
# else:print("The file does not exist")

# Python OOPS Concepts--
# What are Python OOPs Concepts?--
# Major OOP (object-oriented programming) concepts in Python include Class, Object, Method, Inheritance,
# Polymorphism, Data Abstraction, and Encapsulation.
# What are Classes and Objects?--
# A class is a collection of objects.
# Class is defined under a “Class” Keyword.
# lass contains variables (attributes/state) and methods (behaviour)logic will be included in the methodwe
# can create variables and methods in class.We can create any no of objects for a class.
# class Myclass:
#     def myfun(self):  # self keyword-it says myfun method belongs to Myclass
#         pass
#     def display(self,name): # self is just keyword which say dispay is method belongs  Myclass, name is argument.
#         print("name is:", name)
# # Python supports both. with or without class we can use functions.
# #  now if we want to access above class we need to create an object
# mc=Myclass()  # Myclass is actual object and mc is reference variable means vraible which holds
#                # Myclass object
# mc.myfun() # kuch nhi milegamc.
# mc.display("Yusuf") # name is: Yusuf
# instance method and static method--
# instance method--
# class Myclass1():
#     def m1(self):  # Instance Method -When i create a method withing a class by default it is instance method
#         print("We are printing Instance Method")
# mc1 = Myclass1() # mc1 is instance variable which will store Myclass1 Object
# mc1.m1() # We are printing Instance Method
# static method with parameters--
# class Myclass1():
#     @staticmethod
#     def m2(self):
#         print("We are printing Static Method")
#         print(self)
#
# Myclass1().m2("Anil")
# static method without parameters--
# class Myclass1():
#     def m1(self):
#         print("We are printing Instance Method")
#     @staticmethod
#     def m2(): #Static Method
#         print("We are printing Static Method")
# mc1 = Myclass1()
# mc1.m1()
# Myclass1().m2()
# Difference between instance and static  method--
# static method -
# @staticmethod keyword use is manadatory,
# dont need to create an object to access that method,
# no need to use self, if u use then it will be taken as argument then u have to pass the arguments
# while accessing it.
# instance method -
# @staticmethod keyword use is not manadatory,
# must need to create an object to access that method,
# must need to use self, if u use then it will be taken as keywordwhich will say m1 method is part of Myclass1
# declaring variables inside the class--
# class Myclass2:
#     a = 100  # Class variable
#     b = 200  # class Variable
#     def add(self):
#         # print(a+b) # It will not add becz a and b are not defined in add method
#         print(self.a+self.b) # it will add becz self will used to access the class variables
#     def mul(self):
#         print(self.a*self.b)
# mc2 = Myclass2()
# mc2.add()
# mc2.mul()

# # local variables, global variables and class variables--
# i,j = 100,200  # Global Variables
# class Myclass3:
#     a,b= 10,20 # Class variables
#     def add(self,x,y):
#         print(x+y) # accessing x and y are Local Variables but we havent defined thats why it will not
#                    # add values.
#         print(self.a+self.b)
#         print(i+j)
# mc3 = Myclass3()
# mc3.add(1000,2000)

# local variables, global variables and class variables with same name--
# a,b=100,200 # Global variables
# class Myclass4:
#     a,b=10,20 # Class Variables
#     def add(self,a,b): # Local Variables
#         print(a+b) # access local with normal print
#         print(self.a+self.b) # access class with self keyword
#         print(a+b) # access local with normal print
#         print(globals()['a']+globals()['b']) # access global with globals method
# mc4=Myclass4()
# mc4.add(1000,2000)

# creating multiple objects for same class--
# class Myclass5:
#     def add(self,x,y):
#         print(x+y)
# mc5= Myclass5()
# mc6= Myclass5()
# print(id(mc6))#--check memory locations of objects

# Constructor--(if you need this topic in brief,go with yusuf sir's notes (page no.- 308))
# Constructors are generally used for initializing an object

# Python Inheritance--
# One of the core concepts in object-oriented programming (OOP) languages is inheritance. It is a mechanism
# that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a
# class from another class. Inheritance is the capability of one class to derive or inherit the properties
# from another class.Inheritance allows us to define a class that inherits all the methods and properties
# from another class.
#     Parent classis the class being inherited from, also called base class.
#     Child classis the class that inherits from another class, also called derived class.
#     Parent class -superclassBaseclass
#     Child class -subclass Derived Class
# Benefits of inheritance are:
# •It provides the reusability of a code. We don’t have to write the same code again and again. Also,
# it allows us to add more features to a class without modifying it.
# •It is transitive in nature, which means that if class B inherits from another class A, then all the
# subclasses of B would automatically inherit from class A.
# •Inheritance offers a simple, understandable model structure.
# Different types of Inheritance:
#   •Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
# We saw an example above.
#   •Multiple inheritances: When a child class inherits from multiple parent classes, it is called
# multiple inheritances.
#   •Multilevel inheritance: When we have a child and grandchild relationship.
#   •Hierarchical inheritance: More than one derived class are created from a single base.
#   •Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of
# more than one type of inheritance.

# 1.Single inheritance: When onlychild class inherits from only one parent class, it is called single
# inheritance
# Example-1)--
# class A:
#     def m1(self):
#         print("This m1 method is from Parent A")
#         #a1=A()#a1.m1()  # Parent class object call m1
# class B(A):
#     pass
# b1=B()
# b1.m1() # Child class object call m1

# Example-2)--
# class A:
#     def m1(self):
#         print("This m1 method is from Parent A")
# class B(A):
#     def m2(self):
#         print("This m2 method is from Parent B")
# a1=A()
# a1.m1()  # Parent class object call m1
# b1=B()
# b1.m2() # Child class object call child method m2
# b1.m1() # Child class object call parent method m1

# Example-3)--
# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     x,y=10,20
#     def m2(self):
#         print(self.x + self.y)
# bobj=B()
# bobj.m2()
# bobj.m1()

# 2.Multilevel inheritance: When we have a child and grandchild relationship.--
# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     x,y=10,20
#     def m2(self):
#         print(self.x + self.y)
#
# class C(B):
#     i, j = 1000, 2000
#     def m3(self):
#        print(self.i + self.j)
# aobj = A()
# aobj.m1()
# # aobj.m2() # invalid
# # aobj.m3() # invalid
# bobj=B()
# bobj.m2()
# bobj.m1()
# # bobj.m3() # invalid
# cobj=C()
# cobj.m3()
# cobj.m2()
# cobj.m1()
# 3.Hierarchical inheritance-- More than one derived class are created from a single base.
# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B(A):
#     def m2(self):
#         print("This is m2 method of Child B")
# class C(A):
#     def m3(self):
#         print("This is m3 method of GrandChild C")
# b1=B()
# b1.m1()
# b1.m2()
# c1=C()
# c1.m1()
# c1.m3()
# #c1.m2()  # invalid
# 4. Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple
# inheritances
# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B():
#     def m2(self):
#         print("This is m2 method of Child B")
# class C(A,B):
#     def m3(self):
#         print("This is m3 method of GrandChild C")
# a1=A()
# a1.m1()
# # a1.m2() #invalid
# b1=B()
# # b1.m1() #invalid
# b1.m2()
# c1=C()
# c1.m1()
# c1.m2()
# c1.m3()

# The super() Method in Python Inheritance--
# Previously we saw that the same method in the subclass overrides the method in the superclass.However,
# if we need to access the superclass method from the subclass, we use the super()method.
# Super() can be used in 3 ways
# 1. to invoke the parent class methods(this point will discuss in this notes and remaing 2 and 3 point we are
# not discuss in this notes if you see 2nd 3rd point in brief go with yusuf sir's notes - page no_316)
# 2. to invoke the parent class variables
# 3. to invoke the parent class constructor
#
# 1. to invoke the parent class methods-
# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B(A):
#     def m2(self):
#         print("This is m2 method of Child B")
#         super().m1()
# bobj=B()
# bobj.m2()
#

# Polymorphismin Python--
# WhatisPolymorphism:The word polymorphism means having many forms. In programming, polymorphism means the
# same function name (but different values) being used for different types.
# Example of inbuilt polymorphic functions:--
# #len() being used for a string
# print(len("geeks"))
# # len() being used for a list
# print(len([10, 20, 30]))

# Examples of user-defined polymorphic functions:--
# def add(x, y, z = 0):
#     return x + y+z
# print(add(2, 3))
# print(add(2, 3, 4))

# Polymorphism with class methods:--
# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#     def type(self):
#         print("India is a developing country.")
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#     def language(self):
#         print("English is the primary language of USA.")
#     def type(self):
#         print("USA is a developed country.")
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()
# Polymorphism with Inheritance:--
# In Python, Polymorphism lets us define methods in the child class that have the same name as the methods
# in the parent class. In inheritance, the child class inherits the methods from the parent class. However,
# it is possible to modify a method in a child class that it has inherited from the parent class. This is
# particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child
# class. In such cases, we re-implement the method in the child class. This process of re-implementing a
# method in the child class is known as Method Overriding.
# Example-1)--
# class A:
#     def m1(self,a=100,b=200):
#         print(a+b)
# class B(A):
#     def m1(self,x=10,y=20):
#         print(x+y)
#         super().m1()
# # aobj=A()
# # aobj.m1()
# bobj= B()
# bobj.m1()

# Polymorphism with a Function and objects:-
# here create a function called “func()” (if you see this topic in brief go with yusuf sir's notes page_no_323)


# Method Overriding --
#    Method overriding is an ability of any object-oriented programming language that allows a subclass or
# child class to provide a specific implementation of a method that is already provided by one of its
# super-classes or parent classes. When a method in a subclass has the same name, same parameters or
# signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass
# is said tooverridethe method in the super-class.
#     The version of a method that is executed will bedetermined by the object that is used to invoke it. If an
# object of a parent class is used to invoke the method, then the version in the parent class will be
# executed, but if an object of the subclass is used to invoke the method, then the version in the child
# class will be executed. In other words, it is the type of the object being referred to
# (not the type of the reference variable) that determines which version of an overridden method will
# be executed
# However, what if the same method is present in both the superclass and subclass?
# In this case, the method in the subclass overrides the method in the superclass. This concept is known
# as method overriding in Python.
# Example: Method Overriding--
# class Animal:
#    #attributes and method of the parent class name=""
#    def eat(self):
#        print("Icaneat")
#        #inherit from Animal
# class Dog(Animal):
#    #overrideeat()method
#     def eat(self):
#        print("I like to eat bones")
#        #create an object of the sub class
# labrador=Dog()
# #call the eat()method on the labrador object
# labrador.eat()
# Output--
# I like to eat bones
# In the above example, the same method eat()is present in both the Dog class and the Animal class.
# Now,when we call the eat()method using the object of the Dog subclass, the method of the Dog class is called.
# This is because theeat()method of the Dog subclass overrides the same method of the Animal superclass.

# For example,--
# class Animal:
#     name=""
#     def eat(self):
#         print("I can eat")
#         #inherit from Animal
# class Dog(Animal):#override eat()method
#     def eat(self):
#      #call the eat()method of the super class using super()
#      super().eat()
#      print("I like to eat bones")
# #create an object of the sub class
# labrador=Dog()
# labrador.eat()

# Output--
# I can eat
# I like to eat bones
#
# # In the above example, theeat()method of theDogsubclass overrides the same method of the Animal super class.
# # Inside the Dog class, we have used
# #call method of superclass
# super().eat()
# # to call the eat()method of the Animal superclass from the Dog subclass.So, when we call the eat()method
# # using the labrador object
# #call the eat()method
# labrador.eat()
# # Both the overridden and the superclass version of the eat()method is executed.
# # Method Overloading in Python
# # In Python you can define method in such way that there are multiple ways to call it.We can pass number
# # parameters with multiple times

# Method Overloading:--
# Two or more methods have the same name but different numbers of parameters or different types of parameters,
# or both. These methods are called overloaded methods and this is called method overloading.
# The problem with method overloading in Python is that we may overload the methods but can only use the
# latest defined method.
# Example-1)--
# def product(a, b):
#     p = a * b
#     print(p)
#     # Second product method
#     # Takes three argument and print their product
# def product(a, b, c):
#     p = a * b*c
#     print(p)
#     # Uncommenting the below line shows an error
# # product(4, 5)
#     # This line will call the second product method
# product(4, 5, 5)
# Output--
# 100
# ** Abstraction in Python--
# Why Abstraction is Important?--
# In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity.
# It  also enhances  the  application  efficiency.  Next,  we  will  learn  how  we  can achieve abstraction
# using thePython program.
# In Python, abstraction can be achieved by using abstract classes and interfaces.A class that consists of one
# or more abstract method is called the abstract class.
# An abstract class can be useful when we are designing  large  functions.
# Python provides the abc module to use the abstraction in the Python program.
# (if you want to see Abstraction in detail, go with yusuf sir's notes. page_no_335)

# ** Encapsulation in Python--
# Encapsulation is one of the most fundamental concepts in object-oriented programming (OOP). This is the
# concept of wrapping data and methods that work with data in one unit.
#
# Encapsulation in  Python describes  the  concept  of bundling  data  and methods with in  a  single unit. So,
# for example, when you create aclass, it means you are implementing encapsulation. A class  is  an  example of
# encapsulation  as  it  binds  all  the  data  members  (instance  variables)  and methods into a single unit.
# (if you want to see Encapsulation in detail, go with yusuf sir's notes. page_no_335)
