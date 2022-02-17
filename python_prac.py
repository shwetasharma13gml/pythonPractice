"""print("multi
      add
      sub
      div")
a=int(input("enter num1"))
b=int(input("enter num2"))

op=input("enter oper")

if(op=='+'):
    print(a+b)
elif(op=='-'):
    print(a-b)
elif(op=='*'):
    print(a*b)
elif(op=='/'):
    print(a/b)
else:
    print("wrong choice ")
    exit()"""




#table
def mult(x):
      for a in range(1,11):
            print(x,"*",a,"=",x*a)
mult(2)
mult(3)

# while loop
i=1
while i<=10:
      print(i,"my name is shweta")
      i=i+1
print(i)  # it well print i value last as 11 coz it will increment as 11 but when it will go under loop the condition will get false

s="my name is shweta SHARMA "
t=len(s)
print("LENGTH",t)  # length of the string
for a in range(t):
      print(s[a]) # will print one by one
print("*************************************************************")
for b in range(t-1,-1,-1):  #t-1==total len-1  becoz at begining we use forward indexing and
      print(s[b])

print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.swapcase())
print(s.find('s'))
print(s.find('s',10)) #it will start finding from 3rd index
print(s.index('s'))
print("*************************************************")
lis=[2,3,4,5,'s',"shweta"]
for a in lis:
      print(a)
n=8
lis.append(n) #append at last
print(lis)
li=[5,6,7,8]
lis.extend(li) #extend other list into list
print(lis)

print("list comprehension")
listy=[]
for a in range(1,10):
      listy.append(a)
print(listy)

ne=[1,2,3,4,5,6]
print(ne.count(6)) #number count
print(max(ne))# max number
print(min(ne))
ne.sort() #for sorting
print(ne)
ne.reverse()# for reverse
print(ne)
for a,b in zip(lis,ne): # two loop at same time ... if 1st list have 4 elements and 2nd has 5 elements then loop will print only 4 elements
      print(a,b)

ll=[]
for a in range(1,11):
      n=input("enter val"+str(a))  #ask user for list element
      ll.append(n) # append values in the list
print(ll)  #print the final list

print("""""""""""""""""""""""""""""""")



