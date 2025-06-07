#string is surrounded by either single quotation mark or double quotation mark
#'hello' or "hello"
a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
print(a)


#interms of array
a="Hello,World"
print(a[3])


#loop through a string
for x in "banana":
  print(x)


#for a string length
b="Utsav Tamrakar"
print(len(b))


#check string
txt="The best things in life are free"
print("free" in txt)
  
  #also we can do like
txt="The best things in life are free"
if "free" in txt:
  print("Yes,'free' is present")


#check if not bool
txt="The best things in life are free"
print("expensive" not in txt)


#slicing:specify the start and end index separated by a colon,to return a part of a string
c='Utsav'
print(c[2:5])
#slice from start
print(c[:5])

#slice to the end
print(c[1:])

#negative indexing
print(c[-5:-1])


#uppercase and lowercase
a="Utsav Tamrakar"
print(a.upper())
print(a.lower())

#remove whitespace
print(a.strip())

#replace a string
print(a.replace("T" ,"t"))

#split string
print(a.split(","))

#concatenation string
a="Hello"
b="World"
c=a+b
print(c)
c=a+" "+b
print(c)

#format strings : for variables place {} brackets and need to simply put f in the front of the string literal
age=20
txt =f"My name is Utsav I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

#Escape characters:to insert characters that are illegal in a string,use an escape character...(\) denotion of escape character
#we cannot use double quotes inside a string 
#txt="We are the so-called"Vikings" from the north" to resolve it we use escape character simply 
txt= "We are the so-called \" Vikings \" from the north."
print(txt)

#String Methods
# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



#functions that returns boolean values
def myfunc() :
  return True
print(myfunc())

#Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))