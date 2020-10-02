#  Python program to generate squares from 1 to 100 using yield and therefore generator 

def square_number():
    i=1
    while True:
        yield i*i  #next execution resume from this point
        i=i+1
        
for num in square_number():
    if num>100:
        break
    print(num)
