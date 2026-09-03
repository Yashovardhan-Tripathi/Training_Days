def Array(A):
    if len(A) == 0:
        return 1
    return A[0] * Array(A[1:])
Range = int(input("Enter the Range --> "))
Mylist=[]
for i in range(Range):
    Mylist.append(int(input("Enter the elements --> ")))
print(Array(Mylist))
