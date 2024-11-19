"""
Purpose: Feet to centimetres conversion
    1 foot = 12 inches
    1 inch = 2.54 centimetres
    
Algorithm:
            Step 1: Get feet values in runtime
            Step 2: compute from feet to cms
                    feet to inches, then 
                    inches to centimeters convension
            Step 3: Display the results

"""

# Get feet value at runtime
feet = input("Enter the value in feet: ")
feet = float(feet)

# Convert feet to inches
inches = feet * 12

# Convert inches to centimetres
centimetres = inches * 2.54

# Step 3: Display the result
print(feet, "is equal to", centimetres,"centimetres.")
