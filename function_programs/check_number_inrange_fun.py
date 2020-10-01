# Write a Python function to check whether a number is in a given range.

number=int(input("enter number"))
#function definition to check whether given number is in the range of 1 to 10
def test_range(n):
    if n in range(1,10):
        print( str(n) + " is in the range of (1,10)")
    else :
        print("The number is outside the given range of (1,10).")
test_range(number)
