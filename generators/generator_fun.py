# example for generator function

def genfun():
    n=1
    print("first print")
    yield n
    
    n+=1
    print("second print")
    yield n
    
    n+=1
    print("third print")
    yield n
    
a=genfun()
next(a)
next(a)
next(a)
