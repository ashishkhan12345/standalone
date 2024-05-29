
# num=5
# if (num<10):
#     print("Num is smaller than 10")
# print("This statement will always be executed")
# In the above example,
# we declared a variable called ‘Num’ with the value as 5 and the ”if ” statement is checking whether the number
# is lesser than 10 or not. If the condition is true
# then a set of statements inside the if block will be executed.
# a = 7
# b = 0
# if b:
#     print("positive int")
# else:
#     print("negative int")
# If you observe, in the above example, we are not using or evaluating any condition in the “if” statement.
# Always remember that in any programming language, the positive integer will be treated as true value
# and an integer which is equal to 0 will be treated as false.Here the value of a is 7 which is positive,
# hence it prints true in the console output.
# Remember to use the (:) operator at the end of the if statement,
# because whatever the code you write after the colon operator will be apart
# of “if block” and indentation is very important in Python.
#2)if-elsestatements--
# The statement itself says if a given condition is true then execute the statements present inside the
# “if block” and if the condition is false then execute the “else” block
# if condition is True then the statements present inside the “if” block will be executed
# and the statements present inside the “else” block will be skipped.
# if-else statement evaluates the Boolean expression
#3)elifstatements--
# In Python, we have one more conditional statement called “elif” statements. “elif” statement is used to
# check multiple conditions only if the given condition is false. It’s similar to an “if-else” statement
# and the only difference is that in “else” we will not check the condition
# but in “elif” we will check the condition.
# Example:1
# num=10
# if(num==0):
#     print("Number is Zero")
# elif(num>5):
#     print("Number is greater than 5")
# else:
#     print("Number is smaller than 5")
# Output:Number is greater than 5
# In the above example we have declared a variable called ‘num’ with the value as 10,
# and in the “if” statement we are checking the condition if the condition becomes true.
# Then the block of code present inside the “if” condition will be executed.If the condition becomes false
# then it will check the “elif” condition if the condition becomes true, then a block of code present inside the
# “elif” statement will be executed.If it is false then a block of code present inside the “else” statement
# will be executed.
#4)Nested if-else statements--
# Nested “if-else” statements mean that an “if” statement or “if-else” statement is present inside another
# if or if-else block
# Nested if Example:1--
# num=7
# if(num!=0):
#     print("Number is not equal to Zero")
#     if(num>0):
#         print('Number is greater than Zero')
# Output:Number is greater than Zero
# Nested if-else Example:1--
# num=-7
# if(num!=0):
#     if(num>0):
#         print('Number is positive')
#     else:
#         print('Number is negative')
# else:
#     print('Number is Zero')
# Output: Number is negative
# num=-7
# if(num==0):
#     if(num>0):
#         print('Number is positive')
#     else:
#         print('Number is negative')
# else:
#     print('Number is Zero')
# Output: Number is Zero

#5)elif Ladder--
#This statement is used to test multiple expressions.
# Syntax:
# if(condition):
#     Set of statement to execute if condition is true
# elif(condition):
#     Set of statements to be executed when if condition is false and elif condition is true
# elif(condition):
#     Set of statements to be executed when both if and first elif condition is false and second elif
#     condition is true
# elif(condition):
#     Set of statements to be executed when if,first elif and second elif conditions are fals and third
#     elif statement is true
# else:
#     Set of statement to be executed when all if and elif conditions are false
# Example:1--
# i=20
# if(i==10):
#     print("i is 10")
# elif(i==15):
#     print("i is 15")
# elif(i==20):
#     print("i is 20")
# else:
#     print("i is not present")
# Output: i is 20
# If-else Statements In One Line
# Syntax:
# if(condition):statement 1;statement 2;statement 3;...;statement n
# else:statement 1;statement 2;statement 3;...;statement n
# There can be multiple statements as well, you just need to separate it by a semicolon (;)
# we can also write elif statement In One Line as above.
# we can also evaluate multiple conditions in an “if” statement with and, or operaor like below.
# Example:1--
# fruitName='Apple'
# if(fruitName=='Mango'or fruitName=='Apple'or fruitName=='Grapes'):
#     print("It's a fruit")
# Output:It’s a fruit
# Loops Statements in Python--
# In  general,  statements  are  executed  sequentially:  The  first  statement  in  a  function  is  executed
# first, followed by the second, and so on. There may be a situation when you need to execute a block of code
# several number of times.A loop statement allows us to execute a statement or group of statements multiple times.
# In Python, there are three different types of loops: for loop, while loop, and nested loop.
# While Loop in Python--
# In python, a while loop is used to execute a block of statements repeatedly until a given condition is
# satisfied. And when the condition becomes false, the line immediately after the loop in the program
# is executed.

# Let’s see a simple example of while loop in Python.
# Example-1
# age=32
# while age>18:
#     print('You can vote')


# Example-2
# kitchen= "Apple"
# count = 0
# while "Apple" in kitchen:
# while count <4:
#     count = count+1
#     print('Apple')
#
# Example-3
# count=0
# while(count<6):
#     count = count+1
#     print("HelloGeek")

#Example-4
# count=0
# while(count<3):
#     count=count+1
#     print("HelloGeek")
# Output--
# Hello Geek
# Hello Geek
# Hello Geek


# Syntax of While Loop with else statement--
# count=0
# while(count<10):
#     count=count+1
#     print("HelloGeek")
# else:print("InElseBlock")
# Output--
# Hello Geek
# Hello Geek
# Hello Geek
# In Else Block

# Note: It is suggested not to use this type of loop as it is a never-ending infinite loop where the condition
# is always true and you have to forcefully terminate the compiler.

# Python for Loop--
# In Python, theforloop is used to run a block of code for a certain number of times. It is used to iterate
# over any sequences such aslist,tuple,string, etc.The syntax of the for loop is:
# for val in sequence:
#   statement(s)
# Here,val accesses each item of sequence on each iteration. Loop continues until we reach the last
# item in the sequence.
# Workingforloop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).
# Example 1--
# Print each fruit in a fruit list:
# fruits = ["apple","banana","cherry"]
# for x in fruits:
#     print(x)
# Output --
# apple
# banana
# cherry

# Example 2--
# Looping Through a String--
# Even strings are iterable objects, they contain a sequence of characters:
# Loop through the letters in the word "banana":
# for x in "banana":
#     print(x)
# Output--
# b
# a
# n
# a
# n
# a

# The range() Function--
# Example--
# a = 5
# for i in range(0, a):
#     print(i)
# The range()function returns a sequence of numbers, starting from 0 by default, and increments by
# 1 (by default), and ends at a specified number.Therange()function returns a sequence of numbers between
# the give range
# Syntax of range()
# The range()function can take a maximum of three arguments:range(start,stop,step)The start and
# step parameters in range()are optional.
#
# for x in range(2,30,3):
#     print(x)
# Now, let's see how range()works with different number of argumentsWe use Python's built-in function range()
# to define a range of values. For example--
# values=range(4)
# for i in values:
#     print(i)
# Output--
# 0
# 1
# 2
# 3
# Python for loop with else
# A for loop can have an optional else block as well. The else part is executed when the loop is finished.
# Example1--
# digits=[0,1,5]
# for i in digits:
#     print(i)
# else:
#     print("No items left.")
# Output--
# 0
# 1
# 5
# Noitemsleft.
# Example2--
#
# for x in range(6):
#     print(x)
# else:
#     print("Finally finished!")

# When Should You Use For and While Loop?
# The for loop is used when weknowthe number of iterations, that is, how many times a statement must be executed.
# That is why, when we initialize the for loop, we must define the ending point.
#
# for i in range(11):
#     print(i)
#
# A while loop is used when the number of iterations isunknown. It is used when we need to end the loop on
# a condition other than thenumber of repetitions.
#
# i = 0
# while i <= 10:
#     print(i)
#     i = i + 1
