name=[]
phn=[]
num=1
for i in range(num):
    na=input("name")
    num=int(input("enter number"))
    name.append(na)
    phn.append(num)
print("\nNAME\t\t\t NUMBER\n")


for j in range(num):
    print("{}\t\t\t{}".format(name[j], phn[j]))


search=input("\nEnter search")
print("search result")
if search in name:
    index=name.index(search)
    phnnum=phn[index]
    print("name {},phn:{}".format(search,phnnum))
else:
    print("not found")
