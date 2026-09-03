mylist=[2, 4 , 6 , 8 , 9 , 1 , 5 ]        # len = 7 ------> O(1)
even = 0                                  #         ------> O(1)
odd = 0                                   #         ------> O(1)
for i in range(len(mylist)):              # i=0<7   ------> On(N)
    if(mylist[i]%2==0):                   #         ------> O(1)
        even+=1                           #         ------> O(1)
    else:           
        odd+=1                            #         ------> O(1)
print(even, odd)                          #         ------> O(1)

# Total Time Complexity  -------->   O(1) + O(N) = O(N)