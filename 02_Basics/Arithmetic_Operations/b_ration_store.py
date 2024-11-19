"""
Algorithm
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items into variables
Step 3:0
Compute the selling price to each item, and add them
Step 4:
Compute the subsidy amount and subtract from the selling price
Step 5: Display the Billable Amount

P - PARANTHESES
E - EXPONENT
M - MULTIPLCATION
D - DIVISION
A - ADDITION
S - SUBTRACTION

"""
# cost of Items
cost_of_wheat = 25
cost_of_rice = 12
# Quantities of Items
qty_of_wheat = 30 #kgs
qty_of_rice = 50 # kgs

# Selling Price Computation
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice
total_sp = sp_of_wheat + sp_of_rice
print ("Total Selling Price=", total_sp)

# Subsidy calculation at 20 % subsidy
subsidy_amount = (total_sp * 20)/ 100 #PEMDAS
print ("Subsidy Amount: ", subsidy_amount)

billable_amount = total_sp - subsidy_amount
print ("Billable Amount: ", billable_amount)