#  Write a Python program to print a dictionary in table format

import pandas as pd
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}      
table_dict=pd.DataFrame(my_dict)
print(table_dict)
