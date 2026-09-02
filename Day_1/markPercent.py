'''WAP to accept three paper marks and calculate total, percentange and display it and check that all paper marks is greater 
than equal to 40 so print pass else print fail and check if per>60 and total marks is more than 100 so print you are eligible
for placement drive else print you are not eligible'''

M1=int(input("Enter Marks for Paper 1:- "))
M2=int(input("Enter Marks for Paper 2:- "))
M3=int(input("Enter Marks for Paper 3:- "))

Total_Marks=M1+M2+M3
print("Total Marks Are:-", Total_Marks)

Percentage=(Total_Marks/300)*100
print("Percentage is:-", (value= .2f)Percentage)

if M1>=40 and M2>=40 and M3>=40:
    print("You are Pass")
else:
    print("You are Fail")

if Percentage>60 and Total_Marks>100:
    print("You are Eligible for Placement ")
else:
    print("You are Not Eligible for Placement ")