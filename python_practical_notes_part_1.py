# a = 'pthon'
# while 'pthon' in a:
#     print(a)
#     if a<10:
#
#
# a = 'pthon'
# count = 0
# while (count<10):
#     print(a)
#     count = count+1

# f = 44
# print(id(f))


# implicity type casting
# a = 4
# b = 66.6
# c = a+b
# print(c)
# print(type(c))
# explicit type casting
# a = 4.33
# b = str(a)
# print(b)
# print(type(b))

# a =-20
# b=-3
# c = a//b
# print(c)



# comeprison operator
# a= 66
# b = 3
# print('is equal to or not-----',a==b)
# print('is grater than or not-----',a>b)
# print('is less then or not-----',a<b)
# print('is grater then equal to or not-----',a>=b)
# print('is less then equal to or not-----',a<=b)
# print('is not equal to or not-----',a!=b)


# logincal operator
# a = 6
# b = 2
# print((a<b) and (a>b))
# print((a<b) or (a>b))

# assainment operator
# a =2
# b= 4
# a+=2
# print(a)
# b*=3
# print(b)
# a%=2
# print(a)
# i =2
# p=2
# u =i/p
# print(u)
# print(a==2)
# a**=2
# print(a)
#


# identical operator
# a = 2.3369
# b = 2.3369
# print(id(a))
# print(id(b))
# print(a is not b)

# # membership operator
# cal = (3,4,'hi',7.8)
# l = ['j',44,6]
# s = 'entertenment'
# print(3 in cal)
# print(66 not in l)
# print('r'in s)
# print(44 in cal)

# input function
# a = input('enter your age--')
# a=int(a)
# print(type(a))
# b =(a*a)
# print(b)


# concatination
# a = 'hello'
# b = 'sir'
# c = a+'  '+b
# print(c)

# multiplication
# c = a*2
# print(c)



# string slicing
# name = 'credance'
# print(name[0])
# print(name[8])
# print(name[6])
# print(name[:4])
# print(name[-6:-1:2])
# print(name[:])
# print(name[::-1])
# print(name[::-4])
# print(name[::3])


# python string methods
# name = 'i am a boy with lots of abitions'

# print(name.replace('o','i',4))
# print(name.title())
# n = 'I Am A Boy With Lots Of Abitions'
# print(n.casefold())
# print(name.count('o',0,12))
# print(name.endswith('s'))
# print(name.find('a'))
# print(name.index('a'))

# format() method
# my_string = "{} is a {}software testing {} for students"
# print(my_string.format('credance','computer','class'))
# name = '{} all how are {} my name is {}'
# print(name.format('hi','you','ashish'))

# name = 'i am a boy with lots of abitions'
# find method
# print(name.find('b',1,8))
# print(name.index('b',1,8))
# isalnum method
# print(name.isalnum())
# print(v.isalpha())
# v = '2'
# print(v.isnumeric())
v = "93 "
# print(v.isalpha())
# print(v.isdigit())
# s = "7²"
# print(v.isnumeric())
# print(s.isdecimal())
# print(s.isdigit())
# name = 'I  Am A Boy With Lots Of Abitions @4233'
# print(name.casefold())
# print(len(name))
# h = 'skie ksie@@@^'
# print(h.upper())
# print(name.istitle())
# name = 'i am a boy @#$'
# print(name.casefold())
# print(name.count('a',0,4))
# print(name.swapcase())
# print(name.lower())
# print(len(name))
# string = "geeks for geeks\n" "geeks for geeks"
# print(string.replace("geeks for geeks",'hey'))
# print(string.replace('gee','u'))
# print(string.replace('geeks','tt',2))
# s1 = 'abc'
# print(s1[1])
# s2 = '123'
# print(s1.join(s2))
# s = 'credance'
# print(s.count('e',2,9))
# print('$'.join(s))

# list---
# repitation--
# list1 = [2,3,'hi',44,4.9]
# l = list1*2
# print(l)

# concatination
# list2 =[23,24,'all']
# for i in list2:
#     print(i)
# l = list1+list2
# print(l)

# len
# print(len(list1))

# membership
# print(23 in list2)
# print('all' in list2)
# print(99 in list2)
# print(888 not in list2)
# list1 = [2,3,'hi',44,4.9,22,66]
# print(list1[2:5:2])
# print(list1[::-2])
# print(list1[2::2])
# print(list1[-2::-3])
# print(list1[:-1])
# print(list1[-7:1])
# l = list1[::2]
# p = list1[1::2]
# print(l+p)
# list1 = [2,3,'hi',44,4.9,22,66]
# list1[-1]=6
# list1[1:3]='i','am'
# print(list1)
# thislist = ["apple","banana","cherry","orange","kiwi","mango"]
# thislist[1:3] = ["blackcurrant","watermelon"]
# print(thislist)
# list1.append('all')
# print(list1)
# list1.insert(2,'all')
# list1.clear()
# print(list1)
# list1 = [2,3,'hi',44,4.9,22,66]
# m = list1.copy()
# m = list1
# m = list1[:]
# print(m)
# m.append('all')
# print('old list',list1)
# print('new_list',m)
# print(list1.count(3))
# del list1
# print(list1)
# list1 = [2,3,44,4.9,22,66]
# list1.reverse()
# print(list1)
# n = ['ahish','mulla','heena']
# print(n)
# list2 = (66,963,77)
# list1.extend(list2)
# print(list1)
# print(list1.index(3,1,9))
# list1.insert(1,44)
# list1[1]=44
# print(list1)
# list1.insert(0,list2)
# print(list1)
# print(list1.pop(2))
# print(list1)
# list1.remove('hi')
# del list1[1]
# print(sum(list1))
# print(list1)
# list1.reverse()
# print(list1)
# n = ['ashish ','mulla']
# n.sort(reverse=True)
# n.reverse()
# print(n)
# list1 = [2,3,44,4.9,22,66]
# list2 =66,963,77
# print(type(list2))
# print(list1[3])
# list1.sort(reverse=True)
# print(sorted(list1,reverse=True))
# print(list1)


# tuple
# t1 =66,963,77
# t2 = (4,6,77)
# print(t1+t2)
# print(t1*2)
# for i in t1:
#     print(i)
# b = 66 in t1
# print(b)
# print(len(t1))
# print(t1[1])
# a,b,c = t1
# print(a)
# print(t1.index(77,0,4))
# t1 =66,963,77
# print(sorted(t1))
# print(t1)
# y = list(t1)
# y.sort()
# print(y)
# print(type(y))

# n = set (('sie',4))
# n = {'sie',4}
# print(n)
# print(type(n))
Days={"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",7,"Sunday",1,2,3,4}
i = {33,14}
# p = 'kaya',1
# print(Days)
# Days.add(44)
# Days.update(p)
# Days.remove('Sunday')
# u = Days.difference(i)
# print(u)
# print(Days^i)
# print(i.isdisjoint(Days))
# m=1 in Days
# print(m)
# a = {'hi':[4,'lp'],'Hi':6}
# a= (['hi',4],[42,33],[7,'p'],(77,33))
# print(type(a))
# print(a)
# b = dict(a)
# print(b)
# print(type(b))
# a = dict(surname='ravi',name=22)
# print(type(a))
# print(a)
# a = {(2,2):'hi',4:77}
# print(type(a))
# print(a)

# print(a[(2,3)])
# Dict={'Dict1':{1:'Geeks'},'Dict2':{'Name':'For'}}
# print(Dict['Dict1'][1])
# a ={778: 4, 42: 33, 7: 666, 77: 33}
# print(sorted(a.values()))
# d = a[42]
# print(d)
# print(33 in a.values())
# a[66]=2
# print(a)
# b = {42.2:77,6.3:7}
# print(b)
# bb = b.popitem()
# print(bb)
# a.update(b)
# print(a)
# print(type(a))
# b.pop(42.2)
# del b[42.2]
# print(b)
# print(b)
# hh = b.copy()
# print(hh)

# condtional statment
# kitchen = 'apple'
# if kitchen == 'apple':
#     print('ha hai apple')
# print('thik hai')

# a = 10
# if a == 0:
#     print('a is equal to 0')
# elif a==7:
#     print('a is qual to 7')
# elif a >0:
#     print('a is grater then 0')
# else:
#     print('a is negative')
# print('last statment')
# a = 10
# if a <100:
#     if a !=10:
#         print('ye rong hai')
#     else:
#         print('a is equal to 10')
# else:
#     print('galat')

# loop statment
# while loop--
# kithen = 'apple'
# while 'apple'in kithen:
#     print('ha hai')
#     kithen = 'banana'
# c = 0
# while c <=3:
#     print('condtion satisfy')
#     c = c +1

# for loop--
# a = 'gfft vnghf'
# for i in range(len(a)):
#     print(i)
# for i in range(7):
#     for j in range(1,i):
#         print(j,end=' ')
#     print(' ')
a = 7
# for i in range(a):
#     sp = ' '*(a - i)
#     s = '*'*(2*i-1)
#     print(sp+s)
# for i in range(a,0,-1):
#     sp = ' '*(a - i)
#     s = '*'*(2*i-1)
#     print(sp+s)
# s = 7
# for i in range(s):
#     for j in range(i):
#         print('*',end=' ')
#     print(' ')
# def count(num):
#     if num<=0:
#         print('stop')
#     else:
#         print(num)
#         count(num-1)
# count(5)
# def greet():
#     print('hello')
#     greet()
# greet()
# def i(x,y=22):
#     print(x)
#     print(y)
# i(3,3)
# def j(kk):
#     print(kk)
# j('ieoe')
# def name(name,age):
#     print(name)
#     print(age)
# name(22,'ld')
# def s():
#     p = 'kk'
#     print(p)
# s()



# exeptional hadling--
# try:
#     a = 5
#     b = -1
#     print( a/b)
# except:
#     print('some error occured')
# print('out of except block')


# def AbyB(a , b):
#     try:
#         c = ((a+b) / (a-b))
#     except:
#         print ("a/b result in 0")
#     else:
#          print (c)
# # Driver program to test above function
# AbyB(3.0, 3.0)


# def hi():
#     try:
#         a= 12
#         b = 'l'
#         c = a+b
#         print(c)
#
#     except:
#         print('it is not right')
#     else:
#         print('ok')
#
# hi()


# file handling--
# f = open('cut.txt','r')
# print(f.readline())
# print(f.readline())

# f = open('ct.txt','w')
# print(f.write('lets see'))
# f.close()
# f= open('ct.txt','r')
# print(f.read())

# f = open('kk.txt','x')
# f = open("kk.txt",'w')
# print(f.write('kase ho'))
# f = open('cut.txt','r')
# for i in f:
#     print(i)

import os
# os.replace('ct.txt','ccc.txt')

# try:
#     os.remove('ccc.txt')
#     print('file has been removed')
# except:
#     print('fil not found')


# if os.path.exists("C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Stanalone\\cut.txt"):
#     os.remove("C:\\Users\\DEP\\PycharmProjects\\pythonProject\\Stanalone\\cut.txt")
#     print('file removed')
# else:
#     print("file not found")



## in instance method need to create object to access the method--
# class kk:
#     def jj(self):
#         a = 4
#         b= 2
#         c = a+b
#         print(c)
# l = kk()
# l.jj()


## in staticmethod don't need to create object to access the method--
# class kk:
#     @staticmethod
#     def jj():
#         a = 4
#         b= 2
#         c = a+b
#         print(c)
# #        jj()
# kk().jj()

# class ll:
#     def kk(self,x,y):
#         print(x+y)
# p = ll()
# p.kk(2,3)


# class Myclass4:
#     # a,b=10,20
#     def add(self,a,b):
#         print(a+b)
#         # print(self.a+self.b)
#         # print(a+b)
# mc4=Myclass4()
# mc4.add(1000,2000)
# class k:
#     def l(self):
#         a = 4
#         b = 2
#         c = a * b
#         if c == 9:
#             print('test pass')
#             assert True
#         else:
#             print('test fail')
#             assert False
# o = k()
# o.l()


