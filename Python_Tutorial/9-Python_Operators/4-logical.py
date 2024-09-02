#Python Logical operators perform Logical AND , Logical OR , and Logical NOT operations. 
#It is used to combine conditional statements.

a = True
b = False
print(a and b) 
print(a or b) 
print(not a) 
print("--------------")

x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
print("--------------")

x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
print("---------------")

x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result
