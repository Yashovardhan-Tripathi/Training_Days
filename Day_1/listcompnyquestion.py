Array=int(input("Enter the size of array:"))
arr = []
for A in range(Array):
    arr.append(int(input("ENter an elements-->")))
print(arr)
Arr=0
# print(Arr= arr[0]-arr[1])
# print(Arr= arr[1]-arr[2])
# Arr=Arr+Arr
# print(Arr= arr[2]-arr[3])
# Arr=Arr+Arr
# print(Arr= arr[3]-arr[4])
# Arr=Arr+Arr
# print(
for i in range(Array-1):
    Arr+=arr[i]-arr[i+1]
    print(Arr)

print(Arr)
