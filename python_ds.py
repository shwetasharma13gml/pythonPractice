print("implementation of stack_ds")

l=[]
while True:
    c=int(input('''STACK OPERATIONS:
1.PUSH
2.POP
3.PEEK
4.DISPLAY
5.exit \n'''))
    if c==1:
        n=input("enter the value:")
        l.append(n)
        print(l)
    elif c==2:
        if(len(l))==0:
            print("no deletion can take place")
        else:
            p=l.pop()
        print("value that has been deleted is" ,p)
        print("updated list",l)
    elif c==3:
        if(len(l))==0:
            print("empty")
        else:
            print(l[-1])
    elif c==4:
        if (len(l)) == 0:
            print("empty")
        else:
            print(l)
    else:
        break

