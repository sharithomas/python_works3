# Write a Python function that prints out the first n rows of Pascal's triangle

n=int(input("enter numer of rows"))
#funtcion to create a pascal's triangle and save values in sublists and return the list
def pascal(n):
    a=[]
    for i in range(n):
        a.append([]) #append the sub-lists into the list.
        a[i].append(1) #append 1 into the sub-lists
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j]) #Each number is the two numbers above it added together
        if(n!=0):
            a[i].append(1)
    return a
            
b=pascal(n)   
#print list in pascal's triangle format
for i in range(n):
    print(" "*(n-i),end=" ")
    for j in range(0,i+1):
        print("{} ".format(b[i][j]),end=" ")
    print()
