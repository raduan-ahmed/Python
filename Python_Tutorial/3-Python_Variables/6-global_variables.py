#Global variables are defined outside any function and can be accessed from any function within the same program.

global_var = "I am global"

def my_function():
    print(global_var)

my_function()
print(global_var)
