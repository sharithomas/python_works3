# Write a python program to find the longest words

def longest_word(fname):
    max_len=0
    # open file and read string into a variable data 
    f1=open(fname,'r') 
    data=f1.read() 
    #split string word by word and save as a list 
    word=data.split()
    #from list word find word with maximum length 
    for i in word:
        if len(i)>max_len:
            max_len=len(i)
            max_word=i
    return (max_len,max_word)
    f1.close()

word=longest_word('example.txt')
print("word with maximum length:",word[1])
print("length:",word[0])
