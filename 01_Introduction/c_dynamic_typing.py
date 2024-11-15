"""

Purpose: Python is a dynanic Typed Language.
    Progamming Languages
        Classification
            1. Static-Typed Languages
                first declare the variables, & then use them
                Int a, float b # Declaration
                а - 10 # initialization
            2. Dynamic Typed Languages
                create when you need. No declaration needed
                  num1 = 123
                  line or block exceution

python code --> python byte coder --> python Interpretor --> c compiler --> machine
python is slower compared to compiler based languages

"""
num1 =100
print(num1)
print ("num1")
print ("num1", num1)
print ("num1 =", num1)
print ("num1 =", num1, "type =", type(num1) )
# works in both static and dynamic typing
num1 = 300
print ("num1 =", num1, "type =", type(num1)) # int
# Python is dynamic-typed language
num1 = 300.0
print ("num1 =", num1, "type =", type(num1)) # float