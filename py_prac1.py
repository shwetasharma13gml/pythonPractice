di={
      'name':'shweta',
      'age':'24',
      'job':'programmer'

}
a=di.get('name')
print(a)
print(di['name'])
print("total keys:")
for a in di.keys():
      print(a)
print("total values::::::::")
for i in di.values():
      print(i)
for a,b in di.items():
      print(a,"::",b)



course ={
      'python':{'time':'2 months','fees':'2500'},
        'java':{'time':'2 months','fees':'2500'},
      'data analysis':{'time':'2 months','fees':'2500'}
}
print(course)
print(course['java'])
for k,v in course.items():
      print(k,v)


import random
n= random.randint(2,9)
print(n)
l=[4,9,8,18]
lv=random.choice(l)
print(lv)
   #lambda


class democlass:
      a=10
      def fun(self):
            print("hi")
obj=democlass()
print("************FIRST CLASS*****************")
print(obj.a)
obj.fun()
class demo:
      def __init__(self,name,age):
            self.name=name
            self.age=age
p1=demo('shweta',24)
print("******SECOND CLASS**********")
print(p1.name)
print(p1.age)

print("*********OBJECT & CLASS **************")
class car:
      def __init__(self,model,company,color):
            self.model=model
            self.company=company
            self.color=color
      def prnt(self):
            print("my car model is:",self.model,self.company,self.color)

c1=car(6,"tesla","black")
c2=car(3,'mercedes','white')
c3=car(9,'bmw','gray')
c1.prnt()
c2.prnt()
c3.prnt()


print("*****************ENCAPSULATION*************************")
class student:
      def __init__(self):
            self.__name=""
      def getname(self):
            return self.__name
      def setname(self, name):
            self.__name=name
obj1=student()
obj1.setname("mamta")
name=obj1.getname()
print(name)


print("***********************INHERITANCE********************************")
class a:

      def __init__(self):

            print("hello world")
class b(a):
      def newly(self):
            print ("hi dear")
objb=b()
objb.newly()
class encp:
      __name="shweta"  # private variable
      def __init__(self): # constructor
            print(self.__name)
            self.__display() # private function calll in constructor
      def __display(self): #private function
            print("this is private function")

objc=encp()
objc()

