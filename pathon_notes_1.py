# st = "ashishkhanmulla"
# print(st.count("a",0,9))
# endswith() method---
# print(st.endswith("p"))
# find( method)----
# print(st.find("s",4,6))
# format()method--
# print(st.format("kh"))
# k = "{} is my {}"
# print(k.format("this","world"))
# index() method--
# print(st.index("a",9))
# isalnum()method()---
# print(st.isalnum())
# isalpha()method()--
# print(st.isalpha())
# print(st.isalpha())
# st = "ashishkhanmulla"
# p = "14789"
# isdecimal()method--
# print(p.isdecimal())
# isnumeric()mehtod--
# print(st.isnumeric())
# isdigit()method--
# print(p.isdigit())
# islower()mehtod--
# print(st.islower())
# istitle()method--
# print(st.istitle())
# isupper() method--
# st = "ashishkhanmulla"
# print(st.isupper())
# len()method--
# print(len(st))
# replace()method--
# str = "gkkkg For lkkekl"
# new_str = str.replace("k","t",2)
# print(new_str)
# swapcase()method--
# print(st.swapcase())
# join--
# print("#".join(st))
# List---
# list1 = [1,7,8.3,"demo","spoon"]
# print(type(list1))
# concatination--
# k = [9,6,3,7,4]
# p = list1 + k
# print(p)
# leanth--
# print(len(list1))
# list1 = [1,7,8.3,"demo","spoon",4,77,99]
# itiration--
# for i in list1:
#     print(i)
# multipliction--
# print(list1*2)
# membership--
# print(111 in list1)
# print (list1[3::1])
# updeted list---
# list1[1:3]= 3
# list methods()--
# append--
# print(list1)
# list2 = ["tiger", "ziraf"]
# list2.append("rabbit")
# print(list2)
# list1.append(list2)
# print(list1)
# clear--
# list1.clear()
# print(list1)
# del--
# del list1[:]
# print(list1)
# list1 = [1, 7, 1, 1, 8.3, "demo", "spoon", 4, 77, 99]
# list2 = ["tiger", "ziraf"]
# 1st approach copy()--
# new_list1 = list1.copy()
# 2nd approach for copy--
# new_list1 = list1
# new_list1.append(300)
# print(list1)
# However, if you need the original list unchanged when the new list is modified, you can use the copy()method.
# Copy List Using Slicing Syntax--
# new_list1 = list1[:]
# new_list1.append(72003)
# print(list1)
# print(new_list1)
# when adding new item in new list it does not affect on old list
# count--
# print(list1.count(1))
# index--
# print(list1.index('demo', 3, 8))
#
# dal = 1,8,"kop",
# insert--
# # list1.insert(1,'joy')
# # print(list1)
# # pop--
# # list1.pop(2)
# # print(list1)
# # list1 = [1, 7, 1, 1, 8.3, 4, 77, 99]
# # list2 = ["tiger", "ziraf"]
# # pop()--
# # print(list1.pop(2))
# # print(list1)
# # remove--
# # print(list1.remove(77))
# # print(list1)
# # reverse()--
# # list1.reverse()
# # print(list1)
# # sort()--
# # list1.sort()
# # list1.sort(reverse=True)
# # list1.sort(reverse = True)
# # tuple---
# # concatenation--7,90
# jar = (7,9)
# print(dal+jar)
# membership--
# print("kop" in dal)
# iteration--
# for i in dal:
#     print(dal)
# length--
# print(len(dal))
# dal = 1, 8, "kop", 7, 90
# jar = (7, 8, 3, 1, 9, 9)
# j = [2, 3, 3, 4, 6, 7]
# convert data type---
# tt = list(dal)
# print(type(tt))
# tup = tuple(j)
# print(type(tup))
# index()--it return index of perticuler item or element--
# print(j.index(6))
# sum,max,min tuple functions--
# print(sum(jar))
# print(max(jar))
# sort()--?
# j.sort()
# dal = 1, 8, "kop", 7, 90
# jar = (7, 8, 3, 1, 9, 9)
# j = [2, 3, 3, 4, 6, 7]
# len()--
# print(len(dal))
# tuple convert into str or list--
# y = str(jar)
# print(type(y))
# how to append element in tuple--
# y = list(jar)
# y.append("jlj")
# jar = tuple(y)
# print(jar)
# print(type(jar))
# how to remove element in tuple--
# y = list(jar)
# y.remove(7)
# jar = tuple(y)
# print(jar)
# print(type(jar))
# python set--
# lat = {2,2,(3,"dd"),("k",9),3}
# print(lat)
# print(type(lat))
# g ={}
# print(type(g))
# mixed_set = set['Hello', 101, -2, 'Bye']
# print(type(mixed_set))
# add element to a set in python--
# lat.add(87)
# print(lat)
# update python set--
# lat = {2,4,"ll",(3,"dd"),("k",9),3}
# gen = ["kali",3,3,86,22,47]
# h = {1,2,3,4}
# lat.update(gen)
# print(lat)
# deletion from the set--
# 1)Remove--it can also work on tuple's element which inside in set
# lat.remove(22)
# print(lat)
# 2)Discard--it only work on set but not on tuple's element which inside in set
# lat.discard("ll")
# print(lat)
# 3)pop-- randomly remove element and return that element
# po = h.pop()
# print(po)
# 4)clear--
# lat.clear()
# print(lat)
# python set operation--
# lat = {2, 4, "ll", (3, "dd"), ("k", 9), 3}
# h = {1, 66, 2, 3, 4, "ll"}
# 1)union of two sets--
# print("union using |", lat|h)
# print("union using union()", lat.union(h))
# 2)Set Intersection--
# print("Intersection using &", lat & h)
# print("Intersection using Intersection()", lat.intersection(h))
# 3)Difference between Two Sets--
# print(lat - h)
# print(h.difference(lat))
# 4)Set Symmetric Difference--
# print("using ^",lat^h)
# print("using Symmetric Difference()", lat.symmetric_difference(h))
# 5)issubset--
# x={1,2}
# y={1,2,3,4}
# jk = (x.issubset(y))
# print(jk)
# 6)isdisjoint--
# x={1,2}
# y={3,4}
# jk = (x.isdisjoint(y))
# print(jk)
# 7) some other set operator
# print(x == y)
# print(x != y)
# print(x >= y)
# print(x <= y)
# print(x & y)
# print(x | y)
# print(x ^ y)
# Some Build in Methods:--
# x = {1, 2}
# y = {3, 4}
# 1)copy--
# z = x.copy()
# print(z)
# 2)len--
# z = x
# print(len(z))
# 4) min--
# print(min(z))
# 5)max--
# print(max(z))
# 6)sum--
# print(sum(z))
# 7)in--
# print(2 in z)
# 8)not in--
# print(2 not in z)
# 9)all--
# print(all(x))
# 10)sorted--
# print(sorted(z))
# a = 2
# b = 2
# print(a == b)
# print(type(a == b))
# print(type(a > b))
# Boolean Data Type--
# a = True
# print(type(a))
# # Python Dictionary Data Type--
# kk = {"name":"sam","age":44}
# print(kk)
# You can fetch a value from a dictionary by referring to its key in square brackets[].--
# print(kk["name"])
# cammand to avoid exception  if key not present in dictionory--
# print(kk.get("nn"))
# print(type(kk))
# The dict() Constructor--
# hh= ("v",4),('n',7)
# k = dict(hh)
# print(k)
# print(type(k))
# just replace value with new one in dictionory--
# kk["name"]="jorge"
# print(kk)
# If the key is new, it is added to the dictionary with its value.--
# kk["gender"]="male"
# print(kk)
# Python Dictionary Methods--
# kk = {"name":"sam","age":44}
# 1)clear() Removes all items from the dictionary--
# kk.clear()
# print(kk)
# 2)copy()Returns a shallow copy of the dictionary--
# u=kk.copy()
# print(u)
# 3)get()Returns the value of the specified key--
# print(kk.get("age"))
# 4)items()Returns a list of key:value pair
# print(kk.items())
# 5)keys()Returns a list of all keys from dictionary--
# print(kk.keys())
# 6)pop()Removes and returns single dictionary item with specified key.--
# s = kk.pop("age")
# print(s)
# print(kk)
# 7)popitem()Removes and returns last inserted key:value pair from the dictionary.--
# s = kk.popitem()
# print(s)
# print(kk)
# ///below notes comes under notbook poit- "Important Properties of Dictionary" which is written in notebook.
# There are three dictionary methods that return all of the dictionary’s keys, values and key-value pairs:keys()
# ,values(), and items().all wrap them in a list()function.--
# print(list(kk.values()))
# list() function is optional you can also wright print(kk.values())
# print(list(kk.keys()))
# print(list(kk.items()))
# Check if a Key or Value Exists
# print("name" in kk.keys())
# print(44 in kk.values())///
# 8)len()Returns how many key:value pairs in Dictionary
# print(len(kk))
# update()Updates the dictionary with the specified key:value pairs--
# kk.update({"name":"joy"})
# print(kk)
# kk.update({"gender":"male"})
# print(kk)
from selenium import webdriver
from selenium.webdriver.common.by import By


# Conditional Statements in Python--
# In Python we can achieve decision making by using the following statements:
# •if statements
# •if-else statements
# •elif statements•
# Nested if and if-else statements
# •elif ladder

# 1) •if statements
# Syntax:If(EXPRESSION==TRUE):
#    Block of code
# else:
#    Blockofcode
# Here, the condition will be evaluated to a Boolean expression (true or false).
# If the condition is true, then the statement or program present inside the ” if ” block will be executed
# and if the condition is false, then the statements or program present inside the “else” block will be executed.
# -------------------------------------------------------------------------------------------------------------
# ----------------------------------------------end of notes---------------------------------------------------





