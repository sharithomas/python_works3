#18.Write a Python program to print alphabet pattern 'M'

                                                               
  *       *                                                             
  * *   * *                                                             
  *   *   *                                                             
  *       *                                                             
  *       *                                                             
  *       *
cha_M=""
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or (row==2 and col!=2) or (row==3 and col!=1 and col!=3):
            cha_M=cha_M+"*"
        else:
            cha_M=cha_M+" "
    cha_M=cha_M+"\n"
print(cha_M)
