print("implementation of ds queue")
lis=[]
while True:
    v=int(input("QUEUE OPERATIONS:\n 1.INSERTION \n 2.DELETION OF FIRST ELEMENT \n 3.FRONT ELEMENT \n 4.LAST ELEMENT \n 5.DISPLAY \n 6.EXIT \n" ))

    if v==1:
        n = input("enter the value:")
        lis.append(n)
        print(lis)
    elif v==2:
        if len(lis)==0:
            print("no element for deletion")
        else:
            del lis[0]
            print(lis)
    elif v==3:
        if len(lis)==0:
            print("no element detected ")
        else:
            print(lis[0])
    elif v==4:
        if len(lis) == 0:
            print("no element detected ")
        else:
            print(lis[-1])
    elif v==5:
        print(lis)
    elif v==6:
        exit()
    else:
        print("invald choice")
