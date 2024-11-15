#1/usr/bin/python3
"""
Purpose: Working with comment operator
- Once # is encountered, complete line from that position is ignored
- PEP 8 recommends one white space after # operator
- comments
- Single Line comment #
- Multi-line comment - Python doesn't support
Question: Why python dont have multi-line comment operator
Answer : Python is a interpreter based language. means each line executes
Python code -> line by line -> c code > assembly -> Machine
print( 'Hello world1')
"""

print( 'Hello world2')
# print ('Hello world3')

print( "Hello #world4")
print ("Hello", "world5", sep="#")

print ("Hello world7") #
# print('Hello world8'#)
# SyntaxError: ( was never closed
# sidkjlkdj;wl kf*w; dp'kwf*;e kr'1@#$%^&*()
'''
Used to handle multi-line strings in cases where multiple single and double quotes are
'''
"""
used for docstrings
print 'Hello World8'

"""