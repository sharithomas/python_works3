# Write a Python program to remove spaces from dictionary keys

student_dict = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
result_dict={}
print("original dictionary",student_dict)
for k,v in student_dict.items():
    if " " in k:
        k=k.replace(" ","")
        result_dict[k]=v
print("\n new dictionary",result_dict)
