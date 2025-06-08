#List:It is used to store multiple items in a single variable...list are one of four built-in data types in python to store collections of data and the other three are Tuple,Set,and Dictionary.....
mylist=["football","Cricket","Volleyball"]
print(mylist)

#list are ordered,changeable and allow duplicate values.And they are indexed like in array first item[0] index,2nd [1] and so on...
#ordered: it means that the items have a defined order, and that order will not change.
#changeable:we can change, add, and remove items in a list after it has been created.
#allow duplicate: lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#For the length of a list
print(len(thislist))
#For a types of a list
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

print(type(list1))
#print(type(list2))
#print(type(list3))
#A list can contain different data types....
listtt=["abc",34,True,40,"male"]
print(listtt)

# list() constructor
thislist = list(("apple", "banana", "cherry"))   # note the double round-brackets
print(thislist)
print(thislist[1])
print(thislist[-1]) #negative indexing
print(thislist[:5]) #range of indexing

#check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#For a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
thislist.insert(1, "orange")
print(thislist)

#append():adds an item to the end of list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Extend list:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop() items from a list
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#delete a keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#delete a list
del thislist

#clear list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#loop through index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Loop using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension







