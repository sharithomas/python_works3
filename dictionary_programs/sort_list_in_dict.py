#   Write a Python program to sort a list alphabetically in a dictionary

dict1 = {'n1': ['apple','orange','banana'], 'n2': ['kiwi','watermelon','grapes'], 'n3': ['plum','strawberry','avacado']}
sort_dict={x:sorted(y) for x,y  in dict1.items()}
print(sort_dict)
