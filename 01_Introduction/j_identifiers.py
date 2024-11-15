"""
Purpose: Identifiers in Python

Variable
    Keywords: words which havelsome neaning in that language
    Identifiers: words which are defined by user (developers)

    Case sensitive
    Keywords should not be Identifiers
    first character a-z, A-Z, _
    remaining characters:a-z, A-Z, _, 0-9
PEP 8: Do not create identifiers similar to keywords ex: true
       Capitals for Constatnts (PI, DOZEN)

"""

#loading module

import keyword

print(keyword.kwlist)

print(True)

my_value = "something"
print(my_value) # Identifier
# True = "something"
# SyntaxError: cannot assign to True
print (keyword. iskeyword("True"))# True
print (keyword. iskeyword("true"))# False
print (keyword. iskeyword("my_value"))# False

# $name = "Priyanka"
# name-of-student = "Priyanka"
# name of student = "Priyanka"
# 1st_name = "Priyanka"

_2nd_student = "someone"
_job = "software development"
__role = "Product support"
__salary = 1231231232312323233

# OOP -> name mangling
# variable - Public variable
# _variable -› Protected variable
# __variable -> Private variable
#__variable__ -> Built in functions Ex: __file__, __name__,__exit__ 

