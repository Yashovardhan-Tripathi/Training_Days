#Factorial Solution
def factorail(N):
    if N<=1:
        return 1
    return N * factorail(N-1)

Num = int(input("Enter a number --> "))
print(factorail(Num))

# N=int(input())

# def Fact(Num):
#     if Fact <= 1:
#         return 1
#     return Num * Fact(Num-1)

# print(Fact(N))
# #Factorial Solution