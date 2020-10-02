# generators can be used inside for loop

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
    
for i in genfun():
    print(i)
    
