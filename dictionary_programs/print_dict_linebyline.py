# Write a Python program to print a dictionary line by line.

students_dict= {'Alex':{'class':'V','rolld_id':2}, 'Puja':{'class':'V', 'roll_id':3}}
for i in students_dict:
    print(i)
    for j in students_dict[i]:
        print(j,':',students_dict[i][j])
