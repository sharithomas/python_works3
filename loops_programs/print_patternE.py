# Write a Python program to print alphabet pattern 'E'

 *****                                                                  
 *                                                                      
 *                                                                      
 ****                                                                   
 *                                                                      
 *                                                                      
 *****
cha_E=""
for row in range(7):
    for col in range(5):
        if (row==0 or (row==3 and col!=4) or row==6) or col==0:
            cha_E=cha_E+"*"
        else:
            cha_E=cha_E+" "
    cha_E=cha_E+"\n"
print(cha_E)
