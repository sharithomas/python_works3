#5.Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
string=input("enter a string of parenthesis")
class Validity:
    def __init__(self):
        self.stack=[]
        self.par={'(':')','[':']','{':'}',}
    def validity_check(self,string):
        for i in string:
            if i in self.par:
                self.stack.append(i)
            elif len(self.stack)!=0 and self.par[self.stack.pop()]!=i:
                return False
        return len(self.stack)==0

v=Validity()   
check=v.validity_check(string)
if check==True:
    print("valid parenthesis")
else:
    print("not valid")
 
