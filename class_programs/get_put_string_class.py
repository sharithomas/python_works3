#9. Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and
# print_String print the string in upper case
class String:
    def __init__(self):
        pass
    
    def get_string(self):
        string=input("input a string")
        self.string=string
        
    def print_string(self):
        print("string in upper case",self.string.upper())
        
new_class=String()
new_class.get_string()
new_class.print_string()
