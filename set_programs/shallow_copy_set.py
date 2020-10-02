# Write a Python program to create a shallow copy of sets

setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
setr=setp.copy() #shallow copy
print(setr)
