# multiply number with 2 and 3 use function

def myfunc(n):
  return  lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
