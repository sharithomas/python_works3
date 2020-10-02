# Write a Python program to print alphabet pattern 'G'

  ***                                                                   
 *   *                                                                  
 *                                                                      
 * ***                                                                  
 *   *                                                                  
 *   *                                                                  
  *** 
cha_G=""
for row in range(7):
    for col in range(5):
        if ((col==0 or (col==4 and row!=2))and row!=0 and row!=6) or ((row==0 or row==6) and col!=0 and col!=4) or (row==3 and col!=1) :
            cha_G=cha_G+"*"
        else:
            cha_G=cha_G+" "
    cha_G=cha_G+"\n"
print(cha_G)
