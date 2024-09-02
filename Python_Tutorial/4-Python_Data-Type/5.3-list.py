subjects = ["c", "c++", "java", "python", "R","R","React"]

print(len(subjects))
print("---------------------------")

subjects.append("javascript")
print(subjects)
print("---------------------------")

subjects.insert(2,"os")
print(subjects)
print("---------------------------")

subjects.remove("c++")
print(subjects)
print("---------------------------")

subjects.sort()
print(subjects)
print("---------------------------")

subjects.reverse()
print(subjects)
print("---------------------------")

subjects.pop()
subjects.pop()
print(subjects)
print("---------------------------")

 
subjects_2 = subjects.copy()
print(subjects_2)
print("---------------------------")

'''pos = subjects.index("4")
print(pos)
print("---------------------------")

pos = subjects.count("4")
print(pos)
print("---------------------------") 
'''

subjects.clear()
print(subjects)
print("---------------------------")

print("\n")