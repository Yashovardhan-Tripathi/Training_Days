Num = int(input("ENter"))

# def Fibb(Num):
#     if Num  == 0 or Num == 1:
#         return Num
#     return Fibb(Num-1) + Fibb(Num-2) 
# print(Fibb(Num))

# n = int(input())

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(Num))