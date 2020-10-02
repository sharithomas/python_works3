# multiply number with 2 using function

def myfunc(n):
  return  lambda a: a * n

mydoubler = myfunc(2)

print(mydoubler(11))
