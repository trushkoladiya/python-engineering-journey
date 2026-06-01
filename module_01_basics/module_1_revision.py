# <- after this everything is ignored
# this is comment used for explain codes
# python runs code top to bottom line by line
# .py is extention - contains lines of codes
# python3 - REPL for quick testing
# indentation - python use this to group code
# 4 space per level of indentation

"""
this is multi line comment

    print("Trush") # this gives error
    
print("Trush") # always start from left edge

# we can use comment after print and etc..

"""

# in print for direct printing we use "" or ''
print("Trush Koladiya") # this is s - statement
print(2+3) # this line is s (it does something)

# but inside it like 2+3 is expression -e
# e calculate something and produce value
# s can contain e but not opposite

name = "Trush" # variable is a name that stores value
age = 21 # name and age is variable
age = "Not Want To Tell" # dynamic typing
print(type(name)) # type() used for checking type

# python is dynamic typing so we not have to declare types
# variable can change type  - python allows it
# Identifiers - variable names and other for naming things
# variable name can start with _ or letters
# private info variables name start with _ or __ (everyone use this way)
# using numbers allowed but starting with number not allowed
# spaces, python keywords and this(-) and other symbols not allowed
# naming is case sensitive age is not Age
# snake_case is recommended for variable naming
"""

Reserved Keywords that not allowed for naming

False    True     None
and      or       not
if       else     elif
for      while    break
continue pass     return
def      class    import
from     as       in
is       with     try
except   finally  raise

"""

a, b, c = 1, 2, 3 # valid - use meaningfull names
x = y = z = 0 # we can use this way too

a, b = b, a # now a = 2 and b = 1 (swapped)

# 4 data types
# int - 0, 5, -9, 25 ...
# flote - 5.0, -2.3, 4.5, 6.6 ...
# str - "", "369", "Trush", 'valid' ...
# bool - True, False (only 2) (First Capital) ...
# True or False is bool but true or false is not

print("A", "B", "C") # default saprator is " "
print("A", "B", "C", sep="-")
print("A", "B", "C", sep="") # print adds new line at end by default
print() # blank new line
print("Hello " + "Hii " + "HAU") # + for strings only (string joining)
print("line 1", end=" ")
print("line 2") # Line 1 Line 2 on one line
variable = 3 + 3
print(f"Hii {variable + 3} This is f string") # supports expression

# input() wait for user to type something and enter
input("Enter a number ") # meaning less - we not saving user input
user_age = input("Enter Your Age: ") # always returns a string

# for other data type as input we use this 
int(input("enter a number: "))
float(input("enter a number in decimal: "))
# still meaning less because we not stored

# explicit casting ( user do it )
# int("5") str to int
# float("369.369") str to float
# str(911) int to str
# float(5) int to float - 5.0
# int(5.5) float to int - 5 (cut decimal, not round)

# implicit casting ( python does it )
print ( 5 + 4.0 ) # int + float = float

# bool returns True or False based on values inside
# bool() if 0, 0.0, "" or falsy value then false
# bool(x) if any value or string then true

# int(), float(), str(), bool() are casting functions

# chained conversion int(float("3.14"))
# first float then int .. 2 level to go, direct not possible

# basic debugging - finding and fixing errors in code
# syntex error - broken grammer (python can't read it)
# syntex error - misspelled keyword, wrong identation or missing ),:,},] etc..
# runtime error - code written perfectly but when its run something goes wrong
# runtime error - sometimes operation it self not possible like zero divison..
# name error - using unknown variable or identifier
# type error - mixing incompatible types (like int + str)
# print(int("Hello") -> runtime (value error)
# error massage is key to find errors
# last line - error type and massage (read it first)
# line number - which line have error (then this)
# file name - which file have error (for large number of files)
# fix one error at a time (sometimes one fix fixes all errors)
# error reading from bottom to up...
# only reading is not enough, hands on practice gives experience and this is only for quick theory revision not for practice revision.
# solve problems and practice python everyday for better learning and gaining real experience.

# --------- end ---------