#Power Calculation
def Cal(Num,Exp):
    if Exp == 0:
        return 1
    return Num * Cal(Num , Exp-1)
Base=int(input("Enter a Base Number --> "))
Exponent = int(input("Enter Exponentional Number --> "))
print(Cal(Base, Exponent))