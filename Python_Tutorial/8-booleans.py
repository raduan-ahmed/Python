#Booleans represent one of two values: True or False.

print(10 > 9)
print(10 == 9)
print(10 < 9)
print("")

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print("")

print(bool("Hello"))
print(bool(15))
print("")

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print("")

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("")

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
print("")

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
