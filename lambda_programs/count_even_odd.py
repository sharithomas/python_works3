#  Write a Python program to count the even, odd numbers in a given array of integers using Lambda

list_in=[2,5,6,7,19,10,23]
print("original array",list_in)
even_count=len(list(filter((lambda x:x%2==0),list_in))) #if x%2==0 is true accept that number from list_in and make a new list
print("number of even numbers=",even_count)
even_count=len(list(filter((lambda x:x%2!=0),list_in)))
print("number of odd numbers=",odd_count)
#another method
#list_count=list(map((lambda x: x%2 ),list_in))
#even_count=list_count.count(0)
#odd_count=list_count.count(1)
#print("number of even numbers=",even_count)
#print("number of odd numbers=",odd_count)
