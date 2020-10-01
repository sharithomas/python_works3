#  Write a Python program that takes a text file as input and returns the number of words of a given text file

#Note: Some words can be separated by a comma with no space.
def file_words(fname):
    with open(fname,'r') as f1:
        data=f1.read()
        data.replace(","," ")
        print(data)
        return(len(data.split(" ")))
    
print(file_words('example.txt'))
