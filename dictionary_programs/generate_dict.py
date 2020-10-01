# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

dict1={}
n=int(input("enter value of n"))
#creating dictionary
for i in range(1,n+1):
    dict1[i]=i*i
#print dictionary
print(dict1)
