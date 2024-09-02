my_list = ["Jessa", "Kelly", 20, 35.75]
# display list
print(my_list)               # ['Jessa', 'Kelly', 20, 35.75]
print(type(my_list))         # class 'list'

# Accessing first element of list
print(my_list[0])            # 'Jessa'

# slicing list elements
print(my_list[1:5])          # ['Kelly', 20, 35.75]

# modify 2nd element of a list
my_list[1] = "Emma"
print(my_list[1])            # 'Emma'

# create list using a list class
my_list2 = list(["Jessa", "Kelly", 20, 35.75])
print(my_list2)              # ['Jessa', 'Kelly', 20, 35.75]