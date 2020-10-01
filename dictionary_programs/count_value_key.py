# Write a Python program to count the values associated with key in a dictionary.  

student = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]
count=0
#count number of dictionary which has success with value True
for i in student:
    if i['success']==True:
        count=count+1
    else:
        pass
print("count of dictionary with value True for key sucess = ", count)
