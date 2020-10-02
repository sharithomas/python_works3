# Write a Python program to find the second lowest grade of any student(s) from the given names and grades

#of each student using lists and lambda.Input number of students, names and grades of each student.
n=int(input("input number of students"))
list_students=[]
for i in range(n):
    name=input("name:")
    grade=int(input("grade"))
    list_students.append([name,grade])
print("names and grades of all students",list_students)
sort_list=sorted(list_students,key=lambda x:x[1])
length=len(sort_list)
print("second lowest grade is",sort_list[length-2][1])
