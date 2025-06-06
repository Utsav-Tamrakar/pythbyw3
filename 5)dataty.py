#datatype:int,float,string,bool,list,tuple,range and so on.
x = "Hello World" # string data type
x=20 #integer
x=20.5  # float
x=2j  #complex
x=["apple","banana","cherry"]  #list
x = ("apple", "banana", "cherry") #tuple
x=range(6) #range
x = {"name" : "John", "age" : 36} #dict
x = {"apple", "banana", "cherry"} #set
x=True #bool
x = frozenset({"apple", "banana", "cherry"}) #frozenset
x = memoryview(bytes(5)) #memoryview
x=None #NoneType
x=bytearray(5) #bytearray
x = b"Hello"  #bytes
#data type conversion 
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))