#global variables:Variables that are created outside of a function.it can be used inside and outside of a function
x="awesome"
def myfunc() :
   print("Python is "+ x)

myfunc()

print("Python is " + x)


#global keyword is used to create a global variable inside of a function (global)
def myfunc() :
  global x
  x="fantastic"
  
myfunc()

print("Python is " + x)