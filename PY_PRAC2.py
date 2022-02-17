print(ord('C'))  # ord() function takes string argument of a single Unicode character and return its integer Unicode code point value
print(chr(98)) # chr() function takes integer argument and return the string representing a character at that code point.


def print_name():
    print("hi there my name is shweta .........have  nice day ")

print_name()

print_new=lambda a,b,c:a+b+c
print(print_new(3,6,8))
print(print_new(13,43,56))

shweta=lambda x:print(x)
print(shweta("i am lambda"))


class area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("nothing")
obj=area()
obj.find_area(10)
obj.find_area(10,20)
obj.find_area()

