"""
Purpose: Multiple statements in same line
    , logic separator
    ; statement completion operator
"""
print("Hello" "world")
print ("Hello", "world")
print ("Hello", 21312)
# print ("Hello" 21312)
# SyntaxError: invalid syntax. Perhaps you forgot a commma?
print ("Hello", 21312, 213, 123 + 123 - 3)
print()


"""

python -c "print('Hello World')"

used for scripting and general
"""