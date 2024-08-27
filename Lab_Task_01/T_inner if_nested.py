#A nested loop has one or more loops within the body of another loop.

num1 = 30
num2 = 20
num3 = 40

if num1>num2:
    if num1>num3:
         print("This is ",num1)
else:
     print("This is ",num3)

if num2>num1:
     if num2>num3:
          print("This is ",num2)
else:
     print("This is ",num3)