# Numbers - INterger, Float, ComplexNumber
print("###Integer###")
a = 10
b = -112
print(a)
print(type(a))
print("###Float###")
fl =12.4
print(fl)
print("###ComplexNumber###")
com = 12 + 2j
print(com)

#Dictonary
print("###Dictinary###")
dic = {1: "Hello", 2: "welcome"}
print(dic[1])

#Boolean
print("###Boolean###")
bool = True
print(bool)

#Set
print("###Set###")
set1 = set("Hello")
print(set1)

#String, List, Tuple
print("###Sting###")
#len, lower, upper, concat, find, replace, split, join,

Str1 = "This is a first code"
Str2 = 'This is a second code'
Str3 = '''This is a third code 
This is fourth line'''
print(Str1.lower())
print(len(Str1))
print(Str1+Str2)
print(Str1.find("a"))
print(Str1.replace("a", "b"))


#List
#append, insert, index, remove, sort, reverse, pop, Slices, extend
list1 = [1,2,4,5]
list2 = [1,2,4,5]
print(len(list1))
list1.append(6)
list1.insert(2,3)
print(list1)
print(list1.index(4))
list1.remove(4)
list1.sort()
list1.pop()
print(list1)
print(list1[3:4])
list2.extend(list1)
print(list2)


#Tuple
tuple = (1,2,3,4)
print(tuple)




