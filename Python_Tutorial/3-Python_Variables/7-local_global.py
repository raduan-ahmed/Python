# Global variable
global_var = "I am global"

def my_function():
    # Local variable
    local_var = "I am local"
    
    # Accessing global variable inside the function
    print(global_var)
    
    # Accessing local variable inside the function
    print(local_var)
    
    # Modifying global variable inside the function
    global global_var
    global_var = "I have been changed"

# Calling the function
my_function()

# Accessing global variable outside the function
print(global_var)

# Trying to access local variable outside the function will cause an error
# print(local_var)  # Uncommenting this line will cause a NameError
