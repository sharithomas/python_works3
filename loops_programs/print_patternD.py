# Write a Python program to print alphabet pattern 'D'

 ****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *                                                                  
 ****  
cha_D=""
for row in range(7):
     for col in range(5):
         if (col==0 or (col==4 and (row!=0 and row!=6))) or ((row==0 or row ==6) and col!=4):
            cha_D=cha_D+"*"
         else:
            cha_D=cha_D+" "
     cha_D=cha_D+"\n"
print(cha_D)
