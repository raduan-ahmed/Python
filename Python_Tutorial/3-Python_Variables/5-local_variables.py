#Local variables are those defined inside a function and are only accessible within that function.

def my_function():
    local_var = "Iam here don't worry about this"
    print(local_var)

my_function()
print(local_var)
# This will cause an error because local_var is not accessible outside the function