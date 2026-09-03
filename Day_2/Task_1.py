# Mylist=[5 , 6 , 0 , 2 , 0 , 1 , 7]
Range = int(input("Enter the Range"))
Mylist=[]
for i in range(Range):
    Mylist.append(int(input("Enter the elements")))
print(Mylist)
for i in Mylist:
    if i == 0:
        Mylist.remove(i)
        Mylist.append(i)
print(Mylist)
