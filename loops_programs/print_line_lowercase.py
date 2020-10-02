# Write a Python program that accepts a sequence of lines (blank line to terminate) 
#as input and prints the lines as output (all characters in lower case)

line=[]
# loop to accept the given datas and append it to a list line
while True:
    l=input()
    if l:
        line.append(l.lower())
    else:
        break
print("given lines: ")   
#print the list elements line by line
for i in line:
    print(i)
