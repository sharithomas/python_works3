# Write a Python program that prints each item and its corresponding type from the following list.

 data_list = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
 for i in data_list:
     print(i,"   type: ",type(i))
