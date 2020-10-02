
#18. Write a Python program to print alphabet pattern 'L'


 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *                                                                      
 *****
cha_L=""
for row in range(7):
    for col in range(5):
        if col==0 or row==6:
            cha_L=cha_L+"*"
        else:
            cha_L=cha_L+" "
    cha_L=cha_L+"\n"
print(cha_L)
